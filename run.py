from writefiles import *

wf=  WriteFiles("h:\\abc\\student.txt")
ls=wf.readfile()
dc=wf.createdictionary(ls)
wf.writetofile(dc)