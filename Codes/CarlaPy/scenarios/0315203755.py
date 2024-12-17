'''Question: In a dangerous dense traffic scenario, during a mid-rainy noon, 40% of the vehicles are being dangerously driven in crowded traffic. These vehicles ignore traffic signs, lights, and other vehicles, increasing the risk of accidents. There are 15 pedestrians navigating the challenging weather conditions.'''
import utils 
def generate_scenario(): 
    # Configs
    vehicles_count = 10 
    walkers_count = 15 
    weather = utils.WeatherPresets.MidRainyNoon 

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, 0) 

    for i in range(int(vehicles_count * 0.4)): 
        dangerous_vehicle = utils.g_vehicles[i] 
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100) 
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) 

    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)