# Coding Guidelines

* Name: DioneCG/rfc:004/CodingGuidelines
* Editor: Matthias Gabriel
* Revision: 1.0.1
* State: stable

## Preamble

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## Goals

The _coding-guidelines_ are designed to ensure common practises when writing new code, ease maintenance of new code and ensure cross-platform compatibility. Further its meant to serve as a basic _best prectises_-guide to new users, that started developing C++.

This document is structured in two sub-sections: Requirements, which MUST be used and followed by users and Advices, which SHOULD be used.

## Requirements

### Major Platforms

Your code MUST compile on the following major platforms, herein called PLATFORMS, in the sense of **all**.

* Windows Intel x64, MSVC 14 \(Visual Studio 2015\)
* Linux Intel x64, GCC4.8+
* Linux ARM x64, GCC4.8+

If ones code cannot compile on some of the PLATFORMS due to design \(e.g. device drivers, which highly depend on the platform they are developed on\), it be MUST excluded from being compiled using CMake functionality \(e.g. an option to switch them on, on not supported PLATFORMS\). One SHOULD always try avoid platform specific code.

### Development Tools

* The programming language MUST be **C++11**
    * More modern C++ flavours \(C++14/17\) MAY be used, after ensuring that compilers on the PLATFORMS support it
* The build environment MUST be the **CMake** build system
* Payload datatypes MUST be protobuf classes

### Code Style

* All naming MUST use CamelCase and MUST be meaningful and expressive, for example:

```cpp
class IniFileReader; //a class, that can read ini files
void CalculateAngularDistance(/*..*/) // a method, that calculates an angular distance)
double averageMean // a variable that represents a calculated average mean value
```

* Code MUST be structured, long methods/functions SHOULD be avoided
    * Another person MUST be able to understand the content of a function immediately
    * Robert C. Martin \(Uncle Bob\): _"Methods should be small, smaller than small"_
* Public APIs SHOULD be documented \(e.g. using doxygen\)
* One MUST NOT use platform specific headers \(such as Windows.h\), if the code is used on other PLATFORMS. Otherwise the usage on other PLATFORMS MUST be prohibited
* One MUST NOT call virtual functions in constructor/destructor

### Filestructure

* Appropriate sub-folders in the Dione-tree MUST be used:
    * _Libraries_ for libraries
    * _Services_ for executables
    * _Data_ for data-containers and .proto files
* There SHOULD be one class per header file, except for:
    * auxilliary classes, whoes context does not exceed their parents scope \(e.g. are not used elsewhere, for example: configuration of services\)
    * nested-clases inside its parent
* Each header file MUST use a header guard technique. It SHOULD use `#pragma once` or MAY use traditional header guards\)

**Example for \#pragma once**

```cpp
#pragma once

class Example {};
```

**Example for Header Guards**

```cpp
#ifndef FILENAME_H
#define FILENAME_H

class Example {};

#endif //FILENAME_H
```

* _using namespace .._ MUST NOT be used in header files

## Development Guidelines

### General

* Code SHOULD NOT be duplicated, but re-used
    * If code from an existing Service is to be re-used, instead of copying files a library SHOULD be created and be used by both - the new and the old Service
* Code SHOULD be as near as possible to the consuming Service
    * If code is NOT being used by any other Service/Library, it SHOULD be included in the Service executable directly
* Direct member access SHOULD be avoided, setter/getter MAY be used instead
* Sensor data classes and manipulating/acquiring classes SHOULD be located in detached projects in order separate the ability to use the data from the need of hardware specific dependencies

### Naming

* Variables SHOULD be named in CamelCase starting with a small letter
* Member variables SHOULD be private and start with a small letter and with prefix "\_"
    * Any other prefixes SHOULD NOT be used
* Methods SHOULD start with a capital letter
* Example:

```cpp
class Example {
public:
  void ThisIsAMemberFunction() {
     int thisIsALocalVariable = 0;
  }
private:
   double _thisIsAPrivateDouble;
};
```

### C++ specific

* One SHOULD REALLY read Scott Meyers books \(SHOULD REALLY as in: _You SHOULD REALLY buy a present for your girlfriends birthday!_\)
    * Effective C++ \(C++98 concepts, of which most still hold for C++11\)
    * Effective Modern C++ \(C++11 and C++14\)
* Modern C++11 concepts SHOULD be used extensively
    * std::shared\_ptr, std::unique\_ptr, class enum
    * Lambdas, std::bind
    * Use byte-length specific integral data types: uint64\_t instead of unsigned int
* One SHOULD prefer built-in C++11 features over platform-specific solutions, for example:
    * Threads
    * Mutexes
    * Condition Variables
* Const-correctnes SHOULD be fulfilled, e.g. if a method doesn't modify a classes state, declare it const
    * [https://isocpp.org/wiki/faq/const-correctness](https://isocpp.org/wiki/faq/const-correctness)

```cpp
double ThisMethodDoesNotModify(double firstArgument) const;
```

* All complex function parameters SHOULD be passed by \(const-\)reference

```cpp
void MyStoreFunction(const MySuperComplexType& complexType, const std::string& fileName) const;
```

* All integral types SHOULD be passed by value

```cpp
double MyFancyDoubleAdder(double firstArgument, double secondArgument) const;
```

## History

### Version 1.0.1 \(stable\)

* fixed variable naming in examples and clarified naming conventions

### Version 1.0.0

* initial version
