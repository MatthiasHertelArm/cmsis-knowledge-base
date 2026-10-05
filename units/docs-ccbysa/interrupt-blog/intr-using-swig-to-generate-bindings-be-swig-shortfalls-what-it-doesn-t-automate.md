---
id: "intr-using-swig-to-generate-bindings-be-swig-shortfalls-what-it-doesn-t-automate"
type: "concept"
domain: "debug"
title: "Using SWIG to generate bindings between C and Lua: SWIG shortfalls - what it doesn’t automate"
summary: "Ok, that’s great so far! But what about arrays? We passed a string, an array of chars but what about an array of numbers or custom types? Here’s where things don’t sail as smoothly."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-11-29-swig-for-c-and-lua.md"
doc_source: "https://interrupt.memfault.com/blog/swig-for-c-and-lua#swig-shortfalls-what-it-doesn-t-automate"
license: "CC-BY-SA-4.0"
mode: "V"
---

Ok, that’s great so far! But what about arrays? We passed a string, an array of `char`s but what about an array of numbers or custom types? Here’s where things don’t sail as smoothly.

Consider a modification to our structure:

```c
typedef struct
{
    uint8_t priorities[3];

} my_struct_t;
```

Now the structure contains a known size array of numbers. Following the previous example, let’s inspect `struct.priorities` from Lua using:

```lua
print("[Lua] struct.priorities: " .. inspect(struct.priorities))
print("[Lua] struct.priorities metatable: " .. getmetatable(struct.priorities))
```

Output:

```
[Lua] struct.priorities: <userdata 1>
[Lua] struct.priorities metatable: nil
```

Our array `priorities` is userdata and it doesn’t have an assigned metatable. Therefore Lua cannot do anything with it! That’s not something we expected from a generator tool, after all we’re talking about handling the simplest possible array.

And it is a common problem, even SWIG documentation states:

> Arrays present a challenge for SWIG, because like pointers SWIG does not know whether these are input or output values, nor does SWIG have any indication of how large an array should be.
>

To address this problem we can write a typemap in our SWIG interface file, which will include our custom code to push the array onto Lua stack:

```
%typemap(out) uint8_t my_struct_t::priorities[3]
{
    lua_newtable(L);
    for (uint32_t i = 0; i < 3; i++)
    {
        lua_pushnumber(L, (lua_Number)$1[i]);
        lua_rawseti(L, -2, i + 1); // Lua indexes start from 1
    }

    SWIG_arg++;
}
```

However, this becomes tedious as now we’re writing the exact boilerplate code we were trying to avoid!

This time, inspection of `priorities` array gives:

```
[Lua] struct.priorities: { 1.0, 1.0, 1.0 }
[Lua] struct.priorities metatable: nil
```

Now Lua knows it’s a table, but we’re limited to read-only access. To have the ability to modify the array members we’d, unfortunately, need to write a custom modifier code.
