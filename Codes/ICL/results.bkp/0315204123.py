'''Question: On a snowy day with heavy snowfall, there is a traffic jam. There are 15 pedestrians walking, 5 pedestrians running, and 3 pedestrians crossing. Inside the traffic jam, there is a dangerous vehicle with malfunctioning brakes, ignoring traffic signals and causing near-miss incidents with pedestrians and other vehicles.'''
import utils
def generate_scenario():
    vehicles_count = 20
    walkers_count = 23
    percentage_pedestrians_running = 5 / 23
    weather = utils.WeatherPresets.SoftRainNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    dangerous_vehicle = utils.g_vehicles[0]
    utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Left_Blinker)
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0)
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)
    dangerous_vehicle.open_door(utils.VehicleDoors.All)
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)