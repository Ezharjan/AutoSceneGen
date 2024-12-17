'''Question: On a rainy day, there is a traffic jam. There are 20 people walking and 2 people running. Inside traffic jam, there is a dangerous vehicle ignoring everything and making collisions with the pedestrians as well as other vehicles.'''
import utils
def generate_scenario():
    vehicles_count = 10
    walkers_count = 22
    percentage_pedestrians_running = 2/22 
    weather = utils.WeatherPresets.MidRainyNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    dangerous_vehicle = utils.g_vehicles[0]
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0)
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)