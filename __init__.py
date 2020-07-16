import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

__version__ = '1.0.1'

try:
    import inquirer
except ImportError as e:
    print("An error was found, but returning just with the version: %s" % e)
