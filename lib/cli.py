import argparse
from repository import add_player, add_team, delete_player, delete_team, list_players, list_teams
from sqlalchemy.orm import sessionmaker
from models import Base
from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///game_tracker.db'  # Adjust as needed

def create_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

def display_menu():
    print("\nGame Tracker CLI")
    print("1. Create Database")
    print("2. Add Player")
    print("3. Add Team")
    print("4. Delete Player")
    print("5. Delete Team")
    print("6. List Players")
    print("7. List Teams")
    print("8. Exit")

def main():
    create_db()  # Ensure the database is created at the start
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            create_db()
            print("Database created.")
        elif choice == '2':
            name = input("Enter player's name: ")
            age = int(input("Enter player's age: "))
            team_name = input("Enter team name: ")
            add_player(name, age, team_name)
        elif choice == '3':
            name = input("Enter team name: ")
            add_team(name)
        elif choice == '4':
            player_id = int(input("Enter player ID to delete: "))
            delete_player(player_id)
        elif choice == '5':
            team_id = int(input("Enter team ID to delete: "))
            delete_team(team_id)
        elif choice == '6':
            list_players()
        elif choice == '7':
            list_teams()
        elif choice == '8':
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
