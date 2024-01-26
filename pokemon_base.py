from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """
    Base class representing a generic Pokemon. This class provides a foundation for
    different types of Pokemon with common attributes and behaviors.

    Attributes:
        hp (int): Health points of the Pokemon.
        poke_type (str): Type of the Pokemon ('Fire', 'Water', or 'Grass').
        level (int): Current level of the Pokemon.
        key (int): A sorting key used for team organization based on various attributes.
    """

    def __init__(self, hp: int, poke_type: str) -> None:
        """
        Initialize a new Pokemon with health points and type.

        Args:
            hp (int): Health points of the Pokemon. Must be positive.
            poke_type (str): Type of the Pokemon. Must be one of 'Fire', 'Water', or 'Grass'.

        Raises:
            ValueError: If 'hp' is not positive or 'poke_type' is invalid.

        Complexity:
            Time: O(1)
            Space: O(1)
        """

        if hp <= 0:
            raise ValueError("Pokemon HP must be a positive integer.")
        if poke_type.lower() not in ["fire", "water", "grass"]:
            raise ValueError("Invalid pokemon type. Must be 'Fire', 'Water', or 'Grass'.")

        self.hp = hp
        self.poke_type = poke_type.lower()
        self.level = 1
        self.key = None

    def get_hp(self) -> int:
        """
        Get the health points of the Pokemon.

        Returns:
            int: The current health points of the Pokemon.

        Complexity:
            Time: O(1)
        """
        return self.hp

    def set_hp(self, new_hp: int) -> None:
        """
        Set the health points of the Pokemon.

        Args:
            new_hp (int): The new health points value for the Pokemon. Must be non-negative.

        Complexity:
            Time: O(1)
        """
        if new_hp < 0:
            self.hp = 0
        self.hp = new_hp

    def lose_hp(self, lose_hp: int) -> None:
        """
        Reduce the health points of the Pokemon.

        Args:
            lose_hp (int): The amount by which the Pokemon's health points should be reduced.

        Raises:
            ValueError: If 'lose_hp' is negative.

        Complexity:
            Time: O(1)
        """
        if lose_hp < 0:
            raise ValueError("HP reduction must be non-negative.")

        self.hp = max(self.hp - lose_hp, 0)

    def is_fainted(self) -> bool:
        """
        Check if the Pokemon has fainted (HP is 0 or less).

        Returns:
            bool: True if the Pokemon has fainted, False otherwise.

        Complexity:
            Time: O(1)
        """
        return self.hp <= 0

    def get_level(self) -> int:
        """
        Get the level of the Pokemon.

        Returns:
            int: The current level of the Pokemon.
        Complexity:
            Time: O(1)"""
        return self.level

    def set_level(self, new_level: int) -> None:
        """
        Set the level of the Pokemon.

        Args:
            new_level (int): New level value, must be 1 or greater.

        Raises:
            ValueError: If new_level is less than 1.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        if new_level < 1:
            raise ValueError("Pokemon level must be 1 or greater.")
        self.level = new_level

    def level_up(self, increase_level: int = 1) -> None:
        """
        Increase the level of the Pokemon. Default increment is 1.

        Args:
            increase_level (int): Increment level, must be positive.

        Raises:
            ValueError: If increase_level is not positive.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        if increase_level < 1:
            raise ValueError("Level increase must be positive.")
        self.level += increase_level

    @abstractmethod
    def get_name(self) -> str:
        """Return the name of the Pokemon. Abstract method. Complexity: O(1)"""
        pass

    @abstractmethod
    def get_speed(self) -> int:
        """Return the speed of the Pokemon. Abstract method. Complexity: O(1)"""
        pass

    @abstractmethod
    def get_attack_damage(self, opponent_type: str) -> int:
        """Return the attack damage. Abstract method. Complexity: Depends on implementation."""
        pass

    @abstractmethod
    def is_attacked_by(self, damage_received: int) -> int:
        """Process damage received by the Pokemon. Abstract method. Complexity: Depends on implementation."""
        pass

    def get_poke_type(self) -> str:
        """Return the Pokemon type. Complexity: O(1)"""
        return self.poke_type

    @abstractmethod
    def get_defence(self) -> int:
        """Return the defence of the Pokemon. Abstract method. Complexity: O(1)"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the Pokemon. Abstract method. Complexity: O(1)"""
        pass

    def set_key(self, key: str) -> None:
        """
        Set a sorting key for the Pokemon based on a specified attribute.

        The sorting key is used for organizing Pokemon in a team based on the chosen attribute.
        The key is a composite value calculated from the attribute and the Pokemon's inherent priority.

        Args:
            key (str): A string representing the sorting category.
                       Valid options are 'lvl', 'hp', 'attack', 'defence', 'speed'.

        Raises:
            ValueError: If the key is not one of the valid sorting categories.

        Complexity:
            Time: O(1)
        """
        valid_keys = ["lvl", "hp", "attack", "defence", "speed"]
        if key.lower() not in valid_keys:
            raise ValueError(f"Invalid key. Must be one of {valid_keys}")
        elif key.lower() == "lvl":
            primary_key = self.level
        elif key.lower() == "hp":
            primary_key = self.hp
        elif key.lower() == "attack":
            primary_key = self.get_attack_damage("base")
        elif key.lower() == "defence":
            primary_key = self.get_defence()
        elif key.lower() == "speed":
            primary_key = self.get_speed()

        pokemon_priority_map = {"Charmander": 3, "Bulbasaur": 2, "Squirtle": 1, }
        self.key = (primary_key * 10 + pokemon_priority_map[self.get_name()]) * -1

    def get_key(self) -> int:
        """
        Get the current sorting key of the Pokemon.

        Raise:
            ValueError: If the Pokemon has not been assigned a sorting key.
        Returns:
            int: The sorting key value, used for organizing the Pokemon in a team.

        Complexity:
            Time: O(1)
        """
        if self.key is None:
            raise ValueError("Pokemon has not been assigned a sorting key.")
        return self.key
