import typer

app = typer.Typer(help="Debug commands for Sithaxa")
@app.command()
def debug(message: str):
    """Outputs a debug message."""
    typer.echo(f"Debugging message: {message}")
