import random
from abc import ABC

from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    """
    Charmander Pokemon class, derived from PokemonBase.

    Represents a Charmander, a Fire-type Pokemon, with specific attributes
    like attack damage, defense, and speed.
    """

    def __init__(self, hp: int = 7, poke_type: str = "Fire") -> None:
        """
        Initialize a Charmander Pokemon with specified or default HP and type.

        Args:
            hp (int): Health points of the Charmander. Defaults to 7.
            poke_type (str): Type of the Charmander. Defaults to 'Fire'.
                             Must be one of 'Fire', 'Water', or 'Grass'.

        Raises:
            ValueError: If 'hp' is not positive or 'poke_type' is invalid.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        super().__init__(hp, poke_type)
        self.name = "Charmander"
        self.attack_damage = 6 + self.level
        self.defence = 4
        self.speed = 7 + self.level

    def get_name(self) -> str:
        """
        Get the name of the Pokemon.

        Returns:
            str: The name of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.name

    def get_speed(self) -> int:
        """
        Get the speed attribute of the Charmander.

        Returns:
            int: The current speed of the Charmander.

        Complexity:
            Time: O(1)
        """
        return self.speed

    def is_attacked_by(self, damage_received: int) -> int:
        """
        Process the damage received by the Pokemon from an attack and return the value of the damage.

        Args:
            damage_received (int): The amount of damage received.

        Returns:
            int: The amount of damage received after factoring in the Pokemon's defence.

        Complexity:
            Time: O(1)
        """
        if damage_received > self.defence:
            super().set_hp(self.hp - damage_received)
            return damage_received
        else:
            super().set_hp(self.hp - damage_received // 2)
            return damage_received // 2

    def get_attack_damage(self, opponent_type: str) -> int:
        """
        Calculate the attack damage by Charmander based on the opponent's type.

        Args:
            opponent_type (str): The type of the opponent Pokemon. Valid types are 'fire', 'water', 'grass', and 'base'.

        Returns:
            int: The calculated attack damage after factoring in type effectiveness.

        Raises:
            ValueError: If 'opponent_type' is not a valid Pokemon type.

        Complexity:
            Time: O(1)
        """

        if opponent_type == "fire":
            type_effectiveness = 1
        elif opponent_type == "water":
            type_effectiveness = 0.5
        elif opponent_type == "grass":
            type_effectiveness = 2
        elif opponent_type == "base" or "glitch":
            type_effectiveness = 1
        else:
            raise ValueError("Invalid Pokemon type")
        return round(self.attack_damage * type_effectiveness)

    def get_defence(self) -> int:
        """
        Get the defence value of the Pokemon.

        Returns:
            int: The defence value of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.defence

    def __str__(self) -> str:
        """
        String representation of the Charmander Pokemon.

        Returns:
            str: A formatted string representing the Pokemon's stats.

        Complexity:
            Time: O(1)
        """
        return f"{self.name}'s HP = {self.hp} and level = {self.level}"


class Bulbasaur(PokemonBase):
    """
    Bulbasaur Pokemon class, derived from PokemonBase.

    Represents a Bulbasaur, a Grass-type Pokemon, with attributes such as
    attack damage, defense, and speed.
    """

    def __init__(self, hp: int = 9, poke_type: str = "Grass") -> None:
        """
        Initialize a Bulbasaur Pokemon with specified or default HP and type.

        Args:
            hp (int): Health points of the Bulbasaur. Defaults to 9.
            poke_type (str): Type of the Bulbasaur. Defaults to 'Grass'.
                             Must be one of 'Fire', 'Water', or 'Grass'.

        Raises:
            ValueError: If 'hp' is not positive or 'poke_type' is invalid.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        super().__init__(hp, poke_type)
        self.name = "Bulbasaur"
        self.attack_damage = 5
        self.defence = 5
        self.speed = 7 + self.level // 2

    def get_name(self) -> str:
        """
        Get the name of the Pokemon.

        Returns:
            str: The name of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.name

    def get_speed(self) -> int:
        """
        Get the speed of the Pokemon.

        Returns:
            int: The speed of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.speed

    def is_attacked_by(self, damage_received: int) -> int:
        """
        Process the damage received by the Pokemon from an attack and return the value of the damage.

        Args:
            damage_received (int): The amount of damage received.

        Returns:
            int: The amount of damage received after factoring in the Pokemon's defence.

        Complexity:
            Time: O(1)
        """
        if damage_received > self.defence + 5:
            super().set_hp(self.hp - damage_received)
            return damage_received
        else:
            super().set_hp(self.hp - damage_received // 2)
            return damage_received // 2

    def get_attack_damage(self, opponent_type: str) -> int:
        """
        Calculate the attack damage based on the opponent's type.

        Args:
            opponent_type (str): The type of the opponent Pokemon.

        Raise:
            ValueError: If 'opponent_type' is not a valid Pokemon type.

        Returns:
            int: The calculated attack damage.

        Complexity:
            Time: O(1)
        """

        if opponent_type == "fire":
            type_effectiveness = 0.5
        elif opponent_type == "water":
            type_effectiveness = 2
        elif opponent_type == "grass":
            type_effectiveness = 1
        elif opponent_type == "base" or "glitch":
            type_effectiveness = 1
        else:
            raise ValueError("Invalid Pokemon type")
        return round(self.attack_damage * type_effectiveness)

    def get_defence(self) -> int:
        """
        Get the defence value of the Pokemon.

        Returns:
            int: The defence value of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.defence

    def __str__(self) -> str:
        """
        String representation of the Bulbasaur Pokemon.

        Returns:
            str: A formatted string representing the Pokemon's stats.

        Complexity:
            Time: O(1)
        """
        return f"{self.name}'s HP = {self.hp} and level = {self.level}"


class Squirtle(PokemonBase):
    """
    Squirtle Pokemon class, derived from PokemonBase.

    Represents a Squirtle, a Water-type Pokemon, characterized by specific
    attack damage, defense, and speed attributes.
    """

    def __init__(self, hp: int = 8, poke_type: str = "Water") -> None:
        """
        Initialize a Squirtle Pokemon with specified or default HP and type.

        Args:
            hp (int): Health points of the Squirtle. Defaults to 8.
            poke_type (str): Type of the Squirtle. Defaults to 'Water'.
                             Must be one of 'Fire', 'Water', or 'Grass'.

        Raises:
            ValueError: If 'hp' is not positive or 'poke_type' is invalid.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        super().__init__(hp, poke_type)
        self.name = "Squirtle"
        self.attack_damage = 4 + self.level // 2
        self.defence = 6 + self.level
        self.speed = 7

    def get_name(self) -> str:
        """
        Get the name of the Pokemon.

        Returns:
            str: The name of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.name

    def get_speed(self) -> int:
        """
        Get the speed of the Pokemon.

        Returns:
            int: The speed of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.speed

    def is_attacked_by(self, damage_received: int) -> int:
        """
        Process the damage received by the Pokemon from an attack and return the value of the damage.

        Args:
            damage_received (int): The amount of damage received.

        Returns:
            int: The amount of damage received after factoring in the Pokemon's defence.

        Complexity:
            Time: O(1)
        """
        if damage_received > self.defence * 2:
            super().set_hp(self.hp - damage_received)
            return damage_received
        else:
            super().set_hp(self.hp - damage_received // 2)
            return damage_received // 2

    def get_attack_damage(self, opponent_type: str) -> int:
        """
        Calculate the attack damage based on the opponent's type.

        Args:
            opponent_type (str): The type of the opponent Pokemon.

        Raise:
            ValueError: If 'opponent_type' is not a valid Pokemon type.

        Returns:
            int: The calculated attack damage.

        Complexity:
            Time: O(1)
            Space: O(1)
        """

        if opponent_type == "fire":
            type_effectiveness = 2
        elif opponent_type == "water":
            type_effectiveness = 1
        elif opponent_type == "grass":
            type_effectiveness = 0.5
        elif opponent_type == "base" or "glitch":
            type_effectiveness = 1
        else:
            raise ValueError("Invalid Pokemon type")
        return round(self.attack_damage * type_effectiveness)

    def get_defence(self) -> int:
        """
        Get the defence value of the Pokemon.

        Returns:
            int: The defence value of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.defence

    def __str__(self) -> str:
        """
        String representation of the Squirtle Pokemon.

        Returns:
            str: A formatted string representing the Pokemon's stats.

        Complexity:
            Time: O(1)
        """
        return f"{self.name}'s HP = {self.hp} and level = {self.level}"


class GlitchMon(PokemonBase, ABC):
    """
    GlitchMon Pokemon class, derived from PokemonBase.

    Represents a GlitchMon, a Pokemon with a random type, characterized by specific
    attack damage, defense, and speed attributes.
    """

    def __init__(self, hp: int = 8) -> None:
        """
        Initialize a GlitchMon Pokemon with specified or default HP and type.

        Args:
            hp (int): Health points of the GlitchMon. Defaults to 8.

        Raises:
            ValueError: If 'hp' is not positive or 'poke_type' is invalid.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        super().__init__(hp, "glitch")

    def increase_hp(self) -> None:
        """
        Increase the HP of the Pokemon by 1.

        Complexity:
            Time: O(1)
        """
        super().set_hp(self.hp + 1)

    def superpower(self) -> None:
        """
        Has a random chance to chose one of three effects: increase HP by 1, increase level by 1, or increase both HP
        and level by 1.

        Complexity:
            Time: O(1)
        """
        chance = random.randrange(9)
        if chance <= 2:
            self.increase_hp()
        elif chance <= 5:
            super().level_up()
        else:
            self.increase_hp()
            super().level_up()


class MissingNo(GlitchMon):
    """
    MissingNo Pokemon class, derived from GlitchMon
    """

    def __init__(self, hp: int = 8) -> None:
        """
        Initialize a MissingNo Pokemon with average stats of the other three pokemon.

        Args:
            hp (int): Health points of the MissingNo. Defaults to 8.

        Raises:
            ValueError: If 'hp' is not positive or 'poke_type' is invalid.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        super().__init__(hp)
        self.name = "MissingNo"
        self.speed = 7 * self.level
        self.attack_damage = 5 * self.level
        self.defence = 5 * self.level

    def get_name(self) -> str:
        """
        Get the name of the Pokemon.

        Returns:
            str: The name of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.name

    def get_speed(self) -> int:
        """
        Get the speed of the Pokemon.

        Returns:
            int: The speed of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.speed

    def is_attacked_by(self, damage_received: int) -> int:
        """
        Process the damage received by the Pokemon from an attack and return the value of the damage.
        It has 25% chance of getting a superpower that increases its HP by 1 or level by 1 or both.

        Args:
            damage_received (int): The amount of damage received.

        Returns:
            int: The amount of damage received after factoring in the Pokemon's defence.

        Complexity:
            Time: O(1)
        """

        chance = random.randrange(99)
        if chance <= 25:
            super().superpower()

        if damage_received > self.defence:
            super().set_hp(self.hp - damage_received)
            return damage_received
        else:
            super().set_hp(self.hp - damage_received // 2)
            return damage_received // 2

    def get_attack_damage(self, opponent_type: str) -> int:
        """
        Calculate the attack damage based on the opponent's type.

        Args:
            opponent_type (str): The type of the opponent Pokemon.

        Returns:
            int: The calculated attack damage.

        Complexity:
            Time: O(1)
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
        Get the defence value of the Pokemon.

        Returns:
            int: The defence value of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.defence

    def __str__(self) -> str:
        """
        String representation of the Squirtle Pokemon.

        Returns:
            str: A formatted string representing the Pokemon's stats.

        Complexity:
            Time: O(1)
        """
        return f"{self.name}'s HP = {self.hp} and level = {self.level}"

