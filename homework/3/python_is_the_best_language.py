#! /usr/bin/env python
from platform import python_version
string1 = "Python is the best language for String manipulation!"
print('This is Python version', python_version() + '\n\n' 
+ string1 + '\n\n'
+ string1[::-1] + '\n\n'
+ string1[::-2] + '\n\n'
+ string1[1] + string1[2::].upper() + '\n\n\n'
+ "The sentence '" + string1 + "' contains\n"
+ "4 'a' letters, and\n"
+ "0 'A' letters!\n\n"
+ string1[0:6] + '\n'
+ string1[7:9] + '\n'
+ string1[10:13] + '\n'
+ string1[14:18] + '\n'
+ string1[19:27] + '\n'
+ string1[28:31] + '\n'
+ string1[32:38] + '\n'
+ string1[39:52] + '\n\n'
+ string1[0:6].upper() + '\n'
+ string1[7:9].upper() + '\n'
+ string1[10:13].upper() + '\n'
+ string1[14:18].upper() + '\n'
+ string1[19:27].upper() + '\n'
+ string1[28:31].upper() + '\n'
+ string1[32:38].upper() + '\n'
+ string1[39:52].upper() + '\n')
