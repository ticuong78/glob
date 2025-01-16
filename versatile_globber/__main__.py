from versatile_globber.utils import *

if __name__ == "__main__":
    path = ["E:/Storage/DikeDataset/files/benign"]
    extensions = ['.exe', '.ole']

    globber = ExtensionGlobber(path, extensions)

    print(globber.all)