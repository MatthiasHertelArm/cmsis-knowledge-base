---
id: "view-elemhead-component-viewer-objects-3"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/objects/object/.../list}"
summary: "The element <list> allows to create a: - for loop that increments in each iteration a loop variable by 1 until it reaches the limit. - while loop that stops executing when a while condition becomes 0."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

The element `<list>` allows to create a:
  - **for** loop that increments in each iteration a loop variable by `1` until it reaches the **limit.**
  - **while** loop that stops executing when a **while** condition becomes `0`. 

The child elements of the `<list>` element are executed therefore multiple times.

**Note:**  It is not possible to combine **limit** and **while** in the same `<list>` element.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<object>` | elem_object |  |  |
| \refelem{elem_list,list} | elem_list |  |  |
| Attributes | Description | Type | Use |
| name | The name of a loop variable that is defined previously defined with the element `<var>`. When **limit** is specified, this variable is incremented by `1` with every loop iteration. | xs:string | required |
| start | Expression that specifies the initial value of the loop variable. | xs:string | required |
| limit | Expression that specifies the limit value of the loop variable. The loop is terminated when `limit` >= `loop variable`. | xs:string | optional |
| while | Expression that terminates loop execution when the result is `0`. Default value is `1`. | xs:string | optional |
| cond | Conditional execution: element is executed when expression result is not `0`. Default value is `1`. | xs:string | optional |
| Child Element | Description | Type | Occurrence |
| \refelem{elem_list,list} | Iterate a loop (for or while construct). | ListTypeO | 0..* |
| `<readlist>` | Read a list of structured variables (arrays or linked list) from application program. | ReadlistType | 0..* |
| `<read>` | Read scalar variables or arrays from application program. | ReadType | 0..* |
| `<var>` | Define temporary variables. | VarType | 0..* |
| `<calc>` | Calculate temporary variables. | CalcType | 0..* |



**Examples:**

**for** loop execution:

```
<object name="For_Loop">
  <var  name="i"   type="uint32_t"            />
  <var  name="j"   type="uint8_t"  value="5"  />
  <list name="i" start="0" limit="10" >
    <calc>
      j = j + i;
    </calc>
   </list>
</object>
```

**while** loop execution:

```
<object name="While_Loop">
  <list cond="Threads:TCB[i].State==WaitingMutex" name="m" start="Threads:TCB[i].OS_MUCB" while="Threads:MCB(m).p_mlnk"> 		   
            <item property="Mutex : %x[Threads:MCB(m).index]" value="Owner=%s[Threads:TCB_DEF(Threads:TCB(Threads:MCB(m).owner).Thread_Def).name"/>
          </list>
  <var  name="i"   type="uint32_t"            />
  <var  name="j"   type="uint8_t"  value="5"  />
  <list name="i" start="0" limit="10" >
    <calc>
      j = j + i;
    </calc>
   </list>
</object>
```
