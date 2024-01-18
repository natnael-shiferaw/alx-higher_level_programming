#!/usr/bin/python3
"""
This script prints the first State object from
the hbtn_0e_6_usa database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a database engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Create a session maker to connect to the database
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # Query the database for the first State object
    state = session.query(State).order_by(State.id).first()

    # Print the id and name of the first State object
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
