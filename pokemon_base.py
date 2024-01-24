from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """Base Class for Creating a New Pokemon"""

    def __init__(self, hp: int, poke_type: str) -> None:
        """
        Initialize a new Pokemon with health points and type.

        Args:
            hp (int): Health points of the Pokemon, must be positive.
            poke_type (str): Type of the Pokemon, must be 'Fire', 'Water', or 'Grass'.

        Raises:
            ValueError: If hp is not positive or poke_type is invalid.

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
        """Return the HP of the Pokemon. Complexity: O(1)"""
        return self.hp

    def set_hp(self, new_hp: int) -> None:
        """
        Set the HP of the Pokemon.

        Args:
            new_hp (int): New HP value, must be non-negative.

        Raises:
            ValueError: If new_hp is negative.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        if new_hp < 0:
            raise ValueError("New HP must be non-negative.")
        self.hp = new_hp

    def lose_hp(self, lose_hp: int) -> None:
        """
        Reduces the Pokemon's HP.

        Args:
            lose_hp (int): The amount of HP to be reduced.

        Raises:
            ValueError: If lose_hp is negative.

        Complexity:
            Time: O(1)
            Space: O(1)
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
            Space: O(1)
        """
        return self.hp <= 0

    def get_level(self) -> int:
        """Return the level of the Pokemon. Complexity: O(1)"""
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
    def is_attacked_by(self, damage_received: int) -> None:
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
        Sets a key for sorting the Pokemon team based on various attributes.

        Args:
            key (str): A string representing the sorting category (e.g., 'lvl', 'hp').

        Raises:
            ValueError: If the key is not a valid sorting category.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        valid_keys = ["lvl", "hp", "attack", "defence", "speed"]
        key = key.lower()

        if key not in valid_keys:
            raise ValueError(f"Invalid key. Must be one of {valid_keys}")

        # Set the key based on the category
        self.key = getattr(self, f"get_{key}")()

    def get_key(self) -> int:
        """
        Returns the key used for sorting.

        Returns:
            int: The sorting key value.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return self.key
