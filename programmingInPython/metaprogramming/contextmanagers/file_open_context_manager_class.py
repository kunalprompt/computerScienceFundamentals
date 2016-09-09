class File(object):

    def __init__(self, filename, mode):
        self.file = filename
        self.file_mode = mode

    def __enter__(self):
        self.open_file = open(self.file, mode=self.file_mode)
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open_file.close()


with File('file_open_context_manager_class.py', 'a') as f:
    f.write("\n# a comment added\n")
