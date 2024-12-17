'''Question: In a semi-dangerous vehicle scenario, during a drizzly afternoon, 15% of the vehicles have malfunctioning turn signals. These vehicles exhibit erratic behavior, ignoring traffic signs and making sudden lane changes. There are 6 pedestrians on the wet road, with one pedestrian carrying an open umbrella.'''
import utils
def generate_scenario():
    # Configs
    vehicles_count = 15 # 15% of the vehicles have malfunctioning turn signals.
    walkers_count = 6 # There are 6 pedestrians on the wet road.
    weather = utils.WeatherPresets.WetNoon # during a drizzly afternoon

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, 0) # 0% of pedestrians running
    for i in range(vehicles_count):
        dangerous_vehicle = utils.g_vehicles[i] # Choose each vehicle as a dangerous vehicle
        utils.set_vehicle_light(dangerous_vehicle, utils.VehicleLights.Open_Left_Blinker) # malfunctioning turn signals
        traffic_manager.ignore_signs_percentage(dangerous_vehicle, 100) # ignoring traffic signs
        traffic_manager.vehicle_percentage_speed_difference(dangerous_vehicle, -50) # making sudden lane changes

    utils.g_world.set_weather(weather) 
    utils.start_game_loop(utils.g_world)