'''Question: In a dangerous vehicle scenario, during a foggy and drizzly afternoon, 18% of the vehicles have malfunctioning headlights. These vehicles exhibit negligent driving behavior, disregarding traffic signs and failing to use turn signals. There are 5 pedestrians on the wet road, with 2 pedestrians running and 3 pedestrians crossing.'''
import utils

def generate_scenario():
    vehicles_count = 10 # Assuming total vehicles as 10, so 18% of them are dangerous 
    walkers_count = 5 
    percentage_pedestrians_running = 2/walkers_count # 2 out of 5 pedestrians are running
    weather = utils.WeatherPresets.SoftRainNoon # Assuming foggy and drizzly afternoon as SoftRainNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)

    for i in range(int(vehicles_count * 0.18)): # 18% of vehicles are dangerous
        dangerous_vehicle = utils.g_vehicles[i]
        utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Turn_off_All) # Headlights are malfunctioning
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) # Ignoring traffic lights
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) # Ignoring traffic signs
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100) # Ignoring other vehicles
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100) # Ignoring pedestrians

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)