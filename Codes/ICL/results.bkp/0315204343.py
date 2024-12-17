'''Question: In an intern vehicle scenario, during a light rain in the morning, there are 2 intern vehicles on the road. These vehicles are still learning and occasionally make abrupt stops or slow down unexpectedly. There are 4 pedestrians navigating the wet conditions, taking extra caution around the intern vehicles.'''
import utils 

def generate_scenario():
    # Configs
    vehicles_count = 2 
    walkers_count = 4 
    percentage_pedestrians_running = 0.0 
    weather = utils.WeatherPresets.SoftRainNoon 

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    for vehicle in utils.g_vehicles:
        traffic_manager.distance_to_leading_vehicle(vehicle, 0) 
        traffic_manager.vehicle_percentage_speed_difference(vehicle, -50) 
        traffic_manager.ignore_lights_percentage(vehicle, 100) 
        traffic_manager.ignore_vehicles_percentage(vehicle, 100) 
        traffic_manager.ignore_signs_percentage(vehicle, 100) 
        traffic_manager.ignore_walkers_percentage(vehicle, 100) 

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)