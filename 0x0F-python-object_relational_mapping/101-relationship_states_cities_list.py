#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from relationship_state import Base, State


if __name__ == "__main__":

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(engine_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State):
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))
    session.close()
