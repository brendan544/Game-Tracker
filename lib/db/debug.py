import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player, Team, Game

DATABASE_URL = 'sqlite:///game_tracker.db' 

def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def log_db_state():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    players = session.query(Player).all()
    teams = session.query(Team).all()
    games = session.query(Game).all()

    logging.debug(f"Players: {players}")
    logging.debug(f"Teams: {teams}")
    logging.debug(f"Games: {games}")

    session.close()

if __name__ == "__main__":
    setup_logging()
    log_db_state()