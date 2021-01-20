010 100 10 011 010 01 01101110 01010010 01101001 01101110 
untuk huruf kecil 011xxxxx
untuk huruf besar 010xxxxx

BRAINFUCK MEMORY MANAGEMENT
| 1st looper | 2nd looper | canvas | non standard | input reversed | 0 |
| 2 bit null input | input | 1st looper | 2nd looper | canvas |
| input | null | 8 | 16 | 24 | dst |  


first make the environment
++++++++				0 0
[
	>++++++++++++		0 1
	[
		>>+ i			1 3
		>+ n			3 4
		>>+ i			4 6
		>+ n			6 7
		<<<<<<-			7 1
	]

	++++++++			1 1
	[
		>+ R			1 2		
		>>>+ R			2 5
		<<<<-			5 1
	]
	[<]<- end of loop for main loop (cell #0) 
]

# now for space


++++					0 0
[
	>++++				0 1
	[
		>++++			1 2
		>++				2 3
		>+++			3 4
		>++++			4 5
		>++				5 6
		>+++			6 7
		<<<<<<-			7 1
	]
]

>++.
>+.
>++.
>++.
>+.
>++.