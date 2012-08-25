class Character(object):
    """
    The base class for all characters, both player and monster, in the game.
    """

    def __init__(self):
        # attributes
        self.name = "No Name"
        self.class_template = None

        self.level = 0
        self.hit_points_max = 0
        self.hit_points = 0
        self.magic_points_max = 0
        self.magic_points = 0
        self.rage_points_max = 0
        self.rage_points = 0

        self.attack_power = 0

        self.effects = []  # buffs/debuffs

        self.abilities = {
            "action": [],
            "reaction": [],
            "passive": [],
        }

    def action(name, target):
        if name in self.abilities["action"]:
            self.abilities["action"][name].apply_to(target)
        else:
            raise "{0} has no action ability named {1}".format(self.name, name)
