'''Question: On a sunny morning, there are 5 people walking on the street, with 7 vehicles also being driven on the street. There is a vehicle which has opened all of its door and ignoring the pedestrians on the road. But it does not ignore other traffic objects like vehicles or lights or signs.'''
import utils
def generate_scenario():
    vehicles_count = 7
    walkers_count = 5
    weather = utils.WeatherPresets.ClearNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, 0)
    dangerous_vehicle = utils.g_vehicles[0]
    utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Left_Blinker)
    traffic_manager.distance_to_leading_vehicle(dangerous_vehicle, 0)
    traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50)
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 0)
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 0)
    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 0)
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 100)
    dangerous_vehicle.open_door(utils.VehicleDoors.All)
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)