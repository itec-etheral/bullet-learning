from URDFObjects import URDFObject
from sensor_road_constants import consts_obj
from IRSensor import IRSensor
import pybullet as p


class Robotel(URDFObject):

    """"
    position is used to create a
    self._obj object in the pybullet env

    self._sensors = list with the sensors of the robot
    """

    def __init__(self, position=[0, 0, 0]):
        super().__init__(consts_obj.ROBOT_URDF_PATH, position)
        self._sensors = self._attach_sensors_to_robot()

    @staticmethod
    def number_of_sensosr() -> int:
        return 6

    @staticmethod
    def start_joint_sensor_number() -> int:
        return 4

    def _attach_sensors_to_robot(self) -> list:
        sensors = []
        current_joint = Robotel.start_joint_sensor_number()

        for _ in range(Robotel.number_of_sensosr()):
            sensor = IRSensor()
            sensor_position = list(p.getLinkState(self._obj, current_joint)[0])
            # get the position as a list of 3 elements
            sensor.initialize_sensor(sensor_position)
            sensors.append(sensor)

            current_joint += 1

        return sensors

    def get_sensors_response(self, current_road_point_position) -> list:
        # a list of len(number_of_sensosr()) outputs
        output = []
        for sensor in self._sensors:
            output.append(sensor.get_sensor_response(current_road_point_position))

        return output

