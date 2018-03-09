import pybullet as p
import pybullet_data
from Robotel import Robotel
from Road import Road

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #use by loadURDF

p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)

road = Road()
road.create_road()

robot = Robotel(position=road.get_road_points()[100000].get_road_point_position())

robot.get_output_sensor_for_near_road_points(road)

while 1:
    p.stepSimulation()

p.disconnect()