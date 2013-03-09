from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from settings import SQLALCHEMY_DB_URI

db = create_engine(SQLALCHEMY_DB_URI)
Session = sessionmaker(bind=db)
Base = declarative_base()

player_game_table = Table('player_game', Base.metadata,
	Column('player_id', Integer, ForeignKey('player.id')),
	Column('game_id', Integer, ForeignKey('game.id')))

class Player(Base):
	__tablename__ = 'player'

	id = Column(Integer, primary_key=True)
	name = Column(String(80))
	spy_wins = Column(Integer)
	spy_losses = Column(Integer)
	resistance_wins = Column(Integer)
	resistance_losses = Column(Integer)

	games = relationship("Game",
		secondary=player_game_table,
		backref="players")

class Game(Base):
	__tablename__ = 'game'

	id = Column(Integer, primary_key=True)
	num_players = Column(Integer)
	date = Column(Date)
	resistance_rounds = Column(Integer)
	spy_rounds = Column(Integer)
