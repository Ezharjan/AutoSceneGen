'''Question: In a safe sparse traffic scenario, during a clear night, there are 4 vehicles and 3 pedestrians on the road. One of the vehicles is being driven aggressively, frequently changing lanes without signaling. The pedestrians and other vehicles maintain a safe distance from each other.'''
import utils 

def generate_scenario():
    vehicles_count = 4
    walkers_count = 3
    weather = utils.WeatherPresets.ClearSunset

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, 0)
    dangerous_vehicle = utils.g_vehicles[0] 

    utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Turn_off_All) 
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 10) 
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, 0) 
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 0) 
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 0) 
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 0) 

    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)