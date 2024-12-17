import cv2
import carla
import random
import numpy as np

save_path = './test/' # TODO: Change THIS LINE TO YOUR OWN DIRECTORY

def camera_callback(image, data):
    capture = np.reshape(np.copy(image.raw_data), (image.height, image.width, 4))
    data["image"] = capture
    cv2.imwrite(f"{save_path}{image.frame}.png", capture)
client = carla.Client('localhost', 2000)
client.set_timeout(500.0)
world = client.get_world()
blueprint_library = world.get_blueprint_library()
spawn_points = world.get_map().get_spawn_points()
vehicle_blueprint = blueprint_library.find('vehicle.audi.etron')
vehicle = world.try_spawn_actor(vehicle_blueprint,random.choice(spawn_points))
camera_blueprint = world.get_blueprint_library().find("sensor.camera.rgb")
camera_transform = carla.Transform(carla.Location(z=2, x=0.5))
camera = world.spawn_actor(camera_blueprint, camera_transform, attach_to=vehicle)
image_width = camera_blueprint.get_attribute("image_size_x").as_int()
image_height = camera_blueprint.get_attribute("image_size_y").as_int()
camera_data = {"image": np.zeros((image_height, image_width, 4))}
camera.listen(lambda image: camera_callback(image, camera_data))
spectator = world.get_spectator()
camera_height = carla.Transform(vehicle.get_transform().transform(carla.Location(x=2,z=0.5)),vehicle.get_transform().rotation)
spectator.set_transform(camera_height)
cv2.namedWindow('Camera', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Camera', camera_data['image'])
cv2.waitKey(1)
while True:
    img = cv2.imshow('Camera', camera_data['image'])
    vehicle.set_autopilot(True)
    if cv2.waitKey(1) == ord('p'):
        client.reload_world()
        break
cv2.destroyAllWindows()