# Proj 1

This is a python module for 605.202 Data Structures Lab 1. It converts 
expressions directly from prefix to postfix. For example, the string "-A+BC" 
is a prefix expression, and the program will directly convert it to "ABC+-" 
which is the equivalent postfix expression.

## Running Proj 1

1. Download and install Python 3.11 on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m proj1 -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m proj1 <some_input_file> <some_output_file>`

   IE: `python -m proj1 resources/input/RequiredInput.txt out.txt`

Output will be written to the specified output file after processing the input file.

### Proj 1 Usage:

```commandline
usage: python -m proj1 -h in_file out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  -h or --help  show this help message and exit
```

## Input
The first positional argument is the input file. The path to the input 
file should be relative to the top level proj1 directory. The input file 
should be a text file. If the input file does not exist, the program will 
error and print to the console.

### Input Handling
Each line of the input file represents a different expression. Blank lines 
are ignored, and spaces or tabs within or at the ends of a line are also 
ignored.

### Valid Inputs
Inputs should contain **alphabet letters** or **operators** (+, -, /, *, ^, 
or $). * represents multiplication. $ and ^ both represent exponentiation. 
The number of operators must equal the number of operands minus 1. The 
expression must be in a valid prefix form. Any character other than alphabet 
letters and these operators will result in an error for that line of the 
input file. 

## Output
The second positional argument is the output file. This file should be a 
text file. If the file does not exist, the program will create it.

### Output for Valid Inputs
* Inputted Prefix Expression
* Equivalent Postfix Expression
* Input size
* Run Time for that Input

### Output for Invalid Inputs
* Inputted Prefix Expression
* Error Explained
* Number of Operators
* Number of Operands

> **Note:** Errors are also printed to the console

## Python Packaging

### Python IDE 
I used PyCharm Community Edition for development of this porject

### Python Version
Python 3.11

### Python Packages

* `pathlib`
    * Used for creating paths from input and output arguments
* `argparse`
    * Used for parsing the command line arguments containing the 
      input and output text files
* `sys`
  * Used to handle errors and printing them to the console
* `proj1.modify_strings`
  * Developer created script that contains functions for string manipulation 
* `proj1.stack`
  * Developer created class of Stack to represent the stack data structure
* `proj1.get_count`
  * Developer created script that contains a function to get the number of operators and number of 
    operands of given string
* `typing`
  * Used to specifcy type hints of TextIO for 
    conversion function
* `time`
  * Used to calculate run time metrics for later analysis
* `proj1.runtime_metric`
  * Provided sample code for class of RuntimeMetric to contain size of an input and duration 
    of the solution

### Project Layout

* [proj1/](.): The parent or "root" folder containing all of these files.
    * [README.md](README.md):
      The guide you're reading.
    * [proj1](proj1): 
      This is a *module* in this *package*.
      * [`__init__.py`](proj1/__init__.py) 
        This is used to expose what functions, variables, classes, etc. are 
        exposed when scripts import this module.
      * [`__main__.py`](proj1/__main__.py) 
        This file is the entrypoint to this program when ran as a program. 
        It handles command line arguments.
      * `*.py` 
        These are python scripts that perform the actual logic of the program.





