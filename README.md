# Pokemon-Battle

## Project Overview 🚀
Pokemon-Battle is a console-based game developed as a university assignment, aimed at demonstrating the practical usage 
of Abstract Data Types (ADTs) in building engaging applications. The game allows players to engage in battles using 
classic Pokémon characters, leveraging various ADTs for efficient gameplay management.

## Technologies 🛠️
- **Python**: `Python 3.x`

## Development Process 🖥️
- **Base Class Creation**: Developed Pokemon_base.py as the foundation for Pokémon objects, defining common methods and 
abstract methods for specialization in child classes.
- **Child Class Development**: Implemented child classes for Charmander, Squirtle, and Bulbasaur in pokemon.py, 
providing players with initial Pokémon choices.
- **Team Management**: Created pokemon_team.py to manage player teams, including functionalities for team composition 
and ADT-based team selection.
- **Battle Mechanics**: Developed battle.py to handle the game's battle logic, offering three distinct battle modes: 
set mode, rotating mode, and optimized mode.
- **Add Additional Pokemon**: Extend to add a new type of pokemon to the game that is a different type from the existing
ones with special ability.

## Learning Outcomes 🧠
- **Class Inheritance and OOP Principles**: Gained proficiency in using class inheritance, abstract methods, super() 
method, and static methods for efficient and cleaner code.
- **Abstract Data Types (ADTs)**: Enhanced understanding of choosing appropriate ADTs for different data structures, 
leading to better data management.
- **Encapsulation**: Implemented encapsulation to protect data integrity, using private attributes and methods.
- **Clean Code Practices**: Improved code readability and maintenance by adhering to the Single Responsibility 
Principle, ensuring each class and method has a focused purpose.

## Proposed Improvements 💭
### Within Project Scope
- **Enhanced Battle Statistics**: Implement helper methods in the battle class for more effective round statistics 
display.
- **Refined Attack Process**: Separate attack processing and damage calculation for clearer code responsibility.
- **Universal Team Assignment**: Develop helper methods for team assignment applicable across all battle modes, reducing
code redundancy.
### Future Enhancements
- **Expanded Pokémon Roster**: Introduce more Pokémon options for varied gameplay.
- **Additional Battle Modes**: Implement new battle modes for enhanced player experience.
- **Interactive Attack Selection**: Allow players to choose Pokémon for subsequent attacks, increasing user engagement.
- **Richer User Feedback**: Provide detailed battle feedback, like HP status after attacks, for a more immersive 
experience.
- **Display Management**: Create a separate class for output handling (CLI or GUI) to decouple game logic from display, 
improving code readability and maintainability.

## Getting Started 🚦
- You can `fork` the repository to your GitHub account or `clone` it directly to your local machine. Once you have a copy 
of the project, you can run it locally on your machine. 

- The project does not have a file to run the game, as it only stores the logic of the game. The entry point of the game
is the `battle.py` class. Please create a new `Battle (trainer_one_name: str, trainer_two_name: str)` object and then 
either `set_mode_battle()`, `rotating_mode_battle()`, or `optimized_mode_battle()` to start the game in desired mode. 

## Contributions
As this is a university assignment, multiple students had contributed to the project which I have derived from and 
improved upon. To protect the integrity of the assignment and the students' privacy, the names of the contributors 
will not be disclosed.
