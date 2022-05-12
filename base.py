import typer
import subprocess
from parser import parse
from optimizer import optimize
# from utils import *
import os
from pprint import pformat
from utils import print_break_line

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
            typer.echo("not done yet")
            return

    # time to optimize :)
    parsed = parse(compile_file.stdout.decode())
    optimized = optimize(parsed)
    if print_output:
        print('program length before optimization: ' + str(len(parsed)))
        print('program length after optimization: ' + str(len(optimized)))
        print_break_line()
        typer.echo(pformat(optimized))
    else:
        # output to file:
        pass


@app.command()
def compile_run():
    typer.echo("in development")


if __name__ == "__main__":
    app()

