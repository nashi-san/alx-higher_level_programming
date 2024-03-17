#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
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

    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    session.close()
