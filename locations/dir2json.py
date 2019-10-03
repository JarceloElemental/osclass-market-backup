"""
Simple json.list file creator in directory in which script is located
This will create a json list of directory structure
can be improved as per our use case.
@Author navjottomer
"""
import os
import json

print('Simple Json list creator. ')


def path_to_dict(path, no_child=False):
    d = {}
    if os.path.isdir(path) and no_child == False:
        d['name'] = os.path.basename(path)
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path, x), True)
                         for x in os.listdir(path)]
    else:
        d['name'] = os.path.basename(path)
        d['type'] = "file"
    return d


resultedJsonOfCurrentDirectoryStructure = json.dumps(path_to_dict(
    os.path.dirname(os.path.abspath(__file__))), indent=4)

currentScriptDirectory = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(currentScriptDirectory, 'list.json'), 'w+')
f.write(resultedJsonOfCurrentDirectoryStructure)
f.close()

print_msg = 'A list.json file is created in ' + \
    os.path.dirname(os.path.abspath(__file__))
print(print_msg)
