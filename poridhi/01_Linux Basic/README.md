# Linux Basic


## Table of Contents
- [x] Namespace


### Namespace
In Linux, a namespace is a feature that allows processes to use the system resources they need but separately from other processes. A namespace is a way to virtualize a global system resource such that a process that needs it operates in an isolated instance of that resource.

Additionally, a group of resources and processes can refer to the same namespace, but each namespace has individual resources for each. Only processes in the same namespace can identify the changes made in a global resource.


### Reference
- [Namespace](https://man7.org/linux/man-pages/man7/namespaces.7.html), [list-namespaces](https://www.baeldung.com/linux/list-namespaces)