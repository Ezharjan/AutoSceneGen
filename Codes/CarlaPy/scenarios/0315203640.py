'''Question: In a safe dense traffic scenario, during a clear sunset, there are 25 vehicles and 20 pedestrians sharing the road. Some pedestrians are running, while others are crossing. Safe vehicles operate in autopilot mode and strictly obey traffic rules.'''
import utils 
def generate_scenario(): 
    # Configurations
    vehicles_count = 25 
    walkers_count = 20 
    percentage_pedestrians_running = 0.5
    weather = utils.WeatherPresets.ClearSunset 

    # Scenario Initialization
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, percentage_pedestrians_running) 
    for vehicle in utils.g_vehicles: 
        traffic_manager.auto_mode_percentage(vehicle, 100) 
        traffic_manager.ignore_lights_percentage(vehicle, 0) 
        traffic_manager.ignore_vehicles_percentage(vehicle, 0) 
        traffic_manager.ignore_signs_percentage(vehicle, 0) 
        traffic_manager.ignore_walkers_percentage(vehicle, 0) 

    # Setting Weather
    utils.g_world.set_weather(weather) 

    # Starting Game Loop
    utils.start_game_loop(utils.g_world)