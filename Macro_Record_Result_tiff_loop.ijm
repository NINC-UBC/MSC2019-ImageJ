path=getDirectory("Choose a Directory");
ls = getFileList(path);

for (i=0; i<ls.length; i++) 
{
	fn=path+ls[i];

open(fn);
rename("current");
run("Scale...", "x=.5 y=.5 z=1.0 width=128 height=128 depth=930 interpolation=Bilinear average process create");
selectWindow("current");
close();
selectWindow("current-1");
run("Z Project...", "projection=[Average Intensity]");
imageCalculator("Subtract create 32-bit stack", "current-1","AVG_current-1");
selectWindow("Result of current-1");
imageCalculator("Divide create 32-bit stack", "Result of current-1","AVG_current-1");
selectWindow("Result of Result of current-1");
selectWindow("Result of current-1");
close();
selectWindow("Result of Result of current-1");
selectWindow("AVG_current-1");
close();
selectWindow("Result of Result of current-1");
selectWindow("current-1");
close();
selectWindow("Result of Result of current-1");
rename(ls[i]);
//run("Brightness/Contrast...");
setMinAndMax(-0.0200, 0.2000);
run("Aselfmade3");
	
}