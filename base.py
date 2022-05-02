import typer


app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def compile(file_path: str, optimization: bool = True, print: bool = False):
    if optimization:
        typer.echo(f"Compiling {file_path} with optimization")
    else:
        typer.echo(f"Compiling {file_path} without optimization")


if __name__ == "__main__":
    app()
