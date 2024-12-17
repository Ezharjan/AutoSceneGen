'''Question: In a semi-dangerous vehicle scenario, during a wet and cloudy noon, 30% of the vehicles have wrong lights. These vehicles exhibit negligence towards traffic signs and lights. There are 10 pedestrians on the wet road, with 3 pedestrians running and 7 pedestrians crossing.'''
import utils
def generate_scenario():
    vehicles_count = 10
    walkers_count = 10
    percentage_pedestrians_running = 0.3
    weather = utils.WeatherPresets.WetCloudyNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    
    for i in range(int(vehicles_count*0.3)): # 30% of the vehicles have wrong lights
        negligent_vehicle = utils.g_vehicles[i]
        utils.set_vehicle_light(negligent_vehicle, utils.VehicleLights.Open_Left_Blinker) 
        traffic_manager.ignore_lights_percentage(negligent_vehicle, 100)
        traffic_manager.ignore_signs_percentage(negligent_vehicle, 100)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)