'''Question: On a windy day with gusty winds, there is a traffic jam. There are 25 pedestrians walking, 8 pedestrians running, and 4 pedestrians crossing. Inside the traffic jam, there is a dangerous vehicle with a faulty horn, making it difficult for other road users to be alerted of its presence.'''
import utils
def generate_scenario():
    vehicles_count = 50
    walkers_count = 37
    percentage_pedestrians_running = 8 / walkers_count
    weather = utils.WeatherPresets.WetCloudyNoon
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