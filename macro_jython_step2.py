import os 

in_folder = "E:/DataBinge_ImageJ/ImageJ DB/5 files tiff - Copy/"
out_folder = "E:/DataBinge_ImageJ/ImageJ DB/Claire Output/"

the_files = os.listdir(in_folder) 

print(the_files)

# pick out a single file to test each step
the_file = the_files[0] # in Python, list[0] means take the first item of list which in this case is the list of filenames

# print to double check
print(the_file)
