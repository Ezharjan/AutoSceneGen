'''Question: In a safe sparse traffic scenario, during a foggy and drizzly evening, there are 3 vehicles and 2 pedestrians on the road. One of the vehicles is being driven recklessly, frequently swerving between lanes without signaling. The pedestrians and vehicles maintain a safe distance from each other.'''
import utils 
def generate_scenario(): 
    vehicles_count = 3 
    walkers_count = 2 
    percentage_pedestrians_running = 0.0 
    weather = utils.WeatherPresets.SoftRainSunset 

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) 
    dangerous_vehicle = utils.g_vehicles[0] 
    utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Left_Blinker) 
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 5) 
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50) 
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100) 
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 0) 
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) 
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 0) 
    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)