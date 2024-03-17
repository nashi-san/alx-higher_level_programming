#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username, password, db_name, state_name = sys.argv[1], \
        sys.argv[2], sys.argv[3], sys.argv[4]
    engine_url = "mysql+mysqldb://" + username + ":" + \
        password + "@localhost:3306/" + db_name
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
