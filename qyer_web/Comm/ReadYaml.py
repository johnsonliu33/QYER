import os,yaml


file_name1 = os.getcwd()+os.sep+"Data"+os.sep+"contacts_data.yml"

print("wwwww：",file_name1)

file_name = "../Data/yaml.yml"

with open(file_name,"r",encoding="utf-8")as f:
   print(yaml.load(f))



