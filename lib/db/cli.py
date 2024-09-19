import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Player, Team

DATABASE_URL = 'sqlite:///game_tracker.db'  # Adjust as needed

def create_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

def display_menu():
    print("\nGame Tracker CLI")
    print("1. Add Player")
    print("2. Add Team")
    print("3. Delete Player")
    print("4. Delete Team")
    print("5. List Players")
    print("6. List Teams")
    print("7. Find Player by ID")
    print("8. Find Team by ID")
    print("9. Exit")

def add_player(session):
    name = input("Enter player name: ")
    age = int(input("Enter player age: "))
    team_id = int(input("Enter team ID (or leave blank for none): ") or 0)

    team = session.query(Team).filter_by(id=team_id).first() if team_id else None

    try:
        player = Player.create(session, name, age, team)
        print(f"Player {player.name} added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def add_team(session):
    name = input("Enter team name: ")

    try:
        team = Team.create(session, name)
        print(f"Team {team.name} added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_player(session):
    player_id = int(input("Enter player ID to delete: "))
    player = Player.delete(session, player_id)
    if player:
        print(f"Player {player.name} deleted successfully.")
    else:
        print("Player not found.")

def delete_team(session):
    team_id = int(input("Enter team ID to delete: "))
    team = Team.delete(session, team_id)
    if team:
        print(f"Team {team.name} deleted successfully.")
    else:
        print("Team not found.")

def list_players(session):
    players = Player.get_all(session)
    for player in players:
        print(f"ID: {player.id}, Name: {player.name}, Age: {player.age}, Team ID: {player.team_id}")

def list_teams(session):
    teams = Team.get_all(session)
    for team in teams:
        print(f"ID: {team.id}, Name: {team.name}")

def find_player_by_id(session):
    player_id = int(input("Enter player ID to find: "))
    player = Player.find_by_id(session, player_id)
    if player:
        print(f"Found Player: ID: {player.id}, Name: {player.name}, Age: {player.age}, Team ID: {player.team_id}")
    else:
        print("Player not found.")

def find_team_by_id(session):
    team_id = int(input("Enter team ID to find: "))
    team = Team.find_by_id(session, team_id)
    if team:
        print(f"Found Team: ID: {team.id}, Name: {team.name}")
    else:
        print("Team not found.")

def main():
    create_db()
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_player(session)
        elif choice == '2':
            add_team(session)
        elif choice == '3':
            delete_player(session)
        elif choice == '4':
            delete_team(session)
        elif choice == '5':
            list_players(session)
        elif choice == '6':
            list_teams(session)
        elif choice == '7':
            find_player_by_id(session)
        elif choice == '8':
            find_team_by_id(session)
        elif choice == '9':
            print("Exiting...")
            session.close()
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()