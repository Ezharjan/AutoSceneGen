'''Question: In a safe sparse traffic scenario, during a misty evening, there are 2 vehicles and 3 pedestrians on the road. Intern vehicles, which are still learning, occasionally make sudden stops or slow down unexpectedly. The pedestrians and other vehicles exercise caution when encountering the intern vehicles.'''
import utils
def generate_scenario():
    vehicles_count = 2
    walkers_count = 3
    percentage_pedestrians_running = 0.0
    weather = utils.WeatherPresets.CloudySunset

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)

    for i in range(vehicles_count):
        intern_vehicle = utils.g_vehicles[i]
        traffic_manager.distance_to_leading_vehicle(intern_vehicle, 10)
        traffic_manager.vehicle_percentage_speed_difference(intern_vehicle, -30)
        traffic_manager.ignore_lights_percentage(intern_vehicle, 0)
        traffic_manager.ignore_vehicles_percentage(intern_vehicle, 0)
        traffic_manager.ignore_signs_percentage(intern_vehicle, 0)
        traffic_manager.ignore_walkers_percentage(intern_vehicle, 0)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)