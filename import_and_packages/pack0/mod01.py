#from __future__ import absolute_import

import code # entering the interactive mode at a certain point: code.interact(local=dict(globals(), **locals())), Ctrl+D and the script goes on
import sys

# One way to handle relative imports but still be able to run the script standalone
# alternative use absolute imports ... refere to mod02.py.
try:
    #import . # -> SyntaxError: invalid syntax
    from .mod00 import test_mod00
    from . import mod00
    
    print('import from root script/directory ...')
    
    # Relative imports while running the script standalone will cause an exception:
    # ImportError       Python 3.6
    # SystemError       Python 3.5
except (ImportError, SystemError) as e:
    print('run as standalone script, exception \"{:}\"'.format(e))
    from mod00 import test_mod00
    import mod00
    sys.path.append('..') # to handle the absolute imports



# For relative imports, the dots . can go up only up to (but not including)
# the directory containing the script run from the command line. Thus, 
# from .. import pack1 is invalid in here. Doing so results in the error 
# ValueError: attempted relative import beyond top-level package.

#import pack1 # does not work, the following does
import pack1.mod10



def test_mod01():
    print('in test_mod01, import and call test_mod00 in 2 differnt ways')
    test_mod00()
    mod00.test_mod00()
    print('')
    
    #code.interact(local=dict(globals(), **locals()))
    
    pack1.mod10.test_mod10()

    #print('sys path', sys.path)

if __name__ == '__main__':
    test_mod00()
    test_mod01()
