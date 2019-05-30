# - Delete current folder' some files
import glob, os

def deleteFiles():
    # get current folder
    currentFolder = os.getcwd()
    os.chdir(currentFolder)
    pathnames = glob.glob('{}/*.txt'.format(currentFolder))
    for pathname in pathnames:
        print(pathname)
        os.remove(pathname)