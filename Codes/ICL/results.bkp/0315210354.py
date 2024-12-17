'''Question: In a safe sparse traffic scenario, during a misty evening, there are 2 vehicles and 3 pedestrians on the road. Intern vehicles, which are still learning, occasionally make sudden stops or slow down unexpectedly. The pedestrians and other vehicles exercise caution when encountering the intern vehicles.'''
import utils
def generate_scenario():
    # Configs
    vehicles_count = 2
    walkers_count = 3
    percentage_pedestrians_running = 0.0
    weather = utils.WeatherPresets.CloudySunset

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    for vehicle in utils.g_vehicles:
        traffic_manager.vehicle_percentage_speed_difference(vehicle, -50)
        traffic_manager.distance_to_leading_vehicle(vehicle, 5)
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)