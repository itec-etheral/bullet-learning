from URDFObjects import URDFObject
from sensor_road_constants import consts_obj
from IRSensor import IRSensor
import pybullet as p
from numpy import array


class Robotel(URDFObject):

    """"
    position is used to create a
    self._obj object in the pybullet env

    self._sensors = list with the sensors of the robot
    """

    def __init__(self, position=(0, 0, 0)):
        # position = (position[0], position[1] + 3.5, position[2])
        super().__init__(consts_obj.ROBOT_URDF_PATH, position)
        self._sensors = self._attach_sensors_to_robot()

    @staticmethod
    def number_of_sensosr() -> int:
        return 6

    @staticmethod
    def start_joint_sensor_number() -> int:
        return 2

    def _attach_sensors_to_robot(self) -> list:
        sensors = []

        for current_joint in range(Robotel.start_joint_sensor_number(), Robotel.number_of_sensosr()
                                   + Robotel.start_joint_sensor_number()):
            sensor = IRSensor()
            sensor_position = list(array(p.getLinkState(self._obj, current_joint)[0]))
                                    # + array(p.getBasePositionAndOrientation(self._obj)[0]))
            # global sensor position

            # store in positions in a list
            sensor.initialize_sensor(sensor_position)
            sensors.append(sensor)

        return sensors

    def get_sensors_response(self, current_road_point_position, attach=True) -> list:
        # a list of len(number_of_sensosr()) outputs
        output = []
        # compute the global position of the sensors ( it changes every time the
        # car moves

        if attach:  # this func it is used also in other logic that does not need this recomputation
            self._sensors = self._attach_sensors_to_robot()

        for sensor in self._sensors:
            output.append(sensor.get_sensor_response(current_road_point_position))

        return output

    def get_sensors(self) -> list:
        return self._sensors

    def get_output_sensor_for_near_road_points(self, road) -> list:
        # get output sensor from the point that you are on top of

        self._sensors = self._attach_sensors_to_robot()
        # retake the sensors position

        for road_point in road.get_road_points():
            road_point_pos = road_point.get_road_point_position()
            distance_on_x_axis = self._sensors[2].get_position()[0] - road_point_pos[0]
            distance_on_y_axis = self._sensors[2].get_position()[1] - road_point_pos[1]
            distance = (distance_on_x_axis**2 + distance_on_y_axis**2) ** 0.5

            if distance <= 0.472269:  # empiric number that works just fine (the error it is so big cuz we check
                # the distance with the second sensor position that it usually it is not exactly on top of the line
                # and we compute both x and y axis that both will never be exactly on the line
                return self.get_sensors_response(road_point_pos, attach=False)

        return None
