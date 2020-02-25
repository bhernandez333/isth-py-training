"""Service methods for file endpoints"""
from app.common import Constants
import os


class fileRepository:

    def get_file(self, id):
        return NotImplementedError

    def post_file(self, nombre, data):
        filepath = os.path.join(FILE_UPLOAD_PATH, nombre) 
        if not os.path.exists(FILE_UPLOAD_PATH):
            os.makedirs(FILE_UPLOAD_PATH)
        d = data.provide()
        # return NotImplementedError
        return open(filepath, "a")
