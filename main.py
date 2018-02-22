import pybullet as p
import pybullet_data
import IRSensor as irs

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #use by loadURDF

p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)


sensor1 = irs.IRSensor([0, 0, 0])
sensor2 = irs.IRSensor([1, 0, 0])
print(type(sensor2))

sensor1.get_sensor_response(sensor2)

while 1:
    p.stepSimulation()

p.disconnect()