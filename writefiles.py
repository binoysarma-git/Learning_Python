
import os
import json

class WriteFiles:
    

    #xpath=""

    def __init__(self, xpath):
        self.xpath=xpath

    def readfile(self):
        try:
            ls=[]
            for root, dirs, files in os.walk(self.xpath, topdown=False):
                for name in files:
                    ls.append(os.path.join(root,name))  
            return ls
        except Exception as ex:
            print(ex)

    def createdictionary(self,ls_pass):
        dc={}
    
        for item in ls_pass:
            print(item)
            e=".".join(item.split("\\")[-1].split(".")[0:2])
            val=0
            with open(item,"r" ) as file:
                content=file.read()
                val=len(content)
            dc[e]=val
        return dc


    def writetofile(self,dc):
        try:
            ypath=self.xpath+"\\output.txt"
            with open(ypath,"w" ) as file:
                file.write(json.dumps(dc))
        except Exception as ex:
            print("Error thrown due to invalid arguments!","\n" ,ex)
            

# ls=readfile(xpath)
# dc=createdictionary(ls)
# writetofile(xpath,dc)