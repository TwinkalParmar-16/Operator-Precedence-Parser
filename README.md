#About Operator-precedence parser
An operator precedence parser is a bottom-up parser that interprets an operator-precedence grammar.
A grammar is said to be operator precedence grammar if it has two properties:
? No R.H.S. of any production has a ?.
? No two non-terminals are adjacent.
Operator precedence can only established between the terminals of the grammar. It ignores the
non-terminal.

##About the Project
Language used:Python
The parser will take three input files,viz-a-viz ,input.txt,grammar.txt,precedence.txt.
? precedence.txt
This file will contain the precedence and associativity for the available operators.The precedence
and associativity will be given as per our requirement.
? grammar.txt
This file will contain the grammar rules i.e the production rules for our language.
? input.txt
This file will contain the input string.The parser will determine whether this input is follows the
grammar rule.If accepted,ACCEPT message will be shown else ERROR will be flagged.

##Output of Parser
The operator -precedence table will be displayed.If the input string is accepted by the parser,ACCEPT
message will be displayed,if not ERROR will be shown.