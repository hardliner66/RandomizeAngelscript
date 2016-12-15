# RandomizeAngelscript
Randomize angelscript bytecodes

if you want to ship precompiled angelscript bytecode with your application, but harden it against decompilation, you can use this script to randomize the used bytecodes.

Usage:
1. copy randomize_bytecodes.py into angelscript include directory
2. run the script a few times
3. build angelscript
4. build your angelscript compiler
5. build your application
6. compile your angelscript scripts
7. package it

Tested with version AngelScript 2.31.1

As long as the corresponding enum/array doesn't get renamed, it should work with every version of angelscript
