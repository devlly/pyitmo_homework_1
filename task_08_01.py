'''Вариант ООП'''

class Config(File):
    def __init__(self, read_meth, write_meth, d, File):
        self.read_meth = read_meth
        self.write_meth = write_meth
        self.file_type = File.get_file_type
        self.d = {
        'txt': (read_txt(), write_txt()),
        'file_type': (read_meth(), write_meth())
        }


    def get_read_meth(self, file_type):
        return d[file_type][0]

    def get_write_meth(self, file_type):
        return d[file_type][1]


    def set_read_write_meth(self, file_type, read_meth, write_meth):
         self.d = d.update({'file_type': (read_meth(), write_meth())})




class File(Config):
    def __init__(self, name, path, file_type):
        self.name = name
        self.path = path
        self.file_type = name.rsplit('.', 1)


    def set_name(self, name):
        self.name = name

    def set_path(self, path):
        self.path = path


    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

    def get_file_type(self):
        return self.file_type


    def read_file(self, file_type ):
        super().get_read_meth()

    def write_file(self, file_type ):
        super().get_write_meth())
