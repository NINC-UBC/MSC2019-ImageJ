import os 
from ij import IJ # we will need this to read in files among other things.
from ij import WindowManager as wm 
from ij.plugin import ImageCalculator

# create an instance of image calculator so we can use it in dot notation 
ic = ImageCalculator()

in_folder = "E:/DataBinge_ImageJ/ImageJ DB/5 files tiff - Copy/"
out_folder = "E:/DataBinge_ImageJ/ImageJ DB/Claire Output/"

the_files = os.listdir(in_folder) 

print(the_files)

the_file = the_files[0] 

print(the_file)

# open the_file inside in_folder.
dat = IJ.open(in_folder + the_file) # Note that strings (string = "stuff") are joined by concatenation 

# select the active window
imp = IJ.getImage()

# use the same renaming trick as for the macro recorder
imp.setTitle("current")

# IJ.run executes commands from the macro recorder
IJ.run(
    "Scale...", "x=.5 y=.5 z=1.0 width=128 height=128 depth=930 interpolation=Bilinear average process create"
    ) 
imp.close()
IJ.selectWindow("current-1")
IJ.run(
    "Z Project...", "projection=[Average Intensity]"
    )

# Note the new imports above, WindowManager and ImageCalculator
# ic.run executes commands within image calculator; wm.getImage selects the image using WindowsManager
imp = ic.run(
    "Subtract create 32-bit stack", wm.getImage("current-1"), wm.getImage("AVG_current-1")
    )
imp.show()
imp = ic.run(
    "Divide create 32-bit stack", wm.getImage("Result of current-1"), wm.getImage("AVG_current-1")
    ) 
imp.show()
IJ.selectWindow("Result of Result of current-1")

# adjust the Brightness/Contrast
IJ.setMinAndMax(-0.0200, 0.2000)

# this is the Lookup Tables step 
IJ.run("Aselfmade3")

# IJ.saveAs has 3 arguments: (image, file type, file path)
IJ.saveAs(IJ.getImage(), "Tiff", out_folder + the_file + '-processed') 
IJ.run("Close All", "")


