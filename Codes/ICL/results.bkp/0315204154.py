'''Question: During a foggy morning, there are 8 pedestrians walking on the street, accompanied by 10 vehicles being driven. One vehicle has its windows covered in mist, obstructing the driver's visibility and posing a potential risk to pedestrians and other vehicles.'''
import utils
def generate_scenario():
    vehicles_count = 10
    walkers_count = 8
    weather = utils.WeatherPresets.WetCloudyNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, 0)
    dangerous_vehicle = utils.g_vehicles[0]
    utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_All)
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)