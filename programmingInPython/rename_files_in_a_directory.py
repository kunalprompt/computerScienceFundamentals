"""
Given a directory, rename all the files in that directory.
"""
import os
import random

directory_path = "/home/kunal/Desktop/directory/"

directory = os.listdir(directory_path)

# To print current directory
# print os.getcwd()

for filename in directory:
	os.rename(directory_path+filename, 
				directory_path+str(random.randint(1, 1000)))
