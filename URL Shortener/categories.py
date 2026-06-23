from pathlib import Path

# File category definitions by extension.
CATEGORIES = {
    "Images": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp",
    },
    "Documents": {
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx",
    },
    "Videos": {
        ".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm",
    },
    "Audio": {
        ".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a",
    },
    "Code": {
        ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".c", ".cpp", ".h", ".cs", ".go", ".rb", ".php", ".rs", ".swift", ".sh", ".html", ".css", ".json", ".yaml", ".yml",
    },
    "Archives": {
        ".zip", ".tar", ".gz", ".bz2", ".rar", ".7z", ".xz",
    },
}

DEFAULT_CATEGORY = "Miscellaneous"

_extension_map = {
    extension: category
    for category, extensions in CATEGORIES.items()
    for extension in extensions
}


def get_category(extension: str) -> str:
    """Return the category name for a file extension."""
    if not extension:
        return DEFAULT_CATEGORY
    return _extension_map.get(extension.lower(), DEFAULT_CATEGORY)
