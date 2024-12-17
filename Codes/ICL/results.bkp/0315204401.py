'''Question: In a safe dense traffic scenario, during a hazy sunset, there are 30 vehicles and 20 pedestrians sharing the road. Some pedestrians are walking briskly, while others are using designated crosswalks. Some vehicles have their headlights on, improving visibility in the challenging weather conditions.'''
import utils 

def generate_scenario():
    vehicles_count = 30 
    walkers_count = 20 
    percentage_pedestrians_running = 0.5 
    weather = utils.WeatherPresets.SoftRainSunset 

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)
    for vehicle in utils.g_vehicles:
        utils.set_vehicle_light(vehicle, utils.VehicleLights.Open_Low_Beam)

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)