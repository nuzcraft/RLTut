# fighter class, used as a component of Entity


class Fighter:
    # combat related properties and methods (monster, player, NPC)
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, damage):
        # apply damage if possible
        if damage > 0:
            self.hp -= damage

    def attack(self, target):
        # a simple formula for attack damage
        damage = self.power - target.fighter.defense
        if damage > 0:
            # make the target take some damage
            print (self.owner.name.capitalize() + ' attacks ' + target.name +
                   ' for ' + str(damage) + ' hit points.')
            target.fighter.take_damage(damage)
        else:
            print (self.owner.name.capitalize() + ' attacks ' + target.name +
                   ' but it has no effect!')
