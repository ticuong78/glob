from src.config import *
from src.utils import *

def main(CONFIG: dict):
    input_paths = CONFIG['envs']['INPUT_PATH']
    extensions = CONFIG['envs']['EXTENSIONS']

    categorizer = PathCategorize()
    dirs, exes = categorizer.categorize(input_paths)

    globber = ExtensionGlobber(dirs, extensions) #

    print(globber.all)
    print(len(globber.all))

if __name__ == "__main__":
    # print(CONFIG)
    main(CONFIG)