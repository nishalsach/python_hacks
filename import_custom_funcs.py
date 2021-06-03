# Importing custom functions

# 1. Some sys fixes

import sys
sys.path.append("..") 

# 2. The SourceFileLoader Class

from importlib.machinery import SourceFileLoader
mymodule = SourceFileLoader('myfile2', 'D:/myfile2.py').load_module()

mymodule.myfunction2('Hello World!')