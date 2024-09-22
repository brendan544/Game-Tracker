# GAME TRACKER HUB
This CLI application allows you to track and manage sporting activities by keeping records of players and teams. Built with Python and SQLAlchemy, it provides a simple menu-driven interface for various operations.

## Features
Add Players: Create new player records with name, age, and optionally assign them to a team.
Add Teams: Create new team records.
Delete Players/Teams: Remove players or teams from the database.
List Players/Teams: Display all players or teams currently in the database.
Find Players/Teams by ID: Retrieve details of a player or team using their unique identifier.
## Requirements
Python 3.x
SQLAlchemy
SQLite (built-in with Python)
Installation
Clone the repository:



git clone <https://github.com/brendan544/Game-tracker.git>
cd game-tracker
## Install dependencies:

pip install sqlalchemy
Create the database: Run the following command to create the SQLite database:



python -c "from create_database import create_database; create_database()"

To start the application, run:



python main.py
## Menu Options
1: Add Player
2: Add Team
3: Delete Player
4: Delete Team
5: List Players
6: List Teams
7: Find Player by ID
8: Find Team by ID
9: Exit
## Example
To add a player:
mathematica

Choose an option: 1
Enter player name: Alice
Enter player age: 25
Enter team ID (or leave blank for none): 1
## Database Schema
The application uses a simple schema with two tables:

 Teams:

id: Integer, primary key
name: String, team name
Players:

id: Integer, primary key
name: String, player name
age: Integer, player age
team_id: Integer, foreign key referencing teams
Seeding Data
You can seed the database with initial data by running:



python seed_data.py
Contributing
Feel free to fork the repository, make changes, and submit a pull request. Any contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

