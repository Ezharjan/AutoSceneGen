'''Question: In a semi-dangerous vehicle scenario, during a misty afternoon, 10% of the vehicles have malfunctioning headlights. These vehicles exhibit negligent driving behavior, failing to illuminate the road properly. There are 8 pedestrians on the misty road, with 2 pedestrians running and 6 pedestrians crossing.'''
import utils

def generate_scenario():
    # Configs
    vehicles_count = 10
    walkers_count = 8
    percentage_pedestrians_running = 0.25
    weather = utils.WeatherPresets.MidRainyNoon

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    for i in range(int(vehicles_count * 0.1)):
        dangerous_vehicle = utils.g_vehicles[i]
        utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Turn_off_All)
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)