'''Question: In a semi-dangerous vehicle scenario, during a drizzly morning, 20% of the vehicles have malfunctioning windshield wipers. These vehicles exhibit negligent driving behavior, compromising visibility in wet conditions. There are 7 pedestrians on the road, with one pedestrian carrying a large umbrella.'''
import utils
def generate_scenario():
    vehicles_count = 5
    walkers_count = 7
    percentage_pedestrians_running = 0.0
    weather = utils.WeatherPresets.WetNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)

    for i in range(int(vehicles_count*0.2)):
        dangerous_vehicle = utils.g_vehicles[i]
        utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Left_Blinker)
        traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0)
        traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)