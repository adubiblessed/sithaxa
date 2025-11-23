import typer


from sithaxa.cli.commands import hello, commit, debug, explain, generate, learn, readme, recall

app = typer.Typer(help="Sithaxa - AI-powered local CLI coding assistant")
app.add_typer(hello.app, name="hello")
app.add_typer(commit.app, name="commit")
app.add_typer(debug.app, name="debug")
app.add_typer(explain.app)
app.add_typer(generate.app, name="generate")
app.add_typer(learn.app, name="learn")
app.add_typer(readme.app, name="readme")
app.add_typer(recall.app, name="recall")

def main():
    app()


if __name__ == "__main__":
    app()



