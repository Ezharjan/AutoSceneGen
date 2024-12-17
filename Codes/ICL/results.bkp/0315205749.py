'''Question: In a dangerous dense traffic scenario, during a rainy evening, 55% of the vehicles are being recklessly driven in congested traffic, posing a significant risk to other road users. There are 20 pedestrians navigating the chaotic conditions, seeking shelter from the rain.'''
import utils
def generate_scenario():
    # Configs
    vehicles_count = 100 # Assuming total vehicles as 100 to calculate 55% reckless vehicles
    walkers_count = 20
    percentage_pedestrians_running = 0.5 # Assuming half of the pedestrians are running to seek shelter
    percentage_pedestrians_jumping = 0.0 # No jumping pedestrians in this scenario
    pedestrians_jumping_interval = 0 # No jumping pedestrians in this scenario
    weather = utils.WeatherPresets.MidRainSunset # Assuming it's a rainy evening

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    
    for i in range(int(vehicles_count*0.55)): # 55% of vehicles are being recklessly driven
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