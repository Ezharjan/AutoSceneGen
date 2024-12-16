context = '''
In a dangerous dense traffic scenario with 70 vehicles on the road, during a mid-rainy noon, 40% of the vehicles are being dangerously driven in crowded traffic. These vehicles ignore traffic signs, lights, and other vehicles but do not ignore pedestrians, increasing the risk of accidents. There are 100 pedestrians navigating the challenging weather conditions which 30 percent of them are running.
'''
################################################################################################################################################################
context_head = '''
I'm using a simulator to simulate some dangerous driving scenarios. Here are some rules to generate a scenario:
1. If you want to set vehicles count, just try setting "vehicles_count".
2. If you want to set pedestrians count, just try setting "walkers_count".
3. If you want to set the percentage of the pedestrians running, just try setting "percentage_pedestrians_running".
4. If you want to set the percentage of the pedestrians jumping, you not only have to set "percentage_pedestrians_jumping", but also need to set "pedestrians_jumping_interval", indicating the interval of each jump.
5. If you want to set weather, never try to make up by yourself! You can only choose from: ClearNoon, CloudyNoon, WetNoon, WetCloudyNoon, SoftRainNoon, MidRainyNoon, HardRainNoon, ClearSunset, CloudySunset, WetSunset, WetCloudySunset, SoftRainSunset, MidRainSunset, HardRainSunset.  If there is no exact word found in the new scenario description, just try to select one of the most related words from the choice list given for setting weather. For example, scenario description may be "It is a day raining cats and dogs", then you can choose 'HardRainSunset' from the choice list; the scenario description may be "It is a cloudy evening", then you can choose 'CloudyNoon' from the choice list, etc.
6. It can be many dangerous vehicles with different attributes, and even there can be no dangerous vehicles at all. It's all up to the scenario description.
7. Some vehicles' door might be opened, you can only choose from "Front_Left, Front_Right, Rear_Left, Rear_Right, All" for indicating the door state of the vehicle. Never try to make up by yourself, just choose from the given choices.
8. You can use "for-loop" to enumerate vehicles and walkers if needed.
9. Remember to generate "import utils" before generating your code!
10. Never try to make some list index out of range!
Based on the rules given above, here are some basic utilities to generate a common scenario which contains a dangerous vehicle, do not use any APIs not mentioned in the following example code:
```python
import utils # [keep this line unchanged!]
def generate_scenario(): # [keep this line unchanged!]
    # Configs
    vehicles_count = 3 # determine the desired number of vehicles to be spawned, not final count
    walkers_count = 27 # determine the desired number of walkers to be spawned, not final count
    percentage_pedestrians_running = 0.3 # percentage ranges from 0.0 to 1.0
    percentage_pedestrians_jumping = 0.5 # percentage ranges from 0.0 to 1.0
    pedestrians_jumping_interval = 5 # this value should not be 0! Its unit is 'seconds'
    weather = utils.WeatherPresets.ClearNoon # You can choose from: from: ClearNoon, CloudyNoon, WetNoon, WetCloudyNoon, SoftRainNoon, MidRainyNoon, HardRainNoon, ClearSunset, CloudySunset, WetSunset, WetCloudySunset, SoftRainSunset, MidRainSunset, HardRainSunset.
    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) # [keep this line unchanged!]
    dangerous_vehicle = utils.g_vehicles[0] # Choose one of the vehicle as a dangerous vehicle
    utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Left_Blinker) # Choose from: Turn_off_All, Open_Position, Open_Low_Beam, Open_High_Beam, Open_Brake, Open_Right_Blinker, Open_Left_Blinker, Open_Reverse, Open_Fog, Open_Interior, Open_All
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0) # Sets the minimum distance in meters that a vehicle has to keep with the others. The distance is in meters and will affect the minimum moving distance. It is computed from front to back of the vehicle objects. 
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50) # The difference the vehicle's intended speed and its current speed limit. Speed limits can be exceeded by setting the second param to a negative value. Default is 30. Exceeding a speed limit can be done using negative percentages. 
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) # Between 0 and 100. Amount of times traffic lights will be ignored. 
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100) # Between 0 and 100. Amount of times collisions will be ignored. 
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) # Between 0 and 100. Amount of times stop signs will be ignored. 
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100) # Between 0 and 100. Amount of times collisions will be ignored. 
    dangerous_vehicle.open_door(utils.VehicleDoors.All) # Choose from: Front_Left, Front_Right, Rear_Left, Rear_Right, All        
    utils.set_walkers_jump_interval(utils.g_world, utils.g_walkers, pedestrians_jumping_interval, percentage_pedestrians_jumping) # Set walkers jump repeatedly. Delete this line if no needed. This line of code is only for demonstration, you can delete it if the prompt does not contain related description.
    utils.g_world.set_weather(weather) # You can delete this line if there is no weather-related description in the prompt.
    utils.start_game_loop(utils.g_world) # [keep this line unchanged!]
```
Based on the example codes above, generate a new scenario described below:
'''
context_tail = '''
Start generating your code inside the function named "generate_scenario"! (Note that you can remove some codes, delete some unused parameters and functions, try to make your code as clean as possible! You do not have to generate comments!)
'''
