#!/bin/bash

# List of Python scripts to run
scripts=(
    "1.py"
    "2.py"
    "3.py"
)

# Function to run a Python script and check its exit status
run_python_script() {
    script_path=$1
    
    # Run the Python script
    python $script_path
    
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
    run_python_script "$script"
done

echo "All Python scripts have been executed successfully."