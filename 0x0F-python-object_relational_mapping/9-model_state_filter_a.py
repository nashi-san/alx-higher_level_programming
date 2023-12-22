#!/usr/bin/python3
"""
Lists all State objects that contain the letter "a"
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine_url = "mysql+mysqldb://" + username + ":" + password + \
        "@localhost:3306/" + db_name
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State)\
        .filter(State.name.like("%a%"))\
        .order_by(State.id)\
        .all()

    if not states_with_a:
        print("Nothing")
    else:
        for state in states_with_a:
            print(f"{state.id}: {state.name}")

    session.close()
