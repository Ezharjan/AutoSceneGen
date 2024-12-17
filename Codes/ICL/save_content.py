file_path = "../CarlaPy/autoSceneGen.py"
bkp_file_path = "./results.bkp/"

import datetime
import validate_content
def save(content, comment="", bValidate=True):
    result = ""
    if(bValidate):
        codes = validate_content.validate(content)
        result = comment + codes
    else:
        result = comment + content
    # backup first
    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%m%d%H%M%S")
    with open(bkp_file_path + time_string + ".py", "w") as file:
        file.write(result)
    # then save to the executable path 
    with open(file_path, "w") as file:
        file.write(result)
    print(f">>> Output saved to {file_path}")
