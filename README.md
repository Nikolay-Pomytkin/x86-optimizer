# A86 Assembly Optimizer

### Setup

#### Requirements (requirements.txt)

You can install all the packages required to run my project with `pip3 install -r requirements.txt`

Used for this project:
- [typer](github.com/tiangolo/typer)

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

#### 2. Compile and run a file:

```
python3 base.py compile-run example.rkt
```


#### 3. Compile and run both original and optimized code 