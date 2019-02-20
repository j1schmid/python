#import pack0.mod02
#pack0.mod02.test_mod02()

import pack0 # or import pack0.mod00
from pack0 import mod00
from pack0.mod00 import test_mod00

from pack0.mod01 import test_mod01


print('import and call test_mod00 in 3 different ways')
pack0.mod00.test_mod00()
mod00.test_mod00()
test_mod00()
print('')


print('import and call test_mod01')
test_mod01()
print('')


from pack0.subpack00.mod000 import test_mod000

print('import and call test_mod000')
test_mod000()
print('')


from pack0.mod02 import test_mod02

print('import and call test_mod02')
test_mod02()
print('')


print('done')


