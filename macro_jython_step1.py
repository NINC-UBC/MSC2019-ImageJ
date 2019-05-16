# this is a comment 

import os # os module allows us to interact with the filesystem ie to get the list of files, like getFileList

# some variables to store the folder information
in_folder = "E:/DataBinge_ImageJ/ImageJ DB/5 files tiff - Copy/"
out_folder = "E:/DataBinge_ImageJ/ImageJ DB/Claire Output/"

# use os module to list files, store in a variable to access later
the_files = os.listdir(in_folder) # filenames are stored in a list [item1, item2, item3, item4, item5]

# Note that python uses dot notation to run commands.  Object.command means take the object and do the command

# print to make sure you have the right filenames
print(the_files)
