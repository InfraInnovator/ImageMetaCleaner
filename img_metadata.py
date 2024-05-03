#!/usr/bin/env python

import os
from PIL import Image
import piexif
import argparse

def remove_metadata(image):
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    return image_without_exif

def add_artist(image_path, artist):
    image = Image.open(image_path)
    exif_dict = piexif.load(image.info['exif'])
    exif_dict['0th'][piexif.ImageIFD.Artist] = artist.encode()
    exif_bytes = piexif.dump(exif_dict)
    image.save(image_path, exif=exif_bytes)
    return image

def parse_arguments():
    parser = argparse.ArgumentParser(description='Manage image metadata.')
    parser.add_argument('-r', '--remove', action='store_true', help='Remove all metadata from the image.')
    parser.add_argument('-artist', help='Artist name to add to the image metadata.')
    parser.add_argument('image_paths', nargs='+', help='Path to the image file(s).')
    return parser.parse_args()

def process_images(args):
    for image_path in args.image_paths:
        if os.path.isdir(image_path):
            for filename in os.listdir(image_path):
                filepath = os.path.join(image_path, filename)
                process_single_image(filepath, args.remove, args.artist)
        else:
            process_single_image(image_path, args.remove, args.artist)

def process_single_image(image_path, remove, artist):
    try:
        image = Image.open(image_path)
        if remove:
            image = remove_metadata(image)
        if artist:
            image = add_artist(image_path, artist)
        image.save(image_path)
        print(f"Processed {image_path}")
    except IOError:
        print(f"Error opening or processing the file {image_path}")

if __name__ == '__main__':
    args = parse_arguments()
    process_images(args)
