#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """
    Connect to the database and print the State object with the specified name.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
