#from mod00 import test_mod00

# from ..pack1.mod10 import test_mod00 # -> ValueError: attempted relative import beyond top-level package
# instead use absolute imports and for running the script standalone use the following:


if __name__ == '__main__':
    print('run as standalone script, so add root directory (of the project) to \"path\"')
    import sys
    sys.path.append('..') # to handle the absolute imports



from pack1.mod10 import test_mod10

def test_mod02():
    print('test_mod02')
    test_mod10()

if __name__ == '__main__':
    test_mod02()
