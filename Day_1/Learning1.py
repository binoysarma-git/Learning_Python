# function to get the read all the files
# function to generate a dictionary with key value pairs. Key =Name of the files, Value =Toal Char
# function to save the dictionary in a new file

import os
import json
xpath="E:\\Personal\\Learning\\Python\\Files"


def readfile(xpath):
    ls=[]
    for root, dirs, files in os.walk(xpath, topdown=False):
        for name in files:
            #print (os.path.join(root,name))
            ls.append(os.path.join(root,name))
        
        # for name in dirs:
        #   print(os.path.join(root, name))
        #     ls.append(os.path.join(root,name))
        #     print(ls)
    #print(ls)  
    return ls

def createdictionary(ls_pass):
    dc={}
   
    for item in ls_pass:
        print(item)
        e=".".join(item.split("\\")[-1].split(".")[0:2])
        print(e)
        # f=e.split(".")[0:2]
        # f=".".join(f)
        # print(f)
        val=0
        with open(item,"r" ) as file:
            content=file.read()
            print(content)
            val=len(content)
            print(val)
        dc[e]=val
    print (dc)
    return dc


def writetofile(xpath,dc):
    ypath=xpath+"\\output.txt"
    with open(ypath,"w" ) as file:
        file.write(json.dumps(dc))

ls=readfile(xpath)
dc=createdictionary(ls)
writetofile(xpath,dc)