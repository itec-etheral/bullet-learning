import pybullet as p
import pybullet_data
from Robotel import Robotel
from RoadVisual.RoadV import Road

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #use by loadURDF

p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)

road = Road()
road.create_road()

robot = Robotel(position=road.get_road_points()[70].get_road_point_position())


print("Lenght of road points: {len}".format(len=len(road.get_road_points())))
print("First ROBOT sensor output: {output}".format(output=robot.get_sensors_response(road.get_road_points()[70].get_road_point_position())))

# for road_point in road.get_road_points():#     print(robot.get_sensors_response(road_point.get_road_point_position()))
#     p.stepSimulation()

while 1:
    p.stepSimulation()

p.disconnect()