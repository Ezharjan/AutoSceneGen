'''Question: During a sunny afternoon, there are 10 pedestrians walking on the street, accompanied by 12 vehicles being driven. One vehicle has a cracked windshield, obstructing the driver's view and potentially compromising safety on the road.'''
import utils # [keep this line unchanged!]
def generate_scenario(): # [keep this line unchanged!]
    vehicles_count = 12
    walkers_count = 10
    weather = utils.WeatherPresets.ClearNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, 0)
    dangerous_vehicle = utils.g_vehicles[0]
    utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Left_Blinker)
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0)
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)