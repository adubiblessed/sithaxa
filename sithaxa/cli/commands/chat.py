import typer 

app = typer.Typer(help="Sithaxa - AI-powered chat commands")

@app.command()
def chat(message: str):
    """Send a message to the chat."""
    typer.echo(f"Chat message sent: {message}")
