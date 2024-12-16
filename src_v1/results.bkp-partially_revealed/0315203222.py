'''Question: On a rainy day with hard rain, there is a traffic jam. There are 20 pedestrians walking, 10 pedestrians running, and 5 pedestrians crossing. Inside the traffic jam, there is a dangerous vehicle with broken compartments, including no vehicle lights and opened doors, ignoring everything and causing collisions with pedestrians and other vehicles.'''
import utils

def generate_scenario():
    vehicles_count = 10
    walkers_count = 35
    percentage_pedestrians_running = 10 / walkers_count
    weather = utils.WeatherPresets.HardRainNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)

    dangerous_vehicle = utils.g_vehicles[0]
    utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Turn_off_All)
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0)
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)
    dangerous_vehicle.open_door(utils.VehicleDoors.All)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)