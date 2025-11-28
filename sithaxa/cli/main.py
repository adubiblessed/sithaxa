import typer


from sithaxa.cli.commands import commit, debug, explain, generate, learn, readme, recall

app = typer.Typer(help="Sithaxa - AI-powered local CLI coding assistant")
app.add_typer(commit.app)
app.add_typer(debug.app)
app.add_typer(explain.app)
app.add_typer(generate.app)
app.add_typer(learn.app)
app.add_typer(readme.app)
app.add_typer(recall.app)

def main():
    app()


if __name__ == "__main__":
    app()



