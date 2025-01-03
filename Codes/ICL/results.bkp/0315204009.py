'''Question: In a safe sparse traffic scenario, during a clear sunset, there are 3 vehicles and 2 pedestrians on the road. One of the vehicles is being driven dangerously, exhibiting negligence towards traffic signs. The pedestrians and vehicles maintain a safe distance from each other. Please note that these scenario descriptions tightly contain the specified scenario attributes, including specific values for pedestrians, vehicles, their behaviors, dangerous and semi-dangerous vehicles, intern vehicles, safe vehicles, dense and sparse traffic, varying vehicle light states, and different weather conditions.'''
import utils
def generate_scenario():
    vehicles_count = 3
    walkers_count = 2
    weather = utils.WeatherPresets.ClearSunset

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, 0)
    dangerous_vehicle = utils.g_vehicles[0]

    traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100)
    traffic_manager.ignore_lights_percentage(dangerous_vehicle, 0)
    traffic_manager.ignore_vehicles_percentage(dangerous_vehicle, 0)
    traffic_manager.ignore_walkers_percentage(dangerous_vehicle, 0)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)