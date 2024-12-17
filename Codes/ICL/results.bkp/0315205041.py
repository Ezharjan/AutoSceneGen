'''Question: In a semi-dangerous vehicle scenario, during a drizzly morning, 20% of the vehicles have malfunctioning windshield wipers. These vehicles exhibit negligent driving behavior, compromising visibility in wet conditions. There are 7 pedestrians on the road, with one pedestrian carrying a large umbrella.'''
import utils 
def generate_scenario(): 
    vehicles_count = 5 
    walkers_count = 7 
    percentage_pedestrians_running = 0.0 
    percentage_pedestrians_jumping = 0.0 
    weather = utils.WeatherPresets.WetNoon
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) 
    malfunctioning_vehicles = utils.g_vehicles[:int(vehicles_count * 0.2)] 
    for vehicle in malfunctioning_vehicles:
        utils.set_vehicle_light(vehicle, utils.VehicleLights.Open_Low_Beam) 
        traffic_manager.distance_to_leading_vehicle(vehicle, 0) 
        traffic_manager.vehicle_percentage_speed_difference(vehicle, -50) 
        traffic_manager.ignore_lights_percentage(vehicle, 100) 
        traffic_manager.ignore_vehicles_percentage(vehicle, 100) 
        traffic_manager.ignore_signs_percentage(vehicle, 100) 
        traffic_manager.ignore_walkers_percentage(vehicle, 100) 
        vehicle.open_door(utils.VehicleDoors.All) 
    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)