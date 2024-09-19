from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Sequence


Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, Sequence('player_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    team_id = Column(Integer, ForeignKey('teams.id'))
    
    team = relationship("Team", back_populates="players")
    
    def __repr__(self):
        return f"<Player(id={self.id}, name='{self.name}', age={self.age})>"

class Team(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, Sequence('team_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    
    players = relationship("Player", order_by=Player.id, back_populates="team")
    
    def __repr__(self):
        return f"<Team(id={self.id}, name='{self.name}', city='{self.city}')>"

class Game(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, Sequence('game_id_seq'), primary_key=True)
    date = Column(DateTime, nullable=False)
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    away_team_id = Column(Integer, ForeignKey('teams.id'))
    home_team_score = Column(Integer, nullable=True)
    away_team_score = Column(Integer, nullable=True)
    
    home_team = relationship("Team", foreign_keys=[home_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])
    
    def __repr__(self):
        return (f"<Game(id={self.id}, date='{self.date}', "
                f"home_team_id={self.home_team_id}, away_team_id={self.away_team_id}, "
                f"home_team_score={self.home_team_score}, away_team_score={self.away_team_score})>")