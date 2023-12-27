# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:18:01 2023

@author: Gabriel Duran
"""
import re

test = "<ta>bLe<TaBlewidth=100></table></ta>"



    
char = "BODY"
num = "10"
tag = "<><BODY garbage>body</BODY>"
#def tag_identifier(string, num, tag):
print(re.search(char, tag))
