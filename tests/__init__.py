import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO) -> None:
    """Clears the contents of a given stream."""
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)


def delete_file(file_path: str) -> None:
    """Removes a file if it exists."""
    if os.path.isfile(file_path):
        os.unlink(file_path)


def reset_store(store: FileStorage, file_path: str = 'file.json') -> None:
    """Resets the items in the given store."""
    with open(file_path, mode='w') as file:
        file.write('{}')
    if store is not None:
        store.reload()


def read_text_file(file_name: str) -> str:
    """Reads the contents of a given file."""
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


def write_text_file(file_name: str, text: str) -> None:
    """Writes a text to a given file."""
    with open(file_name, mode='w') as file:
        file.write(text)
