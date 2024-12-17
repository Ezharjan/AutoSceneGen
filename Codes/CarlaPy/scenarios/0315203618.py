'''Question: In a safe sparse traffic scenario, during a wet and cloudy noon, there are 2 vehicles and 3 pedestrians on the road. One of the vehicles is being driven dangerously, exhibiting negligence towards traffic signs and lights. The pedestrians and vehicles maintain a safe distance from each other.'''
import utils 
def generate_scenario():
    # Configs
    vehicles_count = 2 
    walkers_count = 3 
    weather = utils.WeatherPresets.WetCloudyNoon 

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count)
    dangerous_vehicle = utils.g_vehicles[0] 
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 10) 
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -30) 
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) 
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 0) 
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) 
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 0)

    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)