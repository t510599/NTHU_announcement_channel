import os 
import time
print("run.py")
for f in os.listdir("/usr/src/app/crawler"):
    print(f)
    if f[-3:] == ".py":
        print("Excute : python " + f)
        os.system("python crawler/" + f)

