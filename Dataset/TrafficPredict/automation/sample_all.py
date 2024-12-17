"""
For gaining metric values of all epochs. 
"""
import os

total_epochs = 300 # total models trained
venv_name = "carla" # conda activate venv_name
model_data_dir_pairs = [
    ("../model-(A5+B)/", "../data-(A5+B)/"),
    ("../model-(A5+B48)/", "../data-(A5+B48)/"),
    ("../model-(A5+B48)-II/", "../data-(A5+B48)-II/"),
    ("../model-(A5)/", "../data-(A5)/"),
    ("../model-original/", "../data-original/")
    ("../model-(B10)/", "../data-(B10)/"),
]

script_path = "../srnn/sample.py"

def write_results_to_file(dir_sv_rslts):
    if not os.path.exists(dir_sv_rslts):
        os.makedirs(dir_sv_rslts)    
    result_file = os.path.join(dir_sv_rslts, "results.md")
    if os.path.exists(result_file):
        print(result_file)
        os.remove(result_file)
    # Create the "results.md" file and write the table header
    with open(result_file, "w") as f:
        f.write("|   Rank   |     Method     |         TAE         |        ADEv         |         ADEp        |         ADEb        |         TFE         |        FDEv         |        FDEp         |       FDEb          | Epoch |\n")
        f.write("|----------|----------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|-------|\n")
        
def sample_dataset():
    for model_dir, data_dir in model_data_dir_pairs:
        write_results_to_file(data_dir) # save the real result in dataset directory to publicize them
        for epoch in range(total_epochs):
            cmd = f"conda run -n {venv_name} python {script_path} --epoch={epoch} --model_dir='{model_dir}' --data_dir='{data_dir}' --column_name='| Baseline |'"
            print(cmd)
            os.system(cmd)

sample_dataset()