# Photo Organizer

A Python script that automatically organizes photos into folders based on their capture date. It supports various image formats including JPG, JPEG, PNG, GIF, BMP, and HEIC (commonly used by Apple devices).

## Features

- Organizes photos by year and date (YYYY/YYYY-MM-DD structure)
- Supports multiple image formats (JPG, JPEG, PNG, GIF, BMP, HEIC)
- Extracts date from EXIF data (falls back to file modification date if EXIF is unavailable)
- Handles duplicate filenames automatically
- Option to copy instead of move files
- Supports recursive directory processing
- Detailed error reporting
- Cross-platform compatibility (Windows, macOS, Linux)

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/devwanderlei/photo-organizer.git
cd photo-organizer
```

2. Create and activate virtual environment:

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Platform-Specific Python Setup (if needed)

#### Windows
- Install Python from [python.org](https://www.python.org/downloads/windows/)
- During installation, make sure to check "Add Python to PATH"

#### macOS
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

## Project Structure
```
photo-organizer/
│
├── README.md
├── requirements.txt
├── photo_organizer.py
```

## Requirements

The project dependencies are listed in `requirements.txt`:
```
Pillow>=10.0.0
pillow-heif>=1.5.0
```

## Usage

Make sure your virtual environment is activated before running the script.

### Command Line Interface

Basic usage:
```bash
python photo_organizer.py /path/to/source/photos
```

Copy instead of move:
```bash
python photo_organizer.py /path/to/source/photos --copy
```

Specify destination directory:
```bash
python photo_organizer.py /path/to/source/photos --dest_dir /path/to/destination
```

### As a Python Module

```python
from photo_organizer import organize_photos

# Move files
success, errors = organize_photos("/path/to/photos")

# Copy files instead of moving
success, errors = organize_photos("/path/to/photos", copy=True)

# Specify destination directory
success, errors = organize_photos("/path/to/photos", base_dir="/path/to/destination")
```

## Output Structure

The script organizes photos in the following structure:
```
destination_directory/
    2024/
        2024-01-01/
            photo1.jpg
            photo2.heic
        2024-01-02/
            photo3.png
    2023/
        2023-12-31/
            photo4.jpg
```

## Error Handling

The script provides detailed error reporting:
- Successfully processed files count
- List of files that couldn't be processed with error messages
- Automatic handling of duplicate filenames

## Development

To set up the development environment:

1. Create a new virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

3. Install development dependencies:
```bash
pip install -r requirements.txt
```

4. To deactivate the virtual environment when you're done:
```bash
deactivate
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

Copyright (c) 2024 Wanderlei

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact

Wanderlei - devwanderlei@gmail.com

Project Link: https://github.com/wanderlei2583/organizador_de_fotos_por_data
