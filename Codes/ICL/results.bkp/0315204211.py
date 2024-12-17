'''Question: In a safe dense traffic scenario, during a sunny afternoon, there are 40 vehicles and 30 pedestrians sharing the road. Some pedestrians are jogging, while others are waiting at crosswalks. Safe vehicles operate in autonomous mode, following traffic rules and maintaining a safe distance from other objects.'''
import utils 

def generate_scenario(): 
    vehicles_count = 40
    walkers_count = 30
    percentage_pedestrians_running = 0.5
    weather = utils.WeatherPresets.ClearNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) 

    for vehicle in utils.g_vehicles:
        traffic_manager.distance_to_leading_vehicle(vehicle, 5)
        traffic_manager.vehicle_percentage_speed_difference(vehicle, 0)
        traffic_manager.ignore_lights_percentage(vehicle, 0)
        traffic_manager.ignore_vehicles_percentage(vehicle, 0)
        traffic_manager.ignore_signs_percentage(vehicle, 0)
        traffic_manager.ignore_walkers_percentage(vehicle, 0)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)