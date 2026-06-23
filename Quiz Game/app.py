import argparse
import logging
import sys
import traceback
from pathlib import Path

from organizer import organize_directory


LOG_FILENAME = "organizer.log"


def configure_logging(log_file: Path) -> None:
    logging.basicConfig(
        filename=str(log_file),
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filemode="a",
    )


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Organize files in a directory into category subfolders."
    )
    parser.add_argument(
        "target_directory",
        type=Path,
        help="The directory to scan and organize.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview file moves without performing them.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    target_dir = args.target_directory

    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Target path is not a valid directory: {target_dir}")
        sys.exit(1)

    log_file = target_dir / LOG_FILENAME
    log_file.parent.mkdir(parents=True, exist_ok=True)
    configure_logging(log_file)

    logging.info("Starting organization: %s (dry run=%s)", args.target_directory, args.dry_run)

    try:
        moved = organize_directory(args.target_directory, dry_run=args.dry_run)
        if args.dry_run:
            print("Dry run complete. No files were moved.")
        else:
            print(f"Organization complete. {moved} files moved.")
    except ValueError as error:
        logging.error("Invalid directory: %s", error)
        print(error)
        sys.exit(1)
    except Exception as error:
        logging.exception("Unexpected error during organization.")
        traceback.print_exc()
        print(f"An unexpected error occurred: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
