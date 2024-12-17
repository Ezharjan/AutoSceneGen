'''Question: In an intern vehicle scenario, during a light rain in the evening, there are 2 intern vehicles on the road. These vehicles are still learning and occasionally hesitate at intersections, causing minor delays. There are 4 pedestrians navigating the wet conditions, exercising caution around the intern vehicles.'''
import utils
def generate_scenario():
    vehicles_count = 2 
    walkers_count = 4 
    percentage_pedestrians_running = 0.0 
    weather = utils.WeatherPresets.SoftRainSunset 

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) 

    for vehicle in utils.g_vehicles:
        traffic_manager.vehicle_percentage_speed_difference(vehicle, -10) 
        traffic_manager.ignore_lights_percentage(vehicle, 50) 
        traffic_manager.ignore_vehicles_percentage(vehicle, 50) 
        traffic_manager.ignore_signs_percentage(vehicle, 50) 
        traffic_manager.ignore_walkers_percentage(vehicle, 50) 

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)