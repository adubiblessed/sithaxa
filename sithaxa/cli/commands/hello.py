import typer

app = typer.Typer(help="Say hello to Sithaxa!")

@app.command()
def greet(name: str):
    """Greets a user by name."""
    typer.echo(f"👋 Hello, {name}! Welcome to Sithaxa.")
