import typer
from sithaxa.core.ai_connector import client
from sithaxa.utils.file_ops import FileOperations
from sithaxa.core.promts_templates.prompts import DEBUG_CODE_PROMPT

app = typer.Typer(help="Help Debug code snippets using AI")

@app.command()
def debug(
    code: str = typer.Option(None, "--code", "-c", help="Code snippet to Debug"),
    file: str = typer.Option(None, "--file", "-f", help="Path to a file containing the code snippet")
):
    
    if file:
        file_ops = FileOperations(file_path=file)
        code_content = file_ops.read_file()
        if code_content is None:
            typer.echo("Failed to read the file. Please check the file path and try again.")
            raise typer.Exit(code=1)
        code = code_content
    
    typer.echo(f"Explaining code snippet: {code}")

    # Create prompt
    prompt = DEBUG_CODE_PROMPT.format(code_snippet=code)

    response = client.chat.completions.create(
        model="x-ai/grok-4.1-fast",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        extra_body={"reasoning": {"enabled": False}}
    )

    typer.echo("\n" + "="*50)
    typer.echo("EXPLANATION")
    typer.echo("="*50 + "\n")
    typer.echo(response.choices[0].message.content)
    typer.echo("="*50 + "\n")


if __name__ == "__main__":
    app()