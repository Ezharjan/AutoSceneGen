'''Question: In a semi-dangerous vehicle scenario, during a wet sunset, 20% of the vehicles have wrong lights. The semi-dangerous vehicles exhibit negligence towards traffic signs and lights. There are 5 pedestrians on the wet road, with one pedestrian jumping once per interval.'''
import utils

def generate_scenario():
    # Configs
    vehicles_count = 20 # 20% of the vehicles have wrong lights
    walkers_count = 5 
    percentage_pedestrians_running = 0.0
    percentage_pedestrians_jumping = 0.2 # one out of five pedestrians is jumping
    pedestrians_jumping_interval = 1 # pedestrian jumps once per interval
    weather = utils.WeatherPresets.WetSunset

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    for vehicle in utils.g_vehicles:
        utils.set_vehicle_light(vehicle, utils.VehicleLights.Open_Right_Blinker) # setting wrong lights
        traffic_manager.ignore_lights_percentage(vehicle, 100) # ignoring traffic lights
        traffic_manager.ignore_signs_percentage(vehicle, 100) # ignoring traffic signs

    utils.set_walkers_jump_interval(utils.g_world, utils.g_walkers, pedestrians_jumping_interval, percentage_pedestrians_jumping)
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)