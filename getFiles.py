from os import listdir
from os.path import isfile, join

def getFiles(dirname):
    onlyFiles = [f for f in listdir(dirname) if isfile(join(dirname, f))]
    
    return onlyFiles

