'''Question: In a safe dense traffic scenario, during a clear noon, there are 30 vehicles and 20 pedestrians sharing the road. Some pedestrians are running, while others are crossing. Safe vehicles operate in autopilot mode and strictly obey traffic rules.'''
import utils

def generate_scenario():
    # Configs
    vehicles_count = 30
    walkers_count = 20
    percentage_pedestrians_running = 0.5
    weather = utils.WeatherPresets.ClearNoon

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    
    # All vehicles are safe vehicles
    for vehicle in utils.g_vehicles:
        traffic_manager.distance_to_leading_vehicle(vehicle, 5) # Safe distance to leading vehicle
        traffic_manager.vehicle_percentage_speed_difference(vehicle, 0) # No speed difference
        traffic_manager.ignore_lights_percentage(vehicle, 0) # Obey all traffic lights
        traffic_manager.ignore_vehicles_percentage(vehicle, 0) # Respect all vehicles
        traffic_manager.ignore_signs_percentage(vehicle, 0) # Obey all signs
        traffic_manager.ignore_walkers_percentage(vehicle, 0) # Respect all pedestrians

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)