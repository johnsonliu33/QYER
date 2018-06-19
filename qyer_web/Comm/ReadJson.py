import json
file_name = "../Data/json.json"

with open(file_name,"r",encoding="utf-8") as f:
    new_dict = json.load(f)
    print(new_dict["name"])
    print(new_dict["age"])
    print(new_dict["no"])

