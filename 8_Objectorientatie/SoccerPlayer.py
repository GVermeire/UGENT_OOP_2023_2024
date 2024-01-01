"""
Copyright (c) 2023. All rights reserved.

@author Zakaria Oubbi <zakaria.oubbi@ugent.be>
"""
from enum import Enum


class SoccerPlayer:
    # The position a player can play on the pitch.
    position = Enum("position", ["GK",  # Goalkeeper
                                 "DF",  # Defender
                                 "MF",  # Midfield
                                 "FW"  # Forward
                                 ])

    def __init__(self, first_name, last_name, age, position):
        """
        SoccerPlayer constructor.

        :param first_name: the first name of the player
        :param last_name: the last name of the player
        :param age: the player's age
        :param position: the position on the pitch
        """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    def __lt__(self, other):
        """
        Compare two SoccerPlayer objects based on their names.

        :param other: the other SoccerPlayer object to compare
        :return: True if their names are equal, False otherwise
        """
        return self.get_name().casefold() == other.get_name().casefold()

    def __eq__(self, other):
        """
        Check if two SoccerPlayer objects are equal.

        :param other: the other object to compare
        :return: True if self is equal to other, False otherwise
        """
        if self is other:
            return True
        if not isinstance(other, SoccerPlayer):
            return False
        return (
                self.age == other.age and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.position == other.position
        )

    def get_age(self):
        """
        Get the age of the player.

        :return: the age
        """
        return self.age

    def get_name(self):
        """
        Get the full name of the player.

        :return: the full name
        """
        return f'{self.first_name} {self.last_name}'

    def get_position(self):
        """
        Get the position of the player.

        :return: the position
        """
        return self.position

    def __hash__(self):
        """
        Compute the hash value of the SoccerPlayer object.

        :return: the hash value
        """
        return hash((self.age, self.first_name, self.last_name, self.position))

    def __str__(self):
        return self.get_name()







