from Player import *


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.__server = player1
        self.__receiver = player2

    def won_point(self, player: Player):
        if player.is_equal(self.__server):
            self.__server.add_point()
        else:
            self.__receiver.add_point()

    def get_score(self):
        d = {}
        d[0] = "Love"
        d[1] = "Fifteen"
        d[2] = "Thirty"
        d[3] = "Forty"

        points_server = self.__server.get_points()
        points_receiver = self.__receiver.get_points()

        if points_server != points_receiver and points_server < 4 and points_receiver < 4:
            return d[points_server] + "-" + d[points_receiver]
        if points_server == points_receiver and points_server < 3 and points_receiver < 3:
            return d[points_server] + "-All"
        if points_server >= 3 and points_receiver == points_server:
            return "Deuce"
        if ((points_server - 2) == points_receiver and points_receiver >= 2) or (
                points_server == 4 and (points_receiver == 0 or points_receiver == 1)):
            return "Win for player1"
        if ((points_receiver - 2) == points_server and points_server >= 2) or (
                points_receiver == 4 and (points_server == 0 or points_server == 1)):
            return "Win for player2"
        if points_server >= 4 and points_receiver >= 3 and points_server - 1 == points_receiver:
            return "Advantage player1"
        if points_receiver >= 4 and points_server >= 3 and points_receiver - 1 == points_server:
            return "Advantage player2"

        return "Love-All"
