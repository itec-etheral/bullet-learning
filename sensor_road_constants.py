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


consts = Const() # const instance to call the class 
