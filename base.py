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
    if optimization:
        typer.echo(f"Compiling {file_path} with optimization")
        typer.echo("==========================================")
    else:
        typer.echo(f"Compiling {file_path} without optimization")
        typer.echo("==============================================")

    compile_file = subprocess.run(
        ['racket', '-t', 'iniquity/compile-file.rkt', '-m', file_path],
        stdout=subprocess.PIPE
    )

    if print_output and not optimization:
        print(compile_file.stdout.decode())


@app.command()
def compile_run():
    typer.echo("in development")


if __name__ == "__main__":
    app()
