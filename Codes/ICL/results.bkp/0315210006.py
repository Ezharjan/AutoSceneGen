'''Question: In a safe dense traffic scenario, during a clear morning, there are 35 vehicles and 25 pedestrians sharing the road. Some pedestrians are walking leisurely, while others are waiting for traffic lights to change. Safe vehicles operate in autonomous mode, prioritizing pedestrian safety and maintaining a steady pace.'''
import utils 

def generate_scenario():
    vehicles_count = 35 
    walkers_count = 25 
    percentage_pedestrians_running = 0.0 
    weather = utils.WeatherPresets.ClearNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) 

    for vehicle in utils.g_vehicles:
        traffic_manager.distance_to_leading_vehicle(vehicle, 5) 
        traffic_manager.vehicle_percentage_speed_difference(vehicle, 0) 
        traffic_manager.ignore_lights_percentage(vehicle, 0) 
        traffic_manager.ignore_vehicles_percentage(vehicle, 0) 
        traffic_manager.ignore_signs_percentage(vehicle, 0) 
        traffic_manager.ignore_walkers_percentage(vehicle, 100)

    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)