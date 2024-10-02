---
layout: post
title: "Obfuscar: Question on Local Variables"
description: A post about how Obfuscar works on C# local variables
tags: .NET
excerpt_separator: <!--more-->
---
It is not a surprise that many people would like to try out Obfuscar, one of the most popular .NET obfuscation tools, and they have various questions on the obfuscation results. Thus, I might post from time to time on what you should expect from such a tool, and help you better understand C#, .NET, as well as Obfuscar.

Today, let's start with [a recent issue](https://github.com/obfuscar/obfuscar/issues/404) on GitHub regarding local variables in C# methods.
<!--more-->

## The Sample Code
So, we will use the simplest C# sample below as our test case,

``` csharp
using System;
using System.Security.Cryptography.X509Certificates;

namespace C_
{
    class Program
    {
        static void Main(string[] args) 
        {
            var test = Int32.MinValue;
            Console.WriteLine(test);

            var test2 = new X509Certificate2();
            Console.WriteLine(test2);
        }
    }
}
```

If you use `dotnet new console` to create a test project and replace the content of `Program.cs` with the snippet above, you can then easily compile everything to an assembly, such as `bin/Debug/net7.0/testconsole.dll`.

If variable names are kept after compilation, we should be able to see them in MSIL format.

## Disassembling MSIL
You might want to find a disassembler somewhere, and I just published a new global tool for .NET SDK here,
``` bash
$ dotnet tool install --global dotnet-ildasm2
```

With this tool installed, you can easily run the following command to disassemble the Main method from the assembly,

``` text
ildasm testconsole.dll -i Program::Main


.class private auto ansi beforefieldinit C_.Program extends [System.Runtime]System.Object
{

  .method private hidebysig static default void Main(string[] args) cil managed
  {
    // Method begins at Relative Virtual Address (RVA) 0x2050
    .entrypoint
    // Code size 28 (0x1C)
    .maxstack 1
    .locals init(int32 V_0, class [System.Security.Cryptography.X509Certificates]System.Security.Cryptography.X509Certificates.X509Certificate2 V_1)
    IL_0000: nop
    IL_0001: ldc.i4 -2147483648
    IL_0006: stloc.0
    IL_0007: ldloc.0
    IL_0008: call void class [System.Console]System.Console::WriteLine(int32)
    IL_000d: nop
    IL_000e: newobj instance void class [System.Security.Cryptography.X509Certificates]System.Security.Cryptography.X509Certificates.X509Certificate2::.ctor()
    IL_0013: stloc.1
    IL_0014: ldloc.1
    IL_0015: call void class [System.Console]System.Console::WriteLine([System.Runtime]System.Object)
    IL_001a: nop
    IL_001b: ret
  } // End of method System.Void C_.Program::Main(System.String[])
} // End of class C_.Program
```
As you can see, the original variable names `test` and `test2` are nowhere to find. As we are currently working on a debug build assembly, we can see that C# compiler left hints for local variables in `.locals`. But even there names like `V_0` and `V_1` are not related to the original variable names.

If we disassemble the corresponding release build, we will see

``` text
.class private auto ansi beforefieldinit C_.Program extends [System.Runtime]System.Object
{

  .method private hidebysig static default void Main(string[] args) cil managed
  {
    // Method begins at Relative Virtual Address (RVA) 0x2050
    .entrypoint
    // Code size 21 (0x15)
    .maxstack 8
    IL_0000: ldc.i4 -2147483648
    IL_0005: call void class [System.Console]System.Console::WriteLine(int32)
    IL_000a: newobj instance void class [System.Security.Cryptography.X509Certificates]System.Security.Cryptography.X509Certificates.X509Certificate2::.ctor()
    IL_000f: call void class [System.Console]System.Console::WriteLine([System.Runtime]System.Object)
    IL_0014: ret
  } // End of method System.Void C_.Program::Main(System.String[])
} // End of class C_.Program
```

which does not even have `.locals` any more.

## Conclusion
Thus, now you know that local variable names are lost during C# compilation, so that any obfuscation tool needn't to perform anything else on them.

Stay tuned for more.
