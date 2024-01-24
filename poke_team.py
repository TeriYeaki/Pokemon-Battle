from pokemon import Charmander, Bulbasaur, Squirtle
from pokemon_base import PokemonBase
from array_sorted_list import ArraySortedList
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from sorted_list import ListItem


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

        total_pokemon = charm + bulb + squir
        if self.battle_mode == 0:
            self.team = ArrayStack(total_pokemon)
            if squir > 0:
                for _ in range(squir):
                    self.team.push(Squirtle())
            if bulb > 0:
                for _ in range(bulb):
                    self.team.push(Bulbasaur())
            if charm > 0:
                for _ in range(charm):
                    self.team.push(Charmander())

        if self.battle_mode == 1:
            self.team = CircularQueue(total_pokemon)
            if charm > 0:
                for _ in range(charm):
                    self.team.append(Charmander())
            if bulb > 0:
                for _ in range(bulb):
                    self.team.append(Bulbasaur())
            if squir > 0:
                for _ in range(squir):
                    self.team.append(Squirtle())

        if self.battle_mode == 2:
            self.team = ArraySortedList(total_pokemon)
            if charm > 0:
                for _ in range(charm):
                    charmander = Charmander()
                    charmander.set_key(self.criterion)
                    self.team.add(ListItem(charmander, charmander.get_key()))
            if bulb > 0:
                for _ in range(bulb):
                    bulbasaur = Bulbasaur()
                    bulbasaur.set_key(self.criterion)
                    self.team.add(ListItem(bulbasaur, bulbasaur.get_key()))
            if squir > 0:
                for _ in range(squir):
                    squirtle = Squirtle()
                    squirtle.set_key(self.criterion)
                    self.team.add(ListItem(squirtle, squirtle.get_key()))

    def get_fighter(self) -> PokemonBase:
        """Retrieve the fighter from the team"""
        if self.battle_mode == 0:
            return self.team.pop()
        elif self.battle_mode == 1:
            return self.team.serve()
        elif self.battle_mode == 2:
            fighter_item = self.team.delete_at_index(0)
            return fighter_item.value
        else:
            raise ValueError("Invalid battle mode. Please input integer 0, 1, or 2.")

    def return_fighter(self, fighter: PokemonBase) -> None:
        """Return fighter back to the team based on the team data structure"""
        if self.battle_mode == 0:
            self.team.push(fighter)
        if self.battle_mode == 1:
            self.team.append(fighter)
        elif self.battle_mode == 2:
            self.team.add(ListItem(fighter, fighter.get_key()))
        else:
            raise ValueError("Invalid battle mode. Please input integer 0, 1, or 2.")

    def __str__(self) -> str:
        """Print the string details of team based on the team data structure"""

        if self.team.is_empty():
            return "No Pokemon in team."

        if self.team is None:
            return "Pokemon team is not initialised."

        member_details = []

        if self.battle_mode == 0:
            # create temp array to store the member after popping
            temp_array = ArrayStack(len(self.team))
            # pop the member and get info then push to temp array
            while not self.team.is_empty():
                pokemon = self.team.pop()
                member_details.append(str(pokemon))
                temp_array.push(pokemon)
            # push the member back into the team array
            while not temp_array.is_empty():
                self.team.push(temp_array.pop())
            # reverse the order of the member details
            member_details.reverse()

        elif self.battle_mode == 1:
            # create temp queue to store the member after serving
            temp_queue = CircularQueue(len(self.team))
            # serve the member and get info then append to temp queue
            while not self.team.is_empty():
                pokemon = self.team.serve()
                member_details.append(str(pokemon))
                temp_queue.append(pokemon)
            # append the member back into the team queue
            while not temp_queue.is_empty():
                self.team.append(temp_queue.serve())

        elif self.battle_mode == 2:
            # get the member info from the team
            for index in range(len(self.team)):
                member_details.append(str(self.team[index]))

        return ", ".join(member_details) + "\n"
