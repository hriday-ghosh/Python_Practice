# Q1. Create a File Class for reading data from respective file with a method name read and write.
class file_read(object):
    def __init__(self, filename) -> None:
        self.filename = filename


class read(file_read):
    def read(self):
        try:
            open_file = open(self.file, "r")
            self.read_file = open.file.read()
            open_file.close()
        except Exception as e:
            return e


class write(file_read):
    def write(self, *args):
        try:
            open_file = open(self.file, "w")
            for elements in args:
                open_file.write(elements)
                return True

        except Exception as e:
            return e
