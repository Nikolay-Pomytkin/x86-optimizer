import typer
import subprocess

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
    # print intro message
    if optimization:
        typer.echo(f"Compiling {file_path} with optimization")
        typer.echo("==========================================\n"*2)
    else:
        typer.echo(f"Compiling {file_path} without optimization")
        typer.echo("=============================================\n"*2)

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

    ## time to optimize :) 


@app.command()
def compile_run():
    typer.echo("in development")


if __name__ == "__main__":
    app()
