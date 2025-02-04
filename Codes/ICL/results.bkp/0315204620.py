'''Question: In a semi-dangerous vehicle scenario, during a misty noon, 12% of the vehicles have malfunctioning headlights. These vehicles exhibit negligent driving behavior, failing to illuminate the road properly. There are 8 pedestrians on the misty road, with 2 pedestrians running and 6 pedestrians crossing.'''
import utils
def generate_scenario():
    # Configs
    vehicles_count = 12 
    walkers_count = 8 
    percentage_pedestrians_running = 2/8 
    weather = utils.WeatherPresets.CloudyNoon 

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    for i in range(int(vehicles_count*0.12)): # 12% of vehicles have malfunctioning headlights
        dangerous_vehicle = utils.g_vehicles[i] 
        utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Position) 
        traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0) 
        traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100) 

    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)