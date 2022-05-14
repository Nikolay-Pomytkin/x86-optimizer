# A86 Assembly Optimizer
### CMSC430 Final Project
### By: Nikolay Pomytkin

## Table of Contents



### Setup

#### Requirements (requirements.txt)

You can install all the packages required to run my project with `pip3 install -r requirements.txt`

Used for this project:
- [typer](https://github.com/tiangolo/typer)
- [pyparsing](https://github.com/pyparsing/pyparsing)

### How to use:

##### 1. Compile a single file (with or without optimization):

To compile with optimization and print output to console (without saving to file):
```
python3 base.py compile examples/example.rkt --print-output
```

To compile without optimization and print output: 
```
python3 base.py compile example.rkt --no-optimization --print-output
```

To compile with optimization and save to sub-folder with .s and executable file: 
```
python3 base.py compile example.rkt
```

To compile without optimization and save to sub-folder with .s and executable file: 
```
python3 base.py compile example.rkt --no-optimization
```



##### 2. Compile all .rkt files in a folder

To compile all files in given folder and print both optimized and original assembly (in that order):
```
python3 base.py compile-folder examples --print-output
``` 

To compile all files in given folder and output both optimized and original assembly and executable files

##### 3. Compile and run a file:

With optimization:
```
python3 base.py compile-run examples/example.rkt
```

Without optimization:
```
python3 base.py compile-run examples/example.rkt --no-optimization
```




## Write-up

You can see my optimizer source code is split up into a few files:

- `base.py`
    - This file holds the main logic for the actual CLI
    - all the commands shown above are implemented in this file
- `parser.py`
    - This file contains a parsing grammer (setup using pyparser)
    - and a function that takes in a program and parses it
- `optimizer.py`
    - This file contains all of the logic that takes care of optimizing assembly programs that are fed into it
    - Assembly programs fed into it are in the format of a "list of lists", where the inner lists represent individual lines of assembly split up into smaller tokens
    - You can see my looping logic where I loop over the assembly line by line, looking for instructions that can be the initial instruction in a pattern that can be optimized
- `utils.py`
    - This file contains some utility functions I use to support the CLI
    - `print_break_line()` is used a lot in the CLI just for printing a breaking line of "=" in the output
    - `program_to_string()` is used to take a program returned by the optimizer and convert it back into the expected format for a .s assembly file
    - `save_program_to_file()` takes a program and saves it to a filepath

###### Optimizer explanation:

My optimizer completes 4 main optimizations (in this order):
1. Static Pushes:

This optimization checks if something gets pushed but then immediately popped back off the stack. 
In cases like these, we can just make this a move between registers

```
push r1
mov r2, [rsp + 0]
add rsp, 8
```

gets optimized to:

```
mov r2, r1
```

2. Static references:

We sometimes have assembly code that pushes something and the next instruction references it and puts it back in a register
For example:
```
push r1
mov r2, [rsp + 0]
```

gets optimized to:
```
push r1
mov r2, r1
```

Although this does not reduce the number of instructions, stack references are slower than moving between registers, so this speeds up our program.

3. Minimizing multiple add instructions to the rsp pointer (when working with the stack)

Sometimes, an inefficient assembly program pushes many things to the stack and this results in code later that moves the rsp pointer multiple times
with multiple add instructions. We can reduce these multiple add instructions in a row to a single add instruction.

```
add rsp, 8
add rsp, 8
add rsp, 8
```

gets optimized to:

```
add rsp, 24
```


#### Outtakes:
In hindsight, not 100% sure writing this in python was the best idea, but it was a lot of fun. Getting the main "infrastructure" setup was the biggest challenge.
I think the way I set up my code would allow me to pretty easily add more optimizations if I had more time (and more insight on what kind of better optimizations I could make),
but I learned a ton from this project nonetheless!
