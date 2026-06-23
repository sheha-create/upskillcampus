# File Organizer

A small Python command-line tool that organizes files in a target directory into category folders based on file extension.

## Usage

Preview moves without changing files:

```bash
python app.py "C:\path\to\folder" --dry-run
```

Organize a folder:

```bash
python app.py "C:\path\to\folder"
```

The tool writes `organizer.log` inside the target directory.
