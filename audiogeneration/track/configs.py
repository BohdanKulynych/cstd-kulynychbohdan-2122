import os

UPLOAD_FOLDER_NAME = 'temp'
GENERATED_UPLOAD_FOLDER_NAME = 'static'
INITIAL_UPLOAD_SUBFOLDER_NAME = 'input_songs'
GENERATED_UPLOAD_SUBFOLDER_NAME = 'audio'
ALLOWED_EXTENSIONS = ["mid"]
UPLOAD_DIR = os.path.normpath(os.path.join(f"{os.getcwd()}/audiogeneration", os.path.join(UPLOAD_FOLDER_NAME, INITIAL_UPLOAD_SUBFOLDER_NAME)))
GENERATED_UPLOAD_DIR = os.path.normpath(os.path.join(f"{os.getcwd()}/audiogeneration", os.path.join(GENERATED_UPLOAD_FOLDER_NAME, GENERATED_UPLOAD_SUBFOLDER_NAME)))



