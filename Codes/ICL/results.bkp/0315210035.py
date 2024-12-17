'''Question: In a dangerous dense traffic scenario, during a stormy evening, 75% of the vehicles are being driven aggressively in heavy traffic. These vehicles disregard lane markings and speed limits, posing a severe threat to pedestrians and other vehicles. There are 25 pedestrians navigating the challenging weather conditions.'''
import utils
def generate_scenario():
    vehicles_count = 100 
    walkers_count = 25 
    percentage_pedestrians_running = 0.0 
    weather = utils.WeatherPresets.HardRainSunset 

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) 

    for i in range(int(0.75 * vehicles_count)):
        dangerous_vehicle = utils.g_vehicles[i] 
        traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0) 
        traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50) 
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100) 

    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)