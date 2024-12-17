'''Question: In a dangerous vehicle scenario, during a foggy and drizzly afternoon, 15% of the vehicles have malfunctioning headlights. These vehicles exhibit negligent driving behavior, disregarding traffic signs and failing to use turn signals. There are 5 pedestrians on the wet road, with 2 pedestrians running and 3 pedestrians crossing.'''
import utils

def generate_scenario():
    # Configs
    vehicles_count = 15
    walkers_count = 5
    percentage_pedestrians_running = 2/5
    weather = utils.WeatherPresets.SoftRainNoon

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    for i in range(int(vehicles_count * 0.15)): # 15% of vehicles with malfunctioning headlights
        dangerous_vehicle = utils.g_vehicles[i]
        utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Turn_off_All) # headlights malfunctioning
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) # disregard traffic lights
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) # disregard traffic signs
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100) # disregard other vehicles
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100) # disregard pedestrians
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)