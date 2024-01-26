from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    """Charmander Pokemon class, derived from PokemonBase."""

    def __init__(self, hp: int = 7, poke_type: str = "Fire") -> None:
        """
        Initialize a Charmander Pokemon with default or specified HP and type.

        Args:
            hp (int): Health points of the Pokemon. Defaults to 7.
            poke_type (str): Type of the Pokemon. Defaults to 'Fire'.

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
            Space: O(1)
        """
        return self.name

    def get_speed(self) -> int:
        """
        Get the speed of the Pokemon.

        Returns:
            int: The speed of the Pokemon.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return self.speed

    def is_attacked_by(self, damage_received: int) -> None:
        """
        Process the damage received by the Pokemon from an attack.

        Args:
            damage_received (int): The amount of damage received.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        if damage_received > self.defence:
            super().set_hp(self.hp - damage_received)
        else:
            super().set_hp(self.hp - damage_received // 2)

    def get_attack_damage(self, opponent_type: str) -> int:
        """
        Calculate the attack damage based on the opponent's type.

        Args:
            opponent_type (str): The type of the opponent Pokemon.

        Returns:
            int: The calculated attack damage.

        Complexity:
            Time: O(1)
            Space: O(1)
        """

        if opponent_type == "fire":
            type_effectiveness = 1
        elif opponent_type == "water":
            type_effectiveness = 0.5
        elif opponent_type == "grass":
            type_effectiveness = 2
        elif opponent_type == "base":
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
            Space: O(1)
        """
        return self.defence

    def __str__(self) -> str:
        """
        String representation of the Charmander Pokemon.

        Returns:
            str: A formatted string representing the Pokemon's stats.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return f"{self.name}'s HP = {self.hp} and level = {self.level}"


class Bulbasaur(PokemonBase):
    """Bulbasaur Pokemon class, derived from PokemonBase."""

    def __init__(self, hp: int = 9, poke_type: str = "Grass") -> None:
        """
        Initialize a Bulbasaur Pokemon with default or specified HP and type.

        Args:
            hp (int): Health points of the Pokemon. Defaults to 9.
            poke_type (str): Type of the Pokemon. Defaults to 'Grass'.

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
            Space: O(1)
        """
        return self.name

    def get_speed(self) -> int:
        """
        Get the speed of the Pokemon.

        Returns:
            int: The speed of the Pokemon.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return self.speed

    def is_attacked_by(self, damage_received: int) -> None:
        """
        Process the damage received by the Pokemon from an attack.

        Args:
            damage_received (int): The amount of damage received.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        if damage_received > self.defence + 5:
            super().set_hp(self.hp - damage_received)
        else:
            super().set_hp(self.hp - damage_received // 2)

    def get_attack_damage(self, opponent_type: str) -> int:
        """
        Calculate the attack damage based on the opponent's type.

        Args:
            opponent_type (str): The type of the opponent Pokemon.

        Returns:
            int: The calculated attack damage.

        Complexity:
            Time: O(1)
            Space: O(1)
        """

        if opponent_type == "fire":
            type_effectiveness = 0.5
        elif opponent_type == "water":
            type_effectiveness = 2
        elif opponent_type == "grass":
            type_effectiveness = 1
        elif opponent_type == "base":
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
            Space: O(1)
        """
        return self.defence

    def __str__(self) -> str:
        """
        String representation of the Bulbasaur Pokemon.

        Returns:
            str: A formatted string representing the Pokemon's stats.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return f"{self.name}'s HP = {self.hp} and level = {self.level}"


class Squirtle(PokemonBase):
    """Squirtle Pokemon class, derived from PokemonBase."""

    def __init__(self, hp: int = 8, poke_type: str = "Water") -> None:
        """
        Initialize a Squirtle Pokemon with default or specified HP and type.

        Args:
            hp (int): Health points of the Pokemon. Defaults to 8.
            poke_type (str): Type of the Pokemon. Defaults to 'Water'.

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
            Space: O(1)
        """
        return self.name

    def get_speed(self) -> int:
        """
        Get the speed of the Pokemon.

        Returns:
            int: The speed of the Pokemon.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return self.speed

    def is_attacked_by(self, damage_received: int) -> None:
        """
        Process the damage received by the Pokemon from an attack.

        Args:
            damage_received (int): The amount of damage received.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        if damage_received > self.defence * 2:
            super().set_hp(self.hp - damage_received)
        else:
            super().set_hp(self.hp - damage_received // 2)

    def get_attack_damage(self, opponent_type: str) -> int:
        """
        Calculate the attack damage based on the opponent's type.

        Args:
            opponent_type (str): The type of the opponent Pokemon.

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
        elif opponent_type == "base":
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
            Space: O(1)
        """
        return self.defence

    def __str__(self) -> str:
        """
        String representation of the Squirtle Pokemon.

        Returns:
            str: A formatted string representing the Pokemon's stats.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return f"{self.name}'s HP = {self.hp} and level = {self.level}"

