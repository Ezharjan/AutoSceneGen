'''Question: In a dangerous dense traffic scenario, during a rainy noon, 60% of the vehicles are being recklessly driven in congested traffic, creating a hazardous environment for other road users. There are 25 pedestrians navigating the chaotic conditions, with some seeking shelter from the rain.'''
import utils
def generate_scenario():
    vehicles_count = 60
    walkers_count = 25
    percentage_pedestrians_running = 0.0
    weather = utils.WeatherPresets.MidRainyNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)

    for vehicle in utils.g_vehicles:
        traffic_manager.distance_to_leading_vehicle(vehicle, 0)
        traffic_manager.vehicle_percentage_speed_difference(vehicle, -50)
        traffic_manager.ignore_lights_percentage(vehicle, 100)
        traffic_manager.ignore_vehicles_percentage(vehicle, 100)
        traffic_manager.ignore_signs_percentage(vehicle, 100)
        traffic_manager.ignore_walkers_percentage(vehicle, 100)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)