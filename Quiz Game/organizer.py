import logging
import os
import shutil
from pathlib import Path

from categories import get_category, CATEGORIES, DEFAULT_CATEGORY


def organize_directory(directory: Path, dry_run: bool = False) -> int:
    """Scan a directory recursively and move files into category subfolders."""
    root_dir = directory.resolve()
    if not root_dir.exists() or not root_dir.is_dir():
        raise ValueError(f"Target path is not a valid directory: {directory}")

    category_names = set(CATEGORIES) | {DEFAULT_CATEGORY}
    move_count = 0

    for root, dirs, files in os.walk(root_dir):
        current_dir = Path(root)
        # avoid recursing into folders we create for sorted files
        dirs[:] = [d for d in dirs if d not in category_names]

        for filename in files:
            file_path = current_dir / filename
            if file_path.name == "organizer.log":
                continue

            category = get_category(file_path.suffix)
            destination_dir = root_dir / category
            destination_dir.mkdir(parents=True, exist_ok=True)
            destination_path = destination_dir / filename

            if dry_run:
                logging.info("Dry run: would move %s to %s", file_path, destination_path)
                continue

            try:
                shutil.move(str(file_path), str(destination_path))
                logging.info("Moved %s to %s", file_path, destination_path)
                move_count += 1
            except PermissionError as error:
                logging.error("Permission denied moving %s to %s: %s", file_path, destination_path, error)
            except OSError as error:
                logging.error("Error moving %s to %s: %s", file_path, destination_path, error)

    return move_count
