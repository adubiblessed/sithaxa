import typer 

app = typer.Typer(help="Generate README files using AI")
@app.command()
def readme(project_description: str):
    """Generate a README file based on the provided project description."""
    typer.echo(f"Generating README for project: {project_description}")

