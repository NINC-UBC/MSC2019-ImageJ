# Now we can create a for loop, which will perform a series of steps repeatedly

import os 
from ij import IJ 
from ij import WindowManager as wm 
from ij.plugin import ImageCalculator

ic = ImageCalculator()

in_folder = "E:/DataBinge_ImageJ/ImageJ DB/5 files tiff - Copy/"
out_folder = "E:/DataBinge_ImageJ/ImageJ DB/Claire Output/"

the_files = os.listdir(in_folder)

# a for loop begins like this:
for item in the_files:
    # for every "item" in in_folder, do this:
    # the series of steps is inserted as a block, which is indicated by an indent

    IJ.open(in_folder + item)	
    imp = IJ.getImage()
    imp.setTitle("current")	
    IJ.run("Scale...", "x=.5 y=.5 z=1.0 width=128 height=128 depth=930 interpolation=Bilinear average process create")
    imp.close()	
    IJ.selectWindow("current-1")
    IJ.run("Z Project...", "projection=[Average Intensity]")	
    imp = ic.run("Subtract create 32-bit stack", wm.getImage("current-1"), wm.getImage("AVG_current-1"))
    imp.show()
    imp = ic.run("Divide create 32-bit stack", wm.getImage("Result of current-1"), wm.getImage("AVG_current-1"))
    imp.show()	
    IJ.selectWindow("Result of Result of current-1")
    IJ.setMinAndMax(-0.0200, 0.2000)	
    IJ.run("Aselfmade3")	
    IJ.saveAs(IJ.getImage(), "Tiff", out_folder + item + '-processed')
    IJ.run("Close All", "")
    
