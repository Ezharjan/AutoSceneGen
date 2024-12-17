'''Question: In a dangerous dense traffic scenario, during a misty morning, 50% of the vehicles are being driven aggressively in congested traffic. These vehicles disregard traffic rules, causing frequent near-miss incidents with pedestrians and other vehicles. There are 15 pedestrians navigating the challenging weather conditions.'''
import utils 
def generate_scenario(): 
    vehicles_count = 100 
    walkers_count = 15 
    percentage_pedestrians_running = 0.0 
    weather = utils.WeatherPresets.MistyMorning 

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) 

    for i in range(int(vehicles_count * 0.5)): 
        dangerous_vehicle = utils.g_vehicles[i] 
        traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0) 
        traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50) 
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100) 

    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)