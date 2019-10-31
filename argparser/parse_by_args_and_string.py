import sys
import argparse
import copy

import code # entering the interactive mode at a certain point: code.interact(local=dict(globals(), **locals())), Ctrl+D and the script goes on


parser = argparse.ArgumentParser(description='Argparse Test script')
#parser.add_argument("param", help='some parameter')
parser.add_argument("--flag0", help='some flag')
parser.add_argument("--flag1", help='some flag')




str_from___ = 'a command: python parse_by_args_and_string.py --flag0 0.2'
#str_from___ = 'a command: python another_script_name_____.py --flag0 0.2'

# preprocess the string
args_from___ = str_from___.replace('a command: python ','').split()


print('a string/line:          ', str_from___)
print('sys.argv:               ', sys.argv) # to remove brackets *(sys.argv)
print('preproc args from ... : ', args_from___)

code.interact(local=dict(globals(), **locals()))

# (1) parse the flags from the command line, (2) the ones given by the string 
# list.
# ATTENTION the flags from the command line might be overwritten
args_sim = parser.parse_args() # equivalent to parser.parse_args(sys.argv[1:])
args_ext = parser.parse_args(args_from___[1:], namespace=args_sim)
# ATTENTION &args_sim == &args_ext and args_sim == args_ext

args_cli = parser.parse_args()
args_fr_ = parser.parse_args(args_from___[1:])

# join them by ... does not work since arguments will also be overwritten by defautls, etc.
{**vars(args_cli), **vars(args_fr_)}
{**vars(args_fr_), **vars(args_cli)}


# To prioritize a higher the order can be adjusted.
args = parser.parse_args(args_from___[1:])
# no need to store the returnes args it is still the same
parser.parse_args(namespace=args)



# add an flag manually
parser.parse_args(['--flag0','0.0'], args)
# or simply by
args.flag0 = '4.8'


# modify a flag temporary can be done by copy the namespace object (args)
args_cp = copy.deepcopy(args)
args_cp == args # True

parser.parse_args(['--flag0','0.0'], args_cp)
args_cp == args # False





# ------------------------------------------------------------------------------
# archived snippets

#with open(fname) as f:

#argString = 'someTestFile'
#print(argString)
#argString

#args = parser.parse_args()

#parser.parse_args(['python','parse_by_args_and_string.py','a','--flag0','1.2'])

#parser.parse_args(['parse_by_args_and_string.py', 'aasd', '--flag0', '1.0'])
