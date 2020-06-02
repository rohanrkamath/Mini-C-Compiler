# Mini C++ Compiler
A mini C++ compiler that handles While and For constructs.

#INDRODUCTION

Built  a mini-compiler for the C++ programming language. C++ programming is a general-purpose, object oriented language. I have used Lex and Yacc for the implementation of this mini-compiler. 
As we all know, there are 5 distinct phases in compiler designing, namely -
•	Lexical Analysis
•	Syntax Analysis
•	Semantic Analysis
•	Intermediate Code Generation
•	Target Code Generation
The reason why we have to go through this phases is that a high level language like C++ isnt understood by the machine. Here is a brief about the stages -
1.	Lexical Analysis Phase -  In this phase, we will be generating different types of tokens from the code we have written.
2.	Syntax Analysis Phase - In this phase with the written grammar rules we will be checking the syntax of the C++ program we have written. 
3.	Semantic Analysis Phase - In this phase we will do semantic checks of the code and we will also build Abstract Syntax Tree. 
4.	ICG - In this phase, we will be generating (3AC) address codes which are intermediate codes. 
5.	TCG - In this phase, we will generate assembly code (MIPS Architecture), also known as the target code. This, finally is the code understood by the machine. 
I will be focusing on building these 2 constructs - 
•	While looping Statement.
•	For looping Statement. 
Keeping these constructs in mind, I have -
• Built a symbol table
• Done error handling
• Generated an abstract syntax tree
• Converted the C++ program into ICG 
• Converted the ICG to TCG

I have implemented three types of code optimisation - 
• Constant Folding - Checks RHS for numericals, and solves them.
• Constant Propogation - Substitute values of known constants in exressions.
• Dead Code Elimination - Eliminate unnecessary redundant code.
