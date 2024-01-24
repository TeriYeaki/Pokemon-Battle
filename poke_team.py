from pokemon_base import PokemonBase


class PokeTeam:
    """Pokemon battle team class"""
    LIMIT = 6

    def __init__(self, trainer_name: str) -> None:
        """Create a pokemon battle team with trainer and 6 pokemon"""
        self.trainer_name = trainer_name
        self.battle_mode = 0
        self.criterion = None
        self.team = None

    def get_name(self) -> str:
        """Get the trainer name of the pokemon battle team"""
        return self.trainer_name

    def get_team(self):
        """Get battle team"""
        return self.team

    def is_empty(self) -> bool:
        """Check if the team is empty"""
        return self.team.is_empty()

    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """
        Select the Pokemon for the battle team based on user input.

        Args:
            battle_mode (int): The battle mode of the team (0, 1, or 2).
            criterion (str, optional): The criterion for team selection. Defaults to None.

        Raises:
            ValueError: If the battle_mode is invalid.
            ValueError: If the criterion is invalid.
        """
        if battle_mode not in [0, 1, 2]:
            raise ValueError("Invalid battle mode. Please input integer 0, 1, or 2.")

        if criterion not in ["lvl", "hp", "attack", "defence", "speed", None]:
            raise ValueError("Invalid criterion. Please input lvl, hp, attack, defence, or speed")

        self.battle_mode = battle_mode
        self.criterion = criterion

        valid_input = False
        while not valid_input:
            try:
                # Ask for input
                team_input = input(f"Howdy {self.trainer_name}! Choose your team as C B S\n"
                                   "where C is the number of Charmanders, "
                                   "      B is the number of Bulbasaurs, "
                                   "      S is the number of Squirtles\n> ").strip()

                # Parse and validate input
                charmanders, bulbasaurs, squirtles = map(int, team_input.split())
                if charmanders < 0 or bulbasaurs < 0 or squirtles < 0:
                    print("Invalid input. Numbers must be non-negative.")
                    continue

                total_pokemon = charmanders + bulbasaurs + squirtles
                if self.LIMIT >= total_pokemon > 0:
                    valid_input = True
                else:
                    print(f"Invalid input. Total number of Pokemon must be between 1 and {self.LIMIT}.\n")
            except (ValueError, TypeError):
                print("Invalid input. Please enter three integers separated by spaces.\n")

        self.assign_team(charmanders, bulbasaurs, squirtles)

    def assign_team(self, charm: int, bulb: int, squir: int) -> None:
        """Populates the team based on the ADT that is chosen for the battle mode"""

        pass

    def get_fighter(self) -> PokemonBase:
        """Retrieve the fighter from the team"""
        if self.battle_mode == 0:
            return self.team.pop()
        else:
            raise ValueError("Invalid battle mode. Please input integer 0, 1, or 2.")

    def return_fighter(self, fighter: PokemonBase) -> None:
        """Return fighter back to the team based on the team data structure"""
        if self.battle_mode == 0:
            self.team.push(fighter)
        else:
            raise ValueError("Invalid battle mode. Please input integer 0, 1, or 2.")

    def __str__(self) -> str:
        """Print the string details of team based on the team data structure"""

        pass
