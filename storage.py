import json
import os
file_name="data.json"

def load_data():
    if os.path.isfile(file_name) and file_name.endswith(".json"):
        print(f"{file_name} exists!!")
        try:
            with open(file_name,"r") as f:
                return json.load(f)
        except(json.JSONDecodeError,IOError):
            print("JSON file is corrupted!")
            return []

    else:
        print("\nJson file is missing or wrong extension")
        return []
    
def save_data(expenses):

    
    try:
        with open(file_name,"w") as f:
            json.dump(expenses,f,indent=4)
    except IOError:
        print("\n Error couldnt save data")




    
    