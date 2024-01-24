from poke_team import PokeTeam
from pokemon_base import PokemonBase


class Battle:
    """Pokemon Battle Class"""

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        """Create a pokemon battle between two trainers"""
        self.trainer1 = PokeTeam(trainer_one_name)
        self.trainer2 = PokeTeam(trainer_two_name)
        self.winner = None

    def set_mode_battle(self) -> str:
        """Set the default mode for the pokemon battle"""
        return self.start_battle(0)

    def rotating_mode_battle(self) -> str:
        """Set the rotating mode for the pokemon battle"""
        return self.start_battle(1)

    def start_battle(self, battle_mode: int) -> str:
        """Begin battle sequence"""

        # Validate team composition
        if self.trainer1.get_team() is None or self.trainer2.get_team() is None:
            raise ValueError("Teams are not properly initialized.")

        # validate battle mode
        if battle_mode not in [0, 1, 2]:
            raise ValueError("Invalid battle mode. Please select 0, 1, or 2")

        # initiate battle mode
        self.trainer1.choose_team(battle_mode)
        self.trainer2.choose_team(battle_mode)
        round_num = 1

        # continue the fight until all pokemon from one team is fainted
        while True:

            # set the battle ending condition
            if self.trainer1.is_empty() and self.trainer2.is_empty():
                return "Battle ended: It's a draw."
            elif self.trainer1.is_empty():
                return f"Battle ended: {self.trainer2.get_name()} wins."
            elif self.trainer2.is_empty():
                return f"Battle ended: {self.trainer1.get_name()} wins."

            # Assign current round fighter
            t1_pokemon = self.trainer1.get_fighter()
            t2_pokemon = self.trainer2.get_fighter()
            # Check if pokemon exist before fighting
            if not t1_pokemon or not t2_pokemon:
                raise ValueError("One or both teams have run out of Pokemon unexpectedly.")

            # Fight Battle
            if t1_pokemon.get_speed() == t2_pokemon.get_speed():
                self._perform_attack(t1_pokemon, t2_pokemon)
                self._perform_attack(t2_pokemon, t1_pokemon)
            elif t1_pokemon.get_speed() > t2_pokemon.get_speed():
                self._perform_attack(t1_pokemon, t2_pokemon)
                if not t2_pokemon.is_fainted():
                    self._perform_attack(t2_pokemon, t1_pokemon)
            else:
                self._perform_attack(t2_pokemon, t1_pokemon)
                if not t1_pokemon.is_fainted():
                    self._perform_attack(t1_pokemon, t2_pokemon)

            # Both lose 1 hp if both are still alive
            if not t1_pokemon.is_fainted() and not t2_pokemon.is_fainted():
                t1_pokemon.lose_hp(1)
                t2_pokemon.lose_hp(1)

            # Process the battle aftermath
            if not t1_pokemon.is_fainted() and not t2_pokemon.is_fainted():
                self._pokemon_lvlup_and_return(t1_pokemon, self.trainer1)
                self._pokemon_lvlup_and_return(t2_pokemon, self.trainer2)
                print(
                    f"Round {round_num}: {self.trainer1.get_name()}'s {t1_pokemon.get_name()} attack " +
                    f"{self.trainer2.get_name()}'s {t2_pokemon.get_name()} and they and both live")
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
    def _perform_attack(attacker: PokemonBase, defender: PokemonBase) -> None:
        """Get the attack damage and process the attack"""
        try:
            attack_damage = attacker.get_attack_damage(defender.get_poke_type())
            defender.is_attacked_by(attack_damage)
        except Exception as e:
            print(f"An error occurred during attack: {e}")

    @staticmethod
    def _pokemon_lvlup_and_return(pokemon: PokemonBase, team: PokeTeam) -> None:
        """Level up the pokemon and return it back to the team"""
        try:
            pokemon.level_up()
            team.return_fighter(pokemon)
        except Exception as e:
            print(f"An error occurred during pokemon level up and return to team: {e}")

