'''Question: In a dangerous dense traffic scenario, during a rainy evening, 55% of the vehicles are being recklessly driven in congested traffic, posing a significant risk to other road users. There are 20 pedestrians navigating the chaotic conditions, seeking shelter from the rain.'''
import utils
def generate_scenario():
    vehicles_count = 55
    walkers_count = 20
    percentage_pedestrians_running = 0.5
    weather = utils.WeatherPresets.HardRainSunset

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    
    for i in range(vehicles_count):
        dangerous_vehicle = utils.g_vehicles[i]
        traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0)
        traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)
        dangerous_vehicle.open_door(utils.VehicleDoors.All)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)