---
id: "stream-faqs-performances"
type: "concept"
domain: "cmsis-stream"
title: "FAQs: Performances"
summary: "The use of C++ templates is giving more visibility to the compiler:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/FAQ.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/FAQ.md#performances"
license: "Apache-2.0"
mode: "V"
---

The use of C++ templates is giving more visibility to the compiler:

* The number of samples read and written on the FIFOs are statically known ;
* When a FIFO is used as a simple array : it is statically visible to the compiler 
* The dataflow between the nodes is statically visible

It enables the compiler to generate better code for the C++ wrappers and minimize the overhead.

As an example, let's look at the graph:

(figure: perf)

The full code for all the nodes is:

```C++
template<typename IN, int inputSize>
class Sink;

template<int inputSize>
class Sink<float32_t,inputSize>: 
public GenericSink<float32_t, inputSize>
{
public:
    Sink(FIFOBase<float32_t> &src):
    GenericSink<float32_t,inputSize>(src){
    };

    int run()
    {
        float32_t *b=this->getReadBuffer();
        for(int i=0;i<inputSize;i++)
        {
            output[i] = b[i];
        }
        return(0);
    };

    

};

template<typename OUT,int outputSize>
class Source;

template<int outputSize>
class Source<float32_t,outputSize>: GenericSource<float32_t,outputSize>
{
public:
    Source(FIFOBase<float32_t> &dst):
    GenericSource<float32_t,outputSize>(dst){};

    int run(){
        float32_t *b=this->getWriteBuffer();
        for(int i=0;i<outputSize;i++)
        {
            b[i] = input[i];
        }
        return(0);
    };


};

template<typename IN, int inputSize,typename OUT,int outputSize>
class ProcessingNode;

template<int inputSize>
class ProcessingNode<float32_t,inputSize,float32_t,inputSize>: 
public GenericNode<float32_t,inputSize,float32_t,inputSize>
{
public:
    ProcessingNode(FIFOBase<float32_t> &src,FIFOBase<float32_t> &dst):
    GenericNode<float32_t,inputSize,float32_t,inputSize>(src,dst){};

    int run(){
        float32_t *a=this->getReadBuffer();
        float32_t *b=this->getWriteBuffer();
        arm_offset_f32(a,0.5,b,inputSize);
       
        return(0);
    };

};
```

The `input` and `output` arrays, used in the sink / source, are defined as extern. The source is reading from `input` and the sink is writing to `output`.

The generated scheduler is (in C++ API mode):

```C++
uint32_t scheduler(int *error,EventQueue *evtQueue)
{
    int cgStaticError=0;
    uint32_t nbSchedule=0;
    int32_t debugCounter=1;

    CG_BEFORE_FIFO_INIT;
    /*
    Create FIFOs objects
    */
    FIFO<float32_t,FIFOSIZE0,1,0> fifo0(buf0);
    FIFO<float32_t,FIFOSIZE1,1,0> fifo1(buf1);

    CG_BEFORE_NODE_INIT;
    /* 
    Create node objects
    */
    ProcessingNode<float32_t,128,float32_t,128> proc(fifo0,fifo1);
    Sink<float32_t,128> sink(fifo1);
    Source<float32_t,128> source(fifo0);

    /* Run several schedule iterations */
    CG_BEFORE_SCHEDULE;
    while((cgStaticError==0) && (debugCounter > 0))
    {
        /* Run a schedule iteration */
        CG_BEFORE_ITERATION;
        for(unsigned long id=0 ; id < 3; id++)
        {
            CG_BEFORE_NODE_EXECUTION;

            switch(schedule[id])
            {
                case 0:
                {
                   cgStaticError = proc.run();
                }
                break;

                case 1:
                {
                   cgStaticError = sink.run();
                }
                break;

                case 2:
                {
                   cgStaticError = source.run();
                }
                break;

                default:
                break;
            }
            CG_AFTER_NODE_EXECUTION;
            CHECKERROR;
        }
       debugCounter--;
       CG_AFTER_ITERATION;
       nbSchedule++;
    }

errorHandling:
    CG_AFTER_SCHEDULE;
    *error=cgStaticError;
    return(nbSchedule);
}
```

If we look at the asm of the scheduler generated for a Cortex-M7 with `-Ofast` with armclang `AC6.19` and for **one** iteration of the schedule, we get (disassembly is from uVision IDE):

```txt
0x000004B0 B570      PUSH          {r4-r6,lr}
    97:             b[i] = input[i]; 
0x000004B2 F2402518  MOVW          r5,#0x218
0x000004B6 F2406118  MOVW          r1,#0x618
0x000004BA F2C20500  MOVT          r5,#0x2000
0x000004BE 4604      MOV           r4,r0
0x000004C0 F2C20100  MOVT          r1,#0x2000
0x000004C4 F44F7200  MOV           r2,#0x200
0x000004C8 4628      MOV           r0,r5
0x000004CA F00BF8E6  BL.W          0x0000B69A __aeabi_memcpy4
0x000004CE EEB60A00  VMOV.F32      s0,#0.5
   131:         arm_offset_f32(a,0.5,b,inputSize); 
0x000004D2 F2404618  MOVW          r6,#0x418
0x000004D6 F2C20600  MOVT          r6,#0x2000
0x000004DA 2280      MOVS          r2,#0x80
0x000004DC 4628      MOV           r0,r5
0x000004DE 4631      MOV           r1,r6
0x000004E0 F002FC5E  BL.W          0x00002DA0 arm_offset_f32
    63:             output[i] = b[i]; 
0x000004E4 F648705C  MOVW          r0,#0x8F5C
0x000004E8 F44F7200  MOV           r2,#0x200
0x000004EC F2C20000  MOVT          r0,#0x2000
0x000004F0 4631      MOV           r1,r6
0x000004F2 F00BF8D2  BL.W          0x0000B69A __aeabi_memcpy4
   163:        CG_AFTER_ITERATION; 
   164:        nbSchedule++; 
   165:     } 
   166:  
   167: errorHandling: 
   168:     CG_AFTER_SCHEDULE; 
   169:     *error=cgStaticError; 
   170:     return(nbSchedule); 
0x000004F6 F2402014  MOVW          r0,#0x214
0x000004FA F2C20000  MOVT          r0,#0x2000
0x000004FE 6801      LDR           r1,[r0,#0x00]
0x00000500 3101      ADDS          r1,r1,#0x01
0x00000502 6001      STR           r1,[r0,#0x00]
   171: } 
0x00000504 2001      MOVS          r0,#0x01
0x00000506 2100      MOVS          r1,#0x00
   169:     *error=cgStaticError; 
0x00000508 6021      STR           r1,[r4,#0x00]
0x0000050A BD70      POP           {r4-r6,pc}
```

It is the code you would get if you was manually writing a call to the corresponding CMSIS-DSP functions. All the C++ templates have disappeared. The switch / case used to implement the scheduler has also been removed.

The code was generated with `memoryOptimization` enabled and the Python script detected in this case that the FIFOs are used as arrays. As consequence, there is no FIFO update code. They are used as normal arrays.

The generated code is as efficient as something manually coded.

The sink and the sources have been replaced by a `memcpy`. The call to the CMSIS-DSP function is just loading the registers and branching to the CMSIS-DSP function.

It is not always as ideal as in this example. But it demonstrates that the use of C++ templates and a Python code generator is enabling a low overhead solution to the problem of streaming and compute graph.
