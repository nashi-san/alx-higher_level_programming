#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine_url = "mysql+mysqldb://" + username + ":" + password + \
        "@localhost:3306/" + db_name
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        state_name = state.name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()
