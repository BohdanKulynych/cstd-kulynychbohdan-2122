from time import strftime
from audiogeneration.track.configs import UPLOAD_DIR,ALLOWED_EXTENSIONS

import os


def validate_extension(filename):
    return filename.rsplit(".")[-1] in ALLOWED_EXTENSIONS


def has_duplicates(filename):
    return filename if filename not in os.listdir(UPLOAD_DIR) else f"{filename.split('.')[0] + strftime('%m%d%Y%H%M%S')}" \
                                                                   f".{ALLOWED_EXTENSIONS[0]} "


