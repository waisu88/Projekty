import os


class FileInfo:
    def __init__(self, filename):
        self.filename = filename
        self.extension = self.get_file_extension()

    def get_file_extension(self):
        file_extension = os.path.splitext(self.filename)[1][1:]
        return file_extension
