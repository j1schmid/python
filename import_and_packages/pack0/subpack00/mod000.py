# Allowed since the mod00 package is not in the directory where the script was called
from ..mod00 import test_mod00

def test_mod000():
    print('test_mod000 and call test_mod00 from child directory/package')
    test_mod00()
