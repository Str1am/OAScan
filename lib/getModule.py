import os
modules = []
def get_module(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path,i))]
    files = [i for i in lsdir if os.path.isfile(os.path.join(path,i))]
    for each in files:
        modules.append(each.split('.')[0])
    return modules
