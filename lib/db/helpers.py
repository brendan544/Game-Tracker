from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Player, Team

DATABASE_URL = 'sqlite:///game_tracker.db'  

def get_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

def get_team_by_name(session, name):
    return session.query(Team).filter_by(name=name).first()

def get_player_by_name(session, name):
    return session.query(Player).filter_by(name=name).first ()