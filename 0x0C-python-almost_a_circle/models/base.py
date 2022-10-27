"""
Base class
"""

class Base:
    """
    A class with a initialization module:
     The goal of it is to manage id attribute in all your
     future classes and to avoid duplicating the same code
     (by extension, same bugs)
    """


    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing the class and id variable 
        """
        if id is not None:
            self.id =  id

        else:
            __nb_objects += 1

            self.id = __nb_objects
