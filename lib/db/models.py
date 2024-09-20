from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Sequence


Base = declarative_base()

class Team(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    players = relationship("Player", back_populates="team")

    @classmethod
    def create(cls, session, name):
        if not name:
            raise ValueError("Team name cannot be empty.")
        team = cls(name=name)
        session.add(team)
        session.commit()
        return team

    @classmethod
    def delete(cls, session, team_id):
        team = session.query(cls).filter_by(id=team_id).first()
        if team:
            session.delete(team)
            session.commit()
            return team
        return None

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, team_id):
        return session.query(cls).filter_by(id=team_id).first()


class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'))

    team = relationship("Team", back_populates="players")

    @classmethod
    def create(cls, session, name, age, team=None):
        if not name:
            raise ValueError("Player name cannot be empty.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        player = cls(name=name, age=age, team=team)
        session.add(player)
        session.commit()
        return player

    @classmethod
    def delete(cls, session, player_id):
        player = session.query(cls).filter_by(id=player_id).first()
        if player:
            session.delete(player)
            session.commit()
            return player
        return None

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, player_id):
        return session.query(cls).filter_by(id=player_id).first()
