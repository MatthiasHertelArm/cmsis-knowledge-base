---
id: "intr-using-swig-to-generate-bindings-be-passing-a-custom-c-struct-to-lua"
type: "concept"
domain: "debug"
title: "Using SWIG to generate bindings between C and Lua: Passing a custom C struct to Lua"
summary: "We have called a simple C function from Lua, but what about passing struct data?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-11-29-swig-for-c-and-lua.md"
doc_source: "https://interrupt.memfault.com/blog/swig-for-c-and-lua#passing-a-custom-c-struct-to-lua"
license: "CC-BY-SA-4.0"
mode: "V"
---

We have called a simple C function from Lua, but what about passing struct data? As our application evolves, we’ll most likely add custom types and complicated data structures - the source of the massive amount of wrapper code that exists in many repositories that use Lua from C host program. For reference this is `example2`.

Let’s start with defining our data types in C header `types.h`:

```c
typedef enum
{
    LEVEL_NONE = 0,
    LEVEL_LOW,
    LEVEL_MEDIUM,
    LEVEL_HIGH,

} LEVEL_enum_t;

typedef struct
{
    LEVEL_enum_t level;
    uint8_t priority;
    char message[64];
    bool isReady;
} my_struct_t;
```

And a SWIG interface, `bindings.i`, that will include the above C header:

```
%module bindings

%{
#include "types.h"
%}

%include "types.h"
```

If we look into the generated C file from SWIG, we’ll see setters and getters for each of the fields of the structure, as well as a constructor and destructor for the struct.

Assuming we’d not only like to receive a structure passed from C in Lua but also modify it, we’ll write a Lua script that will drive our C implementation:

```lua
function processStruct(struct)
    -- Print our structure
    print("[Lua] struct.level = " .. tostring(struct.level))
    print("[Lua] struct.priority = " .. tostring(struct.priority))
    print("[Lua] struct.message = " .. struct.message)
    print("[Lua] struct.isReady = " .. tostring(struct.isReady))

    -- Now let's modify the structure
    struct.level = bindings.LEVEL_NONE
    struct.priority = 99
    struct.message = "Hey from Lua"
    struct.isReady = false
end
```

We introduced `processStruct` function, which we will call from C and pass a C structure to it, and expect the structure to be modified by Lua.

To call this Lua function from C we need to write a piece of C code using APIs from SWIG runtime header. First, we will generate the runtime header:

```
/app/example2 # swig -lua -external-runtime swig_runtime.h
```

Then write a C function to call Lua’s `processStruct` function:

```c
void callProcessStruct(lua_State *L, my_struct_t *my_struct)
{
    lua_getglobal(L, "processStruct");
    assert(lua_isfunction(L, -1));

    swig_type_info *type = SWIG_TypeQuery(L, "my_struct_t *");
    assert(type != NULL);
    SWIG_NewPointerObj(L, my_struct, type, false);

    // Call function with 1 arguments and no result
    assert(lua_pcall(L, 1, 0, 0) == LUA_OK);
}
```

Here, in `callProcessStruct` we first grab Lua’s `processStruct` function on top of the stack. Then, we get type info for our C structure using `SWIG_TypeQuery` , followed by pushing the pointer on the stack with `SWIG_NewPointerObj`. That call creates a userdata on Lua’s stack containing our C structure. Finally, we call our Lua function.

The rest of the application is just setting up the C structure with initial values, and printing the structure after the call to Lua:

```c
my_struct_t my_struct;
my_struct.isReady = true;
my_struct.level = LEVEL_MEDIUM;
strncpy(my_struct.message, "This is example message", sizeof(my_struct.message));
my_struct.priority = 100;

printf("[C] Calling processStruct\r\n");
callProcessStruct(L, &my_struct);
printf("[C] We're back from Lua\r\n");

printf("[C] Printing my_struct\r\n");
printf("\tmy_struct.level = %d\r\n", my_struct.level);
printf("\tmy_struct.priority = %d\r\n", my_struct.priority);
printf("\tmy_struct.message = %s\r\n", my_struct.message);
printf("\tmy_struct.isReady = %s\r\n", my_struct.isReady ? "true" : "false");
```

Here’s the output:

```
[C] Calling processStruct
[Lua] struct.level = 2.0
[Lua] struct.priority = 100.0
[Lua] struct.message = This is example message
[Lua] struct.isReady = true
[C] We're back from Lua
[C] Printing my_struct
        my_struct.level = 0
        my_struct.priority = 99
        my_struct.message = Hey from Lua
        my_struct.isReady = false
[C] Finished
```

It worked! Lua was able to modify our enum, integer, string, and boolean. To get a peek under the hood, let’s use a well-known Lua [inspect](https://github.com/kikito/inspect.lua) library, which gives us information about objects.

After importing the library with `require`, we add two lines to `processStruct`:

```lua
print("[Lua] struct: " .. inspect(struct))
print("[Lua] struct metatable: " .. inspect(getmetatable(struct)))
```

And get the following print (truncated):

```
[Lua] struct: <userdata 1>
[Lua] struct metatable: <1>{
...
  [".get"] = {
    isReady = <function 2>,
    level = <function 3>,
    message = <function 4>,
    priority = <function 5>
  },
	[".set"] = {
    isReady = <function 6>,
    level = <function 7>,
    message = <function 8>,
    priority = <function 9>
  },
...
```

You can see from Lua's point of view, the object is Lua’s [userdata](https://www.lua.org/pil/28.1.html), which means it’s raw memory. Normally userdata is managed by Lua meaning it will be garbage collected. However, SWIG gives us flexibility here with its `SWIG_NewPointerObj` API. The last argument to that function specified the owner of the object, and since we decided to own the object the garbage collector won’t affect it.

The interesting bit is our struct’s metatable. As you can see from the print, the metatable contains function pointers including getters and setters. This is the main part SWIG took care of for us.

And if you’re wondering whether a known sized buffer, like the string buffer `char message[64];` can overflow, SWIG handles that and would just truncate the string as seen in the generated `swig.c`:

```c
strncpy((char*)arg1->message, (const char *)arg2, 64-1);
arg1->message[64-1] = 0;
```
