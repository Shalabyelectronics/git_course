import typer

app = typer.Typer()

@app.command()
def hi():
    """This command is for greeting users"""
    name = typer.prompt("What is your name?")
    typer.secho(f"Hi, {name}!",
            fg=typer.colors.GREEN)

if __name__ == "__main__":
    app()
