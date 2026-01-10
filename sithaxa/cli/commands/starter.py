"""
    This is the starting point for the Sithaxa CLI application.
    
    It controls the first operation of the appliction when user installs and register for the first time
"""

import typer

app = typer.Typer(help="Start point for installation and configuration of Sithaxa CLI")

@app.command()
def start():
    typer.echo("Welcome to Sithaxa CLI!")
    typer.echo("Please follow the instructions to complete the setup.")
    typer.echo("1. Register your account")
    typer.echo("2. Configure your settings")
    typer.echo("3. Start using Sithaxa CLI")
    typer.echo("4. Enjoy your experience with Sithaxa CLI!")
    model = typer.prompt("what model do you want")