from poke_team import PokeTeam
from pokemon_base import PokemonBase


class Battle:
    """
    A class representing a Pokemon battle between two trainers.

    Manages the entire battle process, including different battle modes,
    and handling the outcome of each battle round.
    """

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        """
        Initialize a Pokemon battle between two trainers.

        Args:
            trainer_one_name (str): Name of the first trainer.
            trainer_two_name (str): Name of the second trainer.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        self.trainer1 = PokeTeam(trainer_one_name)
        self.trainer2 = PokeTeam(trainer_two_name)

    def set_mode_battle(self) -> str:
        """
        Initiate a battle in the default mode (mode 0).

        Returns:
            str: The name of the winning trainer or 'Draw'.

        Complexity:
            Time: O(N) - Depends on the number of rounds.
        """
        return self._start_battle(0)

    def rotating_mode_battle(self) -> str:
        """
        Initiate a battle in rotating mode (mode 1).

        Returns:
            str: The name of the winning trainer or 'Draw'.

        Complexity:
            Time: O(N) - Depends on the number of rounds.
        """
        return self._start_battle(1)

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """
        Initiate a battle in optimised mode (mode 2) based on a chosen attribute.

        Args:
            criterion_team1 (str): The chosen attribute for sorting team 1.
            criterion_team2 (str): The chosen attribute for sorting team 2.

        Returns:
            str: The name of the winning trainer or 'Draw'.

        Complexity:
            Time: O(N) - Depends on the number of rounds.
        """
        return self._start_battle(2, criterion_team1, criterion_team2)

    def _start_battle(self, battle_mode: int, criterion_team1: str = None, criterion_team2: str = None) -> str:
        """
        Begin the battle sequence. It initiates the selected battle mode and start the round. It then begins by checking
        if the winning condition is met. If not, it will continue the rounds and repeat until the winning condition is
        met. First, it will get and assign current round fighter. Then, it will fight the battle. Finally, it will
        process the battle after math.

        Args:
            battle_mode (int): The chosen battle mode (0, 1, or 2).
            criterion_team1 (str, optional): Sorting criterion for team 1 in optimised mode.
            criterion_team2 (str, optional): Sorting criterion for team 2 in optimised mode.

        Returns:
            str: The name of the winning trainer or 'Draw'.

        Raises:
            ValueError: If an invalid battle mode is selected or teams are not properly initialized.

        Complexity:
            Time: O(N) - Depends on the number of rounds and battle mode.
        """

        # validate battle mode
        if battle_mode not in [0, 1, 2]:
            raise ValueError("Invalid battle mode. Please select 0, 1, or 2")

        # initiate battle mode
        self.trainer1.choose_team(battle_mode, criterion_team1)
        self.trainer2.choose_team(battle_mode, criterion_team2)
        round_num = 1

        # Validate team composition
        if self.trainer1.get_team() is None or self.trainer2.get_team() is None:
            raise ValueError("Teams are not properly initialized.")

        # continue the fight until all pokemon from one team is fainted
        while True:

            # Activate glitchmon if team is empty
            if self.trainer1.is_empty() and self.trainer1.have_glitchmon():
                self.trainer1.activate_glitchmon()
            if self.trainer2.is_empty() and self.trainer2.have_glitchmon():
                self.trainer2.activate_glitchmon()

            # set the battle ending condition
            if self.trainer1.is_empty() and self.trainer2.is_empty():
                return "Draw"
            elif self.trainer1.is_empty():
                return self.trainer2.get_name()
            elif self.trainer2.is_empty():
                return self.trainer1.get_name()

            # Assign current round fighter
            t1_pokemon = self.trainer1.get_fighter()
            t2_pokemon = self.trainer2.get_fighter()
            # Check if pokemon exist before fighting
            if not t1_pokemon or not t2_pokemon:
                raise ValueError("One or both teams have run out of Pokemon unexpectedly.")

            # Fight Battle
            if t1_pokemon.get_speed() == t2_pokemon.get_speed():
                t1_final_damage = self._perform_attack(t1_pokemon, t2_pokemon)
                t2_final_damage = self._perform_attack(t2_pokemon, t1_pokemon)
            elif t1_pokemon.get_speed() > t2_pokemon.get_speed():
                t1_final_damage = self._perform_attack(t1_pokemon, t2_pokemon)
                if not t2_pokemon.is_fainted():
                    t2_final_damage = self._perform_attack(t2_pokemon, t1_pokemon)
            else:
                t2_final_damage = self._perform_attack(t2_pokemon, t1_pokemon)
                if not t1_pokemon.is_fainted():
                    t1_final_damage = self._perform_attack(t1_pokemon, t2_pokemon)

            # Both lose 1 hp if both are still alive
            if not t1_pokemon.is_fainted() and not t2_pokemon.is_fainted():
                t1_pokemon.lose_hp(1)
                t2_pokemon.lose_hp(1)

            # Process the battle aftermath
            if not t1_pokemon.is_fainted() and not t2_pokemon.is_fainted():
                self.trainer1.return_fighter(t1_pokemon)
                self.trainer2.return_fighter(t2_pokemon)
                print(
                    f"Round {round_num}: {self.trainer1.get_name()}'s {t1_pokemon.get_name()} attack " +
                    f"{self.trainer2.get_name()}'s {t2_pokemon.get_name()} and loses {t2_final_damage} HP while" +
                    f" {self.trainer2.get_name()}'s {t2_pokemon.get_name()} loses {t1_final_damage} HP")
            elif t1_pokemon.is_fainted():
                self._pokemon_lvlup_and_return(t2_pokemon, self.trainer2)
                print(
                    f"Round {round_num}: {self.trainer1.get_name()}'s {t1_pokemon.get_name()} is " +
                    f"fainted by {self.trainer2.get_name()}'s {t2_pokemon.get_name()}")
            elif t2_pokemon.is_fainted():
                self._pokemon_lvlup_and_return(t1_pokemon, self.trainer1)
                print(f"Round {round_num}: {self.trainer1.get_name()}'s {t1_pokemon.get_name()} faints " +
                      f"{self.trainer2.get_name()}'s {t2_pokemon.get_name()}")

            round_num += 1

    @staticmethod
    def _perform_attack(attacker: PokemonBase, defender: PokemonBase) -> int:
        """
        Calculate and apply the attack damage from one Pokemon to another.

        Args:
            attacker (PokemonBase): The attacking Pokemon.
            defender (PokemonBase): The defending Pokemon.

        Returns:
            int: The amount of damage inflicted.

        Raises:
            Exception: If an error occurs during the attack.

        Complexity:
            Time: O(1)
        """

        try:
            attack_damage = attacker.get_attack_damage(defender.get_poke_type())
            return defender.is_attacked_by(attack_damage)
        except Exception as e:
            raise Exception(f"An error occurred during attack: {e}")

    @staticmethod
    def _pokemon_lvlup_and_return(pokemon: PokemonBase, team: PokeTeam) -> None:
        """
        Level up a Pokemon and return it to its team.

        Args:
            pokemon (PokemonBase): The Pokemon to level up.
            team (PokeTeam): The team to which the Pokemon belongs.

        Raises:
            Exception: If an error occurs during leveling up or returning the Pokemon.

        Complexity:
            Time: O(1)
        """
        try:
            pokemon.level_up()
            team.return_fighter(pokemon)
        except Exception as e:
            print(f"An error occurred during pokemon level up and return to team: {e}")

