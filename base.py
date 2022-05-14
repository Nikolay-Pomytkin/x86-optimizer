import typer
import subprocess
from parser import parse
from optimizer import optimize
# from utils import *
import os
from utils import (
    print_break_line,
    program_to_string,
    save_program
)
from os import listdir
from os.path import isfile, join

app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def compile(
    file_path: str,
    optimization: bool = True,
    print_output: bool = False
):
    # check if input file exists
    if not os.path.exists(file_path):
        typer.echo(
            f"Failed to locate file at path: {file_path}",
            err=True,
        )
        return
    # print intro message
    typer.echo(
        "Compiling {} with{} optimization".format(
            file_path,
            "" if optimization else "out"
        )
    )
    print_break_line()

    # run inputted file through inquity compiler
    compile_file = subprocess.run(
        ['racket', '-t', 'iniquity/compile-file.rkt', '-m', file_path],
        stdout=subprocess.PIPE
    )

    # handle no optimization (just regular printing)
    if not optimization:
        if print_output:
            typer.echo(compile_file.stdout.decode())
            return
        else:
            save_program(file_path, compile_file.stdout.decode())
            return

    # time to optimize :)
    parsed = parse(compile_file.stdout.decode())
    optimized = optimize(parsed)
    output = program_to_string(optimized['program'])
    print('program length before optimization: ' + str(len(parsed)))
    optimized_len = str(len(optimized['program']))
    print('program length after optimization: ' + optimized_len)
    if print_output:
        print_break_line()
        typer.echo(output + "\n")
    else:
        # OUTPUT TO FILE:
        save_program(file_path, output, optimized=True)


@app.command()
def compile_folder(folder_path: str, print_output: bool = False):
    files = [
        join(folder_path, f)
        for f in listdir(folder_path) if isfile(join(folder_path, f))
    ]
    print(files)
    for f in files:
        compile(f, optimization=True, print_output=print_output)
        compile(f, optimization=False, print_output=print_output)


@app.command()
def compile_run(file_path: str, optimization: bool = True):
    # check if input file exists
    if not os.path.exists(file_path):
        typer.echo(
            f"Failed to locate file at path: {file_path}",
            err=True,
        )
        return
    filepath_split = file_path.split('/')
    filename = filepath_split[-1]
    file_no_ext = filename.split('.')[0]
    print("filename: "+ filename)
    print('no extension: '+ file_no_ext)
    if not optimization:
        subprocess.run(
            ['cp', file_path, 'iniquity/'+filename],
        )
        # result = subprocess.run(
        #     ['cd', 'iniquity', '&&', 'make', file_no_ext+'.run']
        # )
        os.system('cd iniquity && make {}.run'.format(file_no_ext))
        print_break_line()
        os.system('./iniquity/'+file_no_ext+'.run')
    else:
        command0 = 'cd iniquity && make clean'
        os.system(command0)
        # run inputted file through inquity compiler
        compile_file = subprocess.run(
            ['racket', '-t', 'iniquity/compile-file.rkt', '-m', file_path],
            stdout=subprocess.PIPE
        )
        parsed = parse(compile_file.stdout.decode())
        optimized = optimize(parsed)
        output = program_to_string(optimized['program'])
        # print("OUTPUT:")
        # print(output)

        # file = open("iniquity/{}.s".format(file_no_ext), "w")
        # file.write(output)
        save_program(f'iniquity/{file_no_ext}.rkt', output)
        os.system('cd iniquity && gcc -fPIC -c -g -o main.o main.c')
        os.system('cd iniquity && gcc -fPIC -c -g -o values.o values.c')
        os.system('cd iniquity && gcc -fPIC -c -g -o print.o print.c')
        os.system('cd iniquity && gcc -fPIC -c -g -o io.o io.c')
        os.system('cd iniquity && ld -r main.o values.o print.o io.o -o runtime.o')
        command1 = f'cd iniquity && nasm -g -f macho64 -o {file_no_ext}.o {file_no_ext}.s'
        command2 = f'cd iniquity && gcc runtime.o {file_no_ext}.o -o {file_no_ext}.run'
        command3 = f'./iniquity/{file_no_ext}.run'
        print(command1)
        os.system(command1)
        print(command2)
        os.system(command2)
        print(command3)
        print_break_line()
        os.system(command3)
        # os.system('cd iniquity && rm {}.o {}.s'.format(file_no_ext, file_no_ext))


if __name__ == "__main__":
    app()
