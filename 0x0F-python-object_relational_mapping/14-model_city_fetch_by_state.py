#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import Base, City


if __name__ == '__main__':
    """
    Access database and print all City Objects.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State)

    for city in cities():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
