# A86 Assembly Optimizer

### Setup

#### Requirements (requirements.txt)

You can install all the packages required to run my project with `pip3 install -r requirements.txt`

Used for this project:
- [typer](https://github.com/tiangolo/typer)
- [pyparsing](https://github.com/pyparsing/pyparsing)

### How to use:

#### 1. Compile a file:

```
python3 base.py compile example.rkt
```

This will compile the file at the given path to an executable

To compile without optimization: 
```
python3 base.py compile example.rkt --no-optimization
```

To compile with optimization and print output to console (without saving to file):
```
python3 base.py compile example.rkt --print
```

#### 2. Compile all .rkt files in a folder and output optimized and unoptimized assembly in subfolder


#### 3. Compile and run a file:

```
python3 base.py compile-run example.rkt
```
