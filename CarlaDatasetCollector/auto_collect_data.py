# Configuration
config = {
    'script_names_list': [
        "1.py",  # scenario script
        "2.py",
        "3.py"
    ],
    # 'collect_count': 41,  # collect 41 times
    'collect_count': 1,  # collect 41 times
    'steps': 1,  # increase or decrease 5 at a time
    'vehicles_count_range': [2, 1*5],  # min-max value to begin and to stop
    'walkers_count_range': [2, 1*5],
    'map_name_list': [
        "AU",
        "Town01",
        "Town02",
        "Town03",
        "Town04",
        "Town05"
    ]
}

#################################################################
import subprocess
import time

# Function to start a subprocess
def start_process(command):
    return subprocess.Popen(command, shell=True)

# Function to kill a process
def kill_process(process):
    if is_process_alive(process):
        process.terminate()
        process.wait()

# Function to check if a process is alive
def is_process_alive(process):
    return process.poll() is None

# Function to run scenario and collect data
def run_scenario_and_collect(config_this_time):
    # app_command = "./CarlaUE4.sh"
    app_command = f"python app.py"
    scenario_command = f"python {config_this_time['script_name']}"
    collect_command = f"python collect.py"

    # Start the app
    app_process = start_process(app_command)
    time.sleep(10)  # wait until the app is fully launched

    # Start the scenario
    scenario_process = start_process(scenario_command)
    time.sleep(5)  # wait until the scenario is fully launched

    # Start data collection
    collect_process = start_process(collect_command)

    # Monitor the collect process
    while is_process_alive(collect_process):
        time.sleep(1)  # check every second if the process is still alive

    # Kill the scenario and app processes after collection is done
    kill_process(scenario_process)
    kill_process(app_process)

# Main logic to iterate over counts and run processes
def main():
    for i in range(config['vehicles_count_range'][0], config['vehicles_count_range'][1] + 1, config['steps']):
        for j in range(config['walkers_count_range'][0], config['walkers_count_range'][1] + 1, config['steps']):
            for script_name in config['script_names_list']:
                for map_name in config['map_name_list']:
                    config_this_time = {
                        'script_name': script_name,
                        'vehicle_count': i,
                        'walkers_count': j,
                        'map_name': map_name
                    }
                    run_scenario_and_collect(config_this_time)
                    time.sleep(5)
                    print(i, j, script_name, map_name)

if __name__ == "__main__":
    main()
    print("All the data has been successfully collected!")
