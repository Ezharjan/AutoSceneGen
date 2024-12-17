'''Question: In an intern vehicle scenario, during a soft rainy noon, there are 2 intern vehicles on the road. These vehicles are semi-dangerous, maintaining a far distance from other objects. At some point, one of the intern vehicles unintentionally opens its door. There are 3 pedestrians navigating the wet conditions.'''
import utils
def generate_scenario():
    vehicles_count = 2
    walkers_count = 3
    weather = utils.WeatherPresets.SoftRainNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, 0)
    semi_dangerous_vehicle = utils.g_vehicles[0]

    traffic_manager.distance_to_leading_vehicle(semi_dangerous_vehicle, 50)
    traffic_manager.vehicle_percentage_speed_difference(semi_dangerous_vehicle, -10)
    traffic_manager.ignore_lights_percentage(semi_dangerous_vehicle, 50)
    traffic_manager.ignore_vehicles_percentage(semi_dangerous_vehicle, 50)
    traffic_manager.ignore_signs_percentage(semi_dangerous_vehicle, 50)
    traffic_manager.ignore_walkers_percentage(semi_dangerous_vehicle, 50)

    semi_dangerous_vehicle.open_door(utils.VehicleDoors.All)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)