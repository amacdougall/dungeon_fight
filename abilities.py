class Ability(object):
    """
    The base class for all abilities, whether action, reaction, or passive.
    """

    def __init__(self, owner):
        """
        Create a new instance of this ability, to belong to the specified owner.
        The owner's attributes or existing abilities may affect the
        functionality of the new ability instance.
        """
        # attributes
        self.owner = owner
        self.name = "No Name"
        self.description = "No description."

class Action(Ability):
    """
    The base class for all abilities which can be directly used by a character.
    """

    def apply_to(target):
        """
        Attempt to apply this ability to the specified target. Subclasses must
        implement this method.
        """
        pass

class Punch(Action):
    def __init__(self, owner):
        Action.__init__(self, owner)
        self.name = "Punch"
        self.description = "The original unarmed combat move."
        self.damage_min = owner.attack_power * 10
        self.damage_max = self.damage_min + owner.attack_power

    def apply_to(target):
        damage = random.randint(self.damage_min, self.damage_max)
        target.hit_points -= damage
        print "Punch dealt {damage} damage, leaving target with {health} \
                health.".format(damage=damage, health=target.hit_points)
