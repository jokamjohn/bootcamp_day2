class Animal:
    """
    A base animal class
    """
    animal_type = ''
    num_of_legs = 4
    sound = 'roar'
    num_of_horns = 0

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
