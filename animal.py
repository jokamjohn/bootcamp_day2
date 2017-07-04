class Animal:
    """
    A base animal class
    """
    animal_type = ''
    num_of_legs = 4
    sound = 'roar'
    num_of_horns = 0

    def __str__(self):
        """Return the string representation of the class"""
        return "A {} with {} legs makes a {} sound.".format(self.__class__.__name__,
                                                            self.num_of_legs,
                                                            self.sound)

    def make_sound(self):
        """Return the sound the animal makes three times"""
        return self.sound.upper() * 2

    def has_horns(self):
        """Returns boolean if the animal has horns"""
        if self.num_of_horns > 0:
            return True
        else:
            return False

    def has_legs(self):
        """Returns boolean if the animal has legs"""
        if self.num_of_legs > 0:
            return True
        else:
            return False

    def move(self):
        return "It is walking"


class Horse(Animal):
    """A Horse class inheriting from Animal and overriding animal type and sound"""
    animal_type = 'Horse'
    sound = 'neigh neigh '


class Snake(Animal):
    """A snake class class inheriting from Animal overriding animal type,sound and number of legs"""
    animal_type = 'Snake'
    sound = 'hiss '
    num_of_legs = 0


class Cow(Animal):
    """A Cow class inheriting from Animal and overriding animal type and sound"""
    animal_type = 'Cow'
    sound = 'mow '
