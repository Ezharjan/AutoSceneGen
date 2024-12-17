#!/bin/bash

# List of Python scripts to run
scripts=(
    "trainvae.py --dataset univ"
    "trainsampler.py --dataset univ"
    "test.py --dataset univ"
)

# Function to run a Python script and check its exit status
run_python_script() {
    script_path=$1
    script_args=$2
    
    # Run the Python script with arguments
    python $script_path $script_args
    
    # Check the exit status of the script
    if [ $? -eq 0 ]; then
        echo "Script $script_path completed successfully."
    else
        echo "Script $script_path terminated with an error. Exiting..."
        exit 1
    fi
}

# Run the Python scripts one by one
for script in "${scripts[@]}"; do
    # Extract the script path and arguments
    script_path=$(echo $script | cut -d' ' -f1)
    script_args=$(echo $script | cut -d' ' -f2-)
    
    run_python_script "$script_path" "$script_args"
done

echo "All Python scripts have been executed successfully."