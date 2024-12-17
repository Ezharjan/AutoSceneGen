'''Question: In a dangerous vehicle scenario, during a wet and cloudy noon, 20% of the vehicles have wrong lights. These vehicles exhibit negligence towards traffic signs and lights. There are 5 pedestrians on the wet road, with 2 pedestrians running and 3 pedestrians crossing.'''
import utils

def generate_scenario():
    vehicles_count = 5
    walkers_count = 5
    percentage_pedestrians_running = 0.4
    weather = utils.WeatherPresets.WetCloudyNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    
    for i in range(int(vehicles_count * 0.2)):
        dangerous_vehicle = utils.g_vehicles[i]
        utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Left_Blinker)
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
    
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)