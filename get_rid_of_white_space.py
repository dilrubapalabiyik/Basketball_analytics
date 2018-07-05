
# coding: utf-8

# In[13]:

import re
import csv
import os


file_needed = open('/Users/dilruba_p/Desktop/last.txt','r')

white_space =  re.compile(r'^\s*$')
start_with_T = re.compile(r'(^T.*)')
contains_0_dot = re.compile(r'.*(\.0)')

garbage_list = []
useful_stuff = []

for line in file_needed:
	if(bool(white_space.search(line))==True):
		garbage_list.append(line)
	elif(bool(start_with_T.search(line))==False):
		garbage_list.append(line)
	elif(bool(start_with_T.search(line))==True and bool(contains_0_dot.search(line))==True):
		useful_stuff.append(line.split('\t'))
	elif(bool(start_with_T.search(line))==True and bool(contains_0_dot.search(line))==False):
		garbage_list.append(line)

print(len(useful_stuff))
print(len(garbage_list))

for i in range(len(useful_stuff)):
	print(useful_stuff[i])

with open('/Users/dilruba_p/Desktop/hanlded_last.csv','a', newline = '') as ft:
			a = csv.writer(ft,delimiter = ',')
			# a.writerow(columns_1)  ---- we don't need columns' names here
			a.writerows(useful_stuff)

