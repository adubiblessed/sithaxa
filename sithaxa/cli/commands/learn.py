import typer

app = typer.Typer(help="Learn new coding concepts using AI")

@app.command()
def learn(topic: str):
    """Learn about a specific coding topic."""
    typer.echo(f"Learning about: {topic}")
    
