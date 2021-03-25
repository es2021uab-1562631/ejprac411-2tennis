class Player:

    def __init__(self, name: str):
        self.__name = name
        self.__num_points = 0

    def add_point(self):
        self.__num_points = self.__num_points + 1
        pass

    def get_points(self):
        return self.__num_points

    def is_equal(self, player):
        return self.__name == player.__name
