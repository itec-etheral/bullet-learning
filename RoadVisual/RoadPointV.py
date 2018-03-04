from URDFObjects import URDFObject
from sensor_road_constants import consts_obj
import pybullet as p

class RoadPoint(URDFObject):

    """
    Used as part of the big road
    """

    def __init__(self, road_point_position):
        super().__init__(consts_obj.ROADPOINT_URDF_PATH, road_point_position)

    def get_road_point_position(self):
        return p.getBasePositionAndOrientation(self._obj)[0]
