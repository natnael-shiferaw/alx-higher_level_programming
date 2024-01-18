#!/usr/bin/python3
"""
This script used to list all the State objects from the
hbtn_0e_6_usa database that contain the letter 'a' in their name.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a database engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session maker to connect to the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # print details of states with the letter 'a' in their name
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
