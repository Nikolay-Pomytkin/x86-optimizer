import typer
import subprocess
from parser import parse
# from utils import *
import os


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
            "out" if optimization else ""
        )
    )
    typer.echo("==========================================\n\n")

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
    optimized = parse(compile_file.stdout.decode())
    if print_output:
        typer.echo(optimized)
    else:
        # output to file:
        pass


@app.command()
def compile_run():
    typer.echo("in development")


if __name__ == "__main__":
    app()
