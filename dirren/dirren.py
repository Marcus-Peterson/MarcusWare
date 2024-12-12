import typer
import os
import pathlib

app = typer.Typer()

@app.command()
def generate(
    inputs: list[str] = typer.Argument(..., help="List of input strings in 'files --> folder' format.")
):
    """
    Create multiple files in multiple directories using the `-->` syntax.
    Example:
    python dirren.py "file1.txt file2.txt --> my_folder" "code.py something.py --> src_folder" "file_3.txt --> text_folder"
    """
    for input_str in inputs:
        # Split each input string into parts based on '-->'
        parts = input_str.split("-->")
        if len(parts) != 2:
            typer.echo(f"Error: Invalid format for input '{input_str}'. Ensure it follows 'files --> folder' syntax.")
            raise typer.Exit()

        # Extract files and folder
        files = parts[0].strip().split()
        folder = parts[1].strip()

        # Validate input
        if not files:
            typer.echo(f"Error: No files specified for folder '{folder}'.")
            raise typer.Exit()

        # Create the directory
        os.makedirs(folder, exist_ok=True)
        directory = pathlib.Path(folder)
        typer.echo(f"Created/Verified folder: {folder}")


        # Create files in the directory
        for file in files:
            file_path = directory / file
            if not file_path.exists():
                with open(file_path, "w") as f:
                    f.write("")  # Create an empty file
                typer.echo(f"Created file: {file_path}")
            else:
                typer.echo(f"File already exists: {file_path}")

if __name__ == "__main__":
    app()

