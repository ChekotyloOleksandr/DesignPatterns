from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def show_info(self):
        pass


class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"File {self.name}.exe",end=' ')


class Picture(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"File {self.name}.png",end=' ')


class Document(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"File {self.name}.doc",end=' ')


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def show_info(self):
        print(f"Directory {self.name}:")
        for child in self.children:
            child.show_info()
            print(f'in directory {self.name}')
        print()


file1 = File("file")
file2 = Picture("picture1")
file3 = Document("documnet")
dir1 = Directory("dir1")
dir1.add_child(file1)
dir2 = Directory("dir2")
dir1.add_child(dir2)
dir2.add_child(file2)
dir2.add_child(file3)
dir1.show_info()
print()
dir1.remove_child(dir2)
dir1.show_info()