import typer

app = typer.Typer()

@app.command()
def hi():
    name = typer.prompt("What is your name?")
    typer.secho(f"Hi, {name}!",
            fg=typer.colors.GREEN)

if __name__ == "__main__":
    app()
