INSTALLATION:

	git clone https://github.com/cipo865/sudoku.git

REQUIREMENTS:

    Python 3

INSTRUCTIONS:

    You must specify an input file using the -i or --input flag.

    To enable the AC3 constraint propagation algorithm, use the -a or --ac3 flag.

    To enable MRV and LCV heuristics, use the -H or --heuristics flag.
    
    You can specify a delay (in seconds) between printed steps using the -d or --delay flag.

    By default, the program uses only forward checking to solve Sudokus with no delay.

HOW TO CREATE A NEW SUDOKU:

    Create a new file in the data directory.

    Represent empty cells with 0.

    The file must contain 81 numbers in total:

        9 numbers per line, separated by spaces.

        9 lines in total.

    Comments:

        Single-line comments start with #.

        Empty lines are allowed.

    Validation:

       	If the file does not have exactly 9 rows and 9 columns, or contains invalid characters, an exception will be thrown.

EXAMPLE:

    # This is a comment
    0 2 6 0 0 1 0 0 0
    3 0 0 0 0 9 2 5 7 
    4 9 5 0 0 0 0 1 0 
    0 4 0 0 5 3 1 0 0
    0 6 3 2 1 0 7 4 0
    0 0 1 0 9 0 0 3 0
    0 8 9 0 7 0 0 0 1
    6 0 0 0 8 0 4 2 9
    0 0 0 9 6 0 3 0 8


