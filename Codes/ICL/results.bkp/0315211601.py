'''Question: In a dangerous dense traffic scenario, during a stormy evening, 75% of the vehicles are being driven aggressively in heavy traffic. These vehicles disregard lane markings and speed limits, posing a severe threat to pedestrians and other vehicles. There are 25 pedestrians navigating the challenging weather conditions.'''
import utils
def generate_scenario():
    # Configs
    vehicles_count = 100 # As the scenario is dense traffic, we set a high number of vehicles
    walkers_count = 25
    percentage_pedestrians_running = 0.0
    percentage_pedestrians_jumping = 0.0
    weather = utils.WeatherPresets.HardRainSunset # Stormy evening can be interpreted as HardRainSunset

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    # As 75% of vehicles are being driven aggressively, we use a for loop to set the behaviors for the first 75 vehicles
    for i in range(75):
        dangerous_vehicle = utils.g_vehicles[i]
        utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_All) # All lights are open to increase visibility in stormy weather
        traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0)
        traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
        traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
        traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)
        dangerous_vehicle.open_door(utils.VehicleDoors.All)
    
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)