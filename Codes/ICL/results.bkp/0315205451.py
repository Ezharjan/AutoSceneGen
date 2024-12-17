'''Question: In a safe dense traffic scenario, during a clear evening, there are 20 vehicles and 15 pedestrians sharing the road. Some pedestrians are walking at a moderate pace, while others are using pedestrian crossings. A semi-dangerous vehicle occasionally exceeds the speed limit, posing a potential risk to other road users.'''
import utils 
def generate_scenario(): 
    vehicles_count = 20 
    walkers_count = 15 
    percentage_pedestrians_running = 0.0
    weather = utils.WeatherPresets.ClearSunset
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) 
    semi_dangerous_vehicle = utils.g_vehicles[0] 
    traffic_manager.distance_to_leading_vehicle(semi_dangerous_vehicle, 0) 
    traffic_manager.vehicle_percentage_speed_difference(semi_dangerous_vehicle, -10)
    traffic_manager.ignore_lights_percentage(semi_dangerous_vehicle, 10)
    traffic_manager.ignore_vehicles_percentage(semi_dangerous_vehicle, 10) 
    traffic_manager.ignore_signs_percentage(semi_dangerous_vehicle, 10) 
    traffic_manager.ignore_walkers_percentage(semi_dangerous_vehicle, 10) 
    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)