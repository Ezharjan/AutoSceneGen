'''Question: In a safe sparse traffic scenario, during a soft rainy sunset, there are 2 vehicles and 3 pedestrians on the road. Intern vehicles, which are semi-dangerous, maintain a safe distance from other objects but occasionally unintentionally open their doors, requiring caution from other road users.'''
import utils
def generate_scenario():
    # Configs
    vehicles_count = 2
    walkers_count = 3
    weather = utils.WeatherPresets.SoftRainSunset

    # Logics
    traffic_manager = utils.initialize_scenario(walkers_count, vehicles_count, 0)
    semi_dangerous_vehicle = utils.g_vehicles[0] 
    utils.set_vehicle_light(semi_dangerous_vehicle, utils.VehicleLights.Open_Left_Blinker)
    traffic_manager.distance_to_leading_vehicle(semi_dangerous_vehicle, 5)
    semi_dangerous_vehicle.open_door(utils.VehicleDoors.All)
    utils.g_world.set_weather(weather)
    utils.start_game_loop(utils.g_world)