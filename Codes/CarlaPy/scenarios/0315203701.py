'''Question: In a semi-dangerous vehicle scenario, during a soft rainy noon, 10% of the vehicles have wrong lights. These vehicles exhibit negligence towards traffic signs and lights. There are 10 pedestrians on the wet road, with 2 pedestrians running and 8 pedestrians crossing.'''
import utils
def generate_scenario():
    vehicles_count = 10
    walkers_count = 10
    percentage_pedestrians_running = 0.2
    weather = utils.WeatherPresets.SoftRainNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    
    for i in range(int(vehicles_count * 0.1)):
        vehicle = utils.g_vehicles[i]
        utils.set_vehicle_light(vehicle, utils.VehicleLights.Open_Low_Beam)
        traffic_manager.ignore_lights_percentage(vehicle, 100)
        traffic_manager.ignore_signs_percentage(vehicle, 100)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)