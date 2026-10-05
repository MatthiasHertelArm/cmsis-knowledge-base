---
id: "svd-device-peripherals-peripheral-regi-device-pripherals-peripheral-registers-c"
type: "concept"
domain: "pack"
title: "/device/peripherals/peripheral/registers element: /device/pripherals/peripheral/registers/.../cluster element"
summary: "Multiple \\tagem{register} and \\tagem{cluster} sections may occur in any order. Since version 1.3 of the specification, the nesting of \\tagem{cluster} elements is supported. Nested clusters express hierarchical structures of registers."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"
license: "Apache-2.0"
mode: "V"
---

**Cluster** describes a sequence of neighboring registers within a peripheral. A \tagem{cluster} specifies
the _addressOffset_ relative to the _baseAddress_ of the grouping element. All \tagem{register}
elements within a \tagem{cluster} specify their _addressOffset_ relative to the cluster base address
(\tagem{peripheral.baseAddress} + \tagem{cluster.addressOffset}).

Multiple \tagem{register} and \tagem{cluster} sections may occur in any order.
Since version 1.3 of the specification, the nesting of \tagem{cluster} elements is supported.
Nested clusters express hierarchical structures of registers. It is predominantely targeted
at the generation of device header files to create a C-data structure within the
peripheral structure instead of a flat list of registers.
Note, you can also specify an array of a cluster using the \tagem{dim} element.


**/device/pripherals/peripheral/registers/.../cluster**


  | 
    Parent Element | 
    Element Chain | 
  

  | 
    registers | 
    elem_registers | 
  

  | 
    cluster | 
    elem_cluster | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    derivedFrom | 

    Specify the cluster name from which to inherit data.
        Elements specified subsequently override inherited values.
        
**Usage:**
        - Always use the full qualifying path, which must start with the peripheral \tagem{name}, when deriving from another scope.
          (for example, in periperhal `B`, derive from `peripheralA.clusterX`).
        - You can use the cluster \tagem{name} when both clusters are in the same scope.
        - No relative paths will work.
        
**Remarks:** When deriving a cluster, it is mandatory to specify at least
        the \tagem{name}, the \tagem{description}, and the \tagem{addressOffset}. | 
    referenceIdentifierType | 
    0..1 | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
      | 
    Refer to dimElementGroup_gr for details. | 
  

  | 
    dim | 
    Define the number of elements in an array of clusters.  | 
    scaledNonNegativeInteger  | 
    1..1  | 
  

  | 
    dimIncrement | 
    Specify the address increment, in `Bytes`, between two neighboring clusters of the cluster array. | 
    scaledNonNegativeInteger  | 
    1..1  | 
  

  | 
    dimIndex | 
    Specify the strings that substitute the placeholder _[%%s]_ within the cluster \tagem{name}.
        Use the placeholder _%%s_ in \tagem{name} when \tagem{dimIndex} is specified. | 
    dimIndexType  | 
    0..1  | 
  

  | 
    dimName | 
    Specify the name of the C-type structure.  If not defined, then the entry of the \tagem{name} element is used. | 
    identifierType | 
    0..1  | 
  

  | 
    `<dimArrayIndex>` | 
    Grouping element to create enumerations in the header file. | 
    dimArrayIndexType | 
    0..1  | 
  

  | 
    name | 
    String to identify the cluster. Cluster names are required to be unique
        within the scope of a peripheral. A list of cluster names can be build using the placeholder _%%s_.
        Use the placeholder _[%%s]_ at the end of the identifier to generate arrays in the header file.
        The placeholder _[%%s]_ cannot be used together with \tagem{dimIndex}. | 
    dimableIdentifierType  | 
    1..1  | 
  

  | 
    description | 
    String describing the details of the register cluster. | 
    xs:string  | 
    0..1  | 
  

  | 
    alternateCluster  | 
    Specify the name of the original cluster if this cluster provides an alternative description. | 
    dimableIdentifierType | 
    0..1  | 
  

  | 
    headerStructName | 
    Specify the struct type name created in the device header file. If not specified, then the name of the cluster is used. | 
    identifierType | 
    0..1  | 
  

  | 
    addressOffset | 
    Cluster address relative to the \tagem{baseAddress} of the peripheral. | 
    scaledNonNegativeInteger | 
    1..1  | 
  

  | 
      | 
    Refer to registerPropertiesGroup_gr for details. | 
  

  | 
    size | 
    Define the default bit-width of any device register (implicit inheritance). | 
    scaledNonNegativeInteger  | 
    0..1  | 
  

  | 
    access | 
    Define access rights. | 
    accessType | 
    0..1  | 
  

  | 
    protection | 
    Specify the security privilege to access an address region. | 
    protectionStringType | 
    0..1  | 
  

  | 
    resetValue  | 
    Define the default value for all registers at RESET. | 
    scaledNonNegativeInteger  | 
    0..1  | 
  

  | 
    resetMask | 
    Identify register bits that have a defined reset value. | 
    scaledNonNegativeInteger | 
    0..1  | 
  

  | 
    `<register>` | 
    Define a sequence of register within a cluster. | 
    registerType | 
    0..*  | 
  

  | 
    `<cluster>` | 
    Element to nest cluster definitions. | 
    clusterType | 
    0..*  | 
  




\delim_sec
