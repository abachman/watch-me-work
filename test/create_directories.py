import os

def create_tmp_directories():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tmp'))
    for dir in ['test1/nested_01/nested_02', 'test2/test', 'test3/test' ]:
        try:
            os.makedirs(os.path.join(root, dir))
        except OSError:
            pass

def remove_tmp_directories():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tmp'))
    for dir in os.listdir(root):
        os.system("rm -rf %s" % os.path.join(root, dir))

