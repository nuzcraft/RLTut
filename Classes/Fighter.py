# fighter class, used as a component of Entity
from helpers.message import message
from helpers.yield_experience import yield_experience
from helpers.get_all_equipped import get_all_equipped


class Fighter:
    # combat related properties and methods (monster, player, NPC)
    def __init__(self, hp, defense, power, xp, death_function=None):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.xp = xp
        self.death_function = death_function

    @property
    def power(self):
        bonus = sum(equipment.power_bonus for equipment in get_all_equipped(self.owner))
        return self.base_power + bonus

    @property
    def defense(self):
        bonus = sum(equipment.defense_bonus for equipment in get_all_equipped(self.owner))
        return self.base_defense + bonus

    @property
    def max_hp(self):
        bonus = sum(equipment.max_hp_bonus for equipment in get_all_equipped(self.owner))
        return self.base_max_hp + bonus

    def take_damage(self, damage):
        # apply damage if possible
        if damage > 0:
            self.hp -= damage
        if self.hp <= 0:
            function = self.death_function
            if function is not None:
                function(self.owner)
            yield_experience(self)

    def attack(self, target):
        # a simple formula for attack damage
        damage = self.power - target.fighter.defense
        if damage > 0:
            # make the target take some damage
            message(self.owner.name.capitalize() + ' attacks ' + target.name +
                    ' for ' + str(damage) + ' hit points.')
            target.fighter.take_damage(damage)
        else:
            message(self.owner.name.capitalize() + ' attacks ' + target.name +
                    ' but it has no effect!')

    def heal(self, amount):
        # heal by the given amount, without going over max
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
