CONVENTION
| Input | Reserved cell | Null | Other cells
Everything started from the null section

Print input reversely
<[.>-<<] 

n time print last cell
<<[<]
>[.>]
+++++ // n minus 1 value
[-<.>]


Caesar n shift
>+
[
	>,
	+ n times
	.
	- n times
]



POSITION HAVE TO BE RESETTED ON NULL CELL AFTER LAST CELL OF INPUT

Capitalize first letter (POSITION CELL #0)
++++[->++++++++<]>	// Store 32 in cell #0
[>,]<[<]>			// Read input
[>-<-] 				// Subtract first letter on input with value of cell #0
>[>]				// Go to last cell to reset position

To print
<[<]>[.>]			// Go back and loop print

Normalize first letter
<[<]<				// Go front
++++[->++++++++<]> 	// Store 32
[>+<-]				// Add first letter on input with value of cell #0
>[>]				// Go to last cell to reset position

>[[->]<[<]>-]

Capitalize all letters (Cheat version)

<[<]>
[-------------------------------->]

Print capitalized letters but keeping input lowercase (Cheat version)

<[<]>
[--------------------------------.++++++++++++++++++++++++++++++++>]

Normalize all letters (Cheat version)
<[<]>
[++++++++++++++++++++++++++++++++.>]

Find nearest non zero and reset the value (https://codegolf.stackexchange.com/a/54435)

+[-[[->>+<<]>>+<<->]<+]->>[-<<+>>]<<[-]