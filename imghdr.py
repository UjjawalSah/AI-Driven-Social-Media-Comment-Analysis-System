import os

def what(filename, byte_offset=0):
    """Tries to guess the image type of the given file."""
    with open(filename, 'rb') as file:
        file.seek(byte_offset)
        header = file.read(32)
        if header.startswith(b'\x89PNG\r\n\x1a\n'):
            return 'png'
        elif header.startswith(b'GIF89a') or header.startswith(b'GIF87a'):
            return 'gif'
        elif header.startswith(b'\xff\xd8\xff'):
            return 'jpeg'
        elif header.startswith(b'BM'):
            return 'bmp'
        elif header.startswith(b'\x00\x00\x01\x00'):
            return 'ico'
        else:
            return None
