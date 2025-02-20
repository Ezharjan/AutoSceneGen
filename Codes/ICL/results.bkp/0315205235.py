'''Question: In a safe sparse traffic scenario, during a foggy and drizzly morning, there are 2 vehicles and 4 pedestrians on the road. One of the vehicles is being driven recklessly, frequently overtaking other vehicles in low visibility conditions. The pedestrians and vehicles maintain a safe distance from each other.'''
import utils
def generate_scenario():
    # Configs
    vehicles_count = 2
    walkers_count = 4
    percentage_pedestrians_running = 0.0
    weather = utils.WeatherPresets.SoftRainNoon 

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    dangerous_vehicle = utils.g_vehicles[0]
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 5) 
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) 
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100) 
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) 
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100) 

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)