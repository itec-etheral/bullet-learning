from URDFObjects import URDFObject
from sensor_road_constants import consts_obj

class RoadPoint(URDFObject):

    """
    Used as part of the big road
    """

    def __init__(self, road_point_position,):
        super().__init__(consts_obj.ROADPOINT_URDF_PATH, road_point_position)