from typer import Typer, echo

app = Typer(help="Generate code structure and folder using AI")

@app.command()
def generate(structure: str):
    """Generate code structure based on the provided description."""
    echo(f"Generating code structure for: {structure}")