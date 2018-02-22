import pybullet as p
import sensor_road_constants as sr_cnst
import numpy as np
from URDFObjects import URDFObject 

class IRSensor(URDFObject):

    """
    sensor_pos_vector3 a 3 length list
    TODO add car references to replace the sensorPos in the get_sensor_response() func
    """
    

    def __init__(self, sensor_pos_vector3):
        super().__init__(sensor_pos_vector3)


    def get_sensor_response(self, sensor_road_input) -> float: # reference to the current point in the road
        """
        it returns a value between [0, 1] 
            - for big distances the value goes towards 1
            - for small distances the value goes towards 0
            (0 when the sensor it's on the middle of the road, 1 when it's on the MAX_MARGIN_VALUE)
        """
        # getting the positions of the 2 objects
        sensorPos, _ = p.getBasePositionAndOrientation(self._sensor_obj)
        roadPos, _ = p.getBasePositionAndOrientation(sensor_road_input.get_sensor_obj())

        response = np.array(roadPos) - np.array(sensorPos) # difference and transform it
        # in a np array -> narray for further calculations
        response_mag = np.sum(response*response) ** 0.5 # magnitude
        mapped_responde = response_mag / sr_cnst.consts.MAX_ROAD_MARGIN
        # how the distance > MAX_ROAD_MARGIN -> the value it's mapped between [0,1]
        print("MAPPED_RESPONDE: " + str(mapped_responde))
        return mapped_responde



