import time
import os
print(os.environ['ChatGPTKey'])
myCodeNexusPath=os.environ['myCodeNexusPath']
with open(myCodeNexusPath+'/py/tools/hadSent.log', "r+", encoding='utf-8') as f:
        days = f.read()
        print(days)
        f.close()