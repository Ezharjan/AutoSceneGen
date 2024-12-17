'''Question: In a safe dense traffic scenario, during a clear noon, there are 30 vehicles and 20 pedestrians sharing the road. Some pedestrians are running, while others are crossing. Safe vehicles operate in autopilot mode and strictly obey traffic rules.'''
import utils
def generate_scenario():
    vehicles_count = 30
    walkers_count = 20
    percentage_pedestrians_running = 0.5
    weather = utils.WeatherPresets.ClearNoon

    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running)

    for vehicle in utils.g_vehicles:
        traffic_manager.auto_mode(vehicle) # All vehicles are in autopilot mode and obey traffic rules

    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)