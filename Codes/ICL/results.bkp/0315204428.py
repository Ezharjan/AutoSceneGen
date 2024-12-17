'''Question: In a semi-dangerous vehicle scenario, during a foggy and rainy noon, 25% of the vehicles have malfunctioning brake lights. These vehicles exhibit reckless driving behavior, frequently tailgating and ignoring traffic signals. There are 12 pedestrians on the wet road, with 4 pedestrians running and 8 pedestrians crossing.'''
import utils

def generate_scenario():
    # Configs
    vehicles_count = 25 # 25% of the vehicles have malfunctioning brake lights
    walkers_count = 12 # 12 pedestrians on the road
    percentage_pedestrians_running = 4 / 12 # 4 out of 12 pedestrians are running
    weather = utils.WeatherPresets.SoftRainNoon # It's a foggy and rainy noon

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    
    for i in range(vehicles_count):
        dangerous_vehicle = utils.g_vehicles[i]
        utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Brake) # Brake lights are malfunctioning
        traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0) # Vehicles are tailgating
        traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50) # Vehicles are driving recklessly
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) # Vehicles are ignoring traffic signals
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100) # Vehicles are ignoring other vehicles
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) # Vehicles are ignoring stop signs
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100) # Vehicles are ignoring pedestrians

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)