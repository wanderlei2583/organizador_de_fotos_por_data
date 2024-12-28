import os
import shutil
from datetime import datetime
from typing import Optional

from PIL import Image
from pillow_heif import register_heif_opener

# Register the HEIF opener to handle HEIC files
register_heif_opener()


def photo_shooting_date(file_path: str) -> datetime:
    """
    Extract the date when a photo was taken, either from EXIF data or file modification time.

    Args:
        file_path (str): Path to the photo file

    Returns:
        datetime: The date when the photo was taken

    Raises:
        PIL.UnidentifiedImageError: If the file is not a valid image
        FileNotFoundError: If the file doesn't exist
    """
    try:
        with Image.open(file_path) as photo:
            exif = photo.getexif()
            if exif is not None:
                # Try different EXIF tags for date information
                date_tags = [36867, 36868, 36876]  # EXIF date tags
                for tag in date_tags:
                    if tag in exif:
                        try:
                            return datetime.strptime(
                                exif[tag], "%Y:%m:%d %H:%M:%S"
                            )
                        except ValueError:
                            continue

        # If no valid EXIF date found, fall back to file modification time
        return datetime.fromtimestamp(os.path.getmtime(file_path))

    except Exception as e:
        raise Exception(f"Error processing {file_path}: {str(e)}")


def folder_path_from_photo_date(
    file_path: str, base_dir: Optional[str] = None
) -> str:
    """
    Generate a folder path based on the photo's date.

    Args:
        file_path (str): Path to the photo file
        base_dir (str, optional): Base directory for organizing photos

    Returns:
        str: Path where the photo should be stored
    """
    date = photo_shooting_date(file_path)
    relative_path = os.path.join(date.strftime("%Y"), date.strftime("%Y-%m-%d"))

    if base_dir:
        return os.path.join(base_dir, relative_path)
    return relative_path


def move_photo(
    file_path: str, base_dir: Optional[str] = None, copy: bool = False
) -> None:
    """
    Move or copy a photo to its date-based directory.

    Args:
        file_path (str): Path to the photo file
        base_dir (str, optional): Base directory for organizing photos
        copy (bool): If True, copy the file instead of moving it

    Raises:
        FileExistsError: If a file with the same name already exists in the destination
        OSError: If there's an error creating directories or moving/copying the file
    """
    try:
        # Get the destination folder path
        new_folder = folder_path_from_photo_date(file_path, base_dir)

        # Create the destination folder if it doesn't exist
        os.makedirs(new_folder, exist_ok=True)

        # Get the filename and construct the destination path
        filename = os.path.basename(file_path)
        destination = os.path.join(new_folder, filename)

        # Handle duplicate filenames
        if os.path.exists(destination):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination):
                new_filename = f"{base}_{counter}{ext}"
                destination = os.path.join(new_folder, new_filename)
                counter += 1

        # Move or copy the file
        if copy:
            shutil.copy2(file_path, destination)
        else:
            shutil.move(file_path, destination)

    except Exception as e:
        raise Exception(f"Error organizing {file_path}: {str(e)}")


def organize_photos(
    directory: str, base_dir: Optional[str] = None, copy: bool = False
) -> tuple[list[str], list[str]]:
    """
    Organize all photos in a directory based on their dates.

    Args:
        directory (str): Directory containing photos to organize
        base_dir (str, optional): Base directory for organizing photos
        copy (bool): If True, copy files instead of moving them

    Returns:
        tuple[list[str], list[str]]: Lists of successfully and unsuccessfully processed files
    """
    success = []
    errors = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".heic")
            ):
                file_path = os.path.join(root, file)
                try:
                    move_photo(file_path, base_dir, copy)
                    success.append(file_path)
                except Exception as e:
                    errors.append(f"{file_path}: {str(e)}")

    return success, errors


# Example usage:
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Organize photos into folders by date"
    )
    parser.add_argument(
        "source_dir", help="Directory containing photos to organize"
    )
    parser.add_argument(
        "--dest_dir", help="Destination directory for organized photos"
    )
    parser.add_argument(
        "--copy", action="store_true", help="Copy files instead of moving them"
    )

    args = parser.parse_args()

    success, errors = organize_photos(args.source_dir, args.dest_dir, args.copy)

    print(f"Successfully processed {len(success)} files")
    if errors:
        print(f"\nErrors occurred with {len(errors)} files:")
        for error in errors:
            print(f"- {error}")
