'''Question: In a safe dense traffic scenario, during a mid-rainy sunset, there are 20 vehicles and 15 pedestrians sharing the road. Some pedestrians are running, while others are crossing. Some vehicles update their lights, enhancing visibility in the challenging weather conditions.'''
import utils
def generate_scenario():
    vehicles_count = 20
    walkers_count = 15
    percentage_pedestrians_running = 0.5
    weather = utils.WeatherPresets.MidRainSunset

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    
    for vehicle in utils.g_vehicles:
        utils.set_vehicle_light(vehicle, utils.VehicleLights.Open_Low_Beam)
        
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)