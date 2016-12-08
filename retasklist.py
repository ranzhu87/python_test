#!/usr/bin/env python

import os
import re

f = os.popen('tasklist /nh', 'r')
for eachline in f:
	# print eachline.rstrip()
	print re.findall(r'([\w.]+(?:[\w.]+)*)\s\s+(\d+)\s+\w+\s\s+\d+\s\s+([\d,]+\sK)',eachline.rstrip())


f.close()
