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
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.id, State.name, City.id, City.name).join(City).order_by(State.id, City.id)

    for state_id, state_name, city_id, city_name in query:
        print(f"{state_id}: {state_name}")
        print(f"\t{city_id}: {city_name}")
    session.close()
