import os

from config import PROJECT_ROOT


# Function to read content from a Markdown file
def read_markdown(file_path):
    # Read the file
    absolute_path = build_absolute_path(file_path)
    with open(absolute_path, "r") as file:
        return file.read().strip()


# Function to write content from a Markdown file
def write_markdown(file_path, write_content):
    absolute_path = build_absolute_path(file_path)
    with open(absolute_path, "w") as file:
        file.write(write_content)
        return absolute_path


def build_absolute_path(file_path, base_dir=PROJECT_ROOT):
    # Get the absolute path based on the current script's location
    if base_dir:
        return os.path.join(base_dir, file_path)
    else:
        return file_path
