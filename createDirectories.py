import os
import shutil
try:
    original_umask = os.umask(0)
    inputPath = os.path.expanduser('~/.fortiate/temp/preprocessedCsvs')
    # outputPath = os.path.expanduser('~/.fortiate/temp/cleanedCsvs')
    if not os.path.exists(inputPath):
        os.makedirs(inputPath)
    # if not os.path.exists(outputPath):
    #     os.makedirs(outputPath)
    #
    # source = 'csvSource'
    # dest = inputPath
    # filesCsv = []
    # files = os.listdir(source)
    # for file in files:
    #     if '.csv' in file:
    #         filesCsv.append(file)
    # if len(files) == 0:
    #     pass
    # else:
    #     for f in files:
    #         shutil.copy((source + '/' + f), dest)
finally:
    os.umask(original_umask)