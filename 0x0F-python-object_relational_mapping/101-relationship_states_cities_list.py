#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects, contained in...
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine_url = "mysql+mysqldb://" + username + ":" + password + \
        "@localhost:3306/" + db_name
    engine = create_engine(engine_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
 
    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
