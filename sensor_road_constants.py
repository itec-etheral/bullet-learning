def constant(f): # readonly decorative
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)



class Const(object):
    """
    class used for sensor and road constants
    """

    @constant # readonly decorative
    def MAX_ROAD_MARGIN() -> float:
        # the right and left extremes of the road (with - for the left side)
        return 1.5

    @constant 
    def IRSENSOR_URDF_PATH() -> str:
        return "lego\lego.urdf"

    @constant
    def ROADPOINT_URDF_PATH() -> str:
        return "table\\table.urdf"

    @constant
    def MAX_ROAD_POINTS() -> int:
        return 20
    
    @constant
    def ROAD_POINTS_STEP() -> float:
        return 0.4

    @constant
    def A_ROAD_ELLIPSE() -> float: # it has to be >= MAX_ROAD_POINTS/2 to work
        return 10

    @constant
    def B_ROAD_ELLIPSE() -> float:
        return 4.0

    @constant
    def DEVIATION_ROAD() -> float:
        return 0.6


consts_obj = Const() # Const instance to call the class 
