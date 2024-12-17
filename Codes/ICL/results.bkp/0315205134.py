'''Question: In a semi-dangerous vehicle scenario, during a foggy and rainy afternoon, 30% of the vehicles have malfunctioning turn signals. These vehicles exhibit erratic behavior, making sudden lane changes without signaling. There are 10 pedestrians on the wet road, with 3 pedestrians running and 7 pedestrians crossing.'''
import utils

def generate_scenario():
    vehicles_count = 10
    walkers_count = 10
    percentage_pedestrians_running = 0.3
    weather = utils.WeatherPresets.SoftRainNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)

    for i in range(int(vehicles_count * 0.3)):
        dangerous_vehicle = utils.g_vehicles[i]
        traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0)
        traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)