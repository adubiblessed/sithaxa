import typer

app = typer.Typer(help="Help recall previous coding sessions using AI")

@app.command()
def recall(session_id: str):
    """Recall a previous coding session."""
    typer.echo(f"Recalling session: {session_id}")
