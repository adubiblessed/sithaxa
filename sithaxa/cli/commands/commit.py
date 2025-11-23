import typer

app = typer.Typer(help="Commit changes with AI assistance")
@app.command()
def commit(message: str):
    """Commits changes to the repository with the provided message."""
    typer.echo(f"Committing changes with message: {message}")
