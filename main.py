import typer
import json
from pathlib import Path
app = typer.Typer()

@app.command()
def hi():
    """This command will say hi to user and save thier names."""
    names = Path("names.json")
    name = typer.prompt("What is your name?")
    typer.secho(f"Hi, {name}!",
            fg=typer.colors.GREEN)
    if names.is_file():
        with open(names,"r") as names_f:
            data = json.load(names_f)
        data["names"].append(name)
        with open(names,"w") as names_f:
            json.dump(data,names_f, indent=4)
    else:
        data = {
                "names":[name]
                }
        with open(names,"w") as names_f:
            json.dump(data,names_f,indent=4)

@app.command()
def bye():
    """This command will say goodbye to all users"""
    check_name = Path("names.json")
    if check_name.is_file():
        with open(check_name, "r") as names_f:
            data = json.load(names_f)
        for name in data["names"]:
            typer.secho(f"Goodbye {name} see you later.",
                    fg=typer.colors.YELLOW)
        check_name.unlink()
    else:
        typer.secho("Goodbye buddy see you later.",
                fg=typer.colors.YELLOW)


if __name__ == "__main__":
    app()
