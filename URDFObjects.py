import pybullet_data
import pybullet as p

class URDFObject(object):
    """
    class to process all the URDF references 
    """

    def __init__(self, sensor_pos_vector3): 
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        if len(sensor_pos_vector3) == 3:
            self._sensor_obj = p.loadURDF("lego\lego.urdf", sensor_pos_vector3) 
        else:
            raise ValueError("use a 3 length ensor_pos_vector3 list as argument")

    def get_sensor_obj(self):
        return self._sensor_obj