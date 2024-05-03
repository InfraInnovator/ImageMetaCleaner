# Image Metadata Manager

## Overview
Image Metadata Manager is a Python script for managing metadata in image files. It offers functionalities to remove all metadata from an image and to add an artist's name to the image's metadata. This tool supports `.jpg`, `.jpeg`, `.png`, `.gif`, and `.bmp` formats.

## Features
- **Remove Metadata:** Strip all metadata from image files to ensure privacy or minimize file size.
- **Add Artist:** Add or update the artist field in the image's metadata.

## Requirements
- Python 3.x
- PIL library

## Installation
To use this script, you will need Python installed on your system. If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/). Additionally, you will need the PIL library, which can be installed via pip:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Removing Metadata from files
```bash
python ./img_metadata.py -r ./image.png
```

### Removing Metadata from irectories:
```bash
python ./img_metadata.py -r ./image_directory
```


## Testing

```bash
exiftool TestImage-Canon_40D.jpg
python ./img_metadata.py -r ./TestImage-Canon_40D.jpg
```
