#!/bin/python3

import math
import os
import random
import re
import sys


a=int(input(""))
if a%2!=0:
    print("Weird")
else:
    if (a>=2)and(a<=5):
       print("Not Weird")
    elif (a>=6)and(a<=20):
       print("Weird")  
    elif (a>20):
       print("Not Weird") 
