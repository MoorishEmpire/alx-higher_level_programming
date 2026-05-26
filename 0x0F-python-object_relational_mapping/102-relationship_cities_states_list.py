#!/usr/bin/python3
"""
Lists all City objects rom the database 'hbtn_0e_101_usa'
"""
import sys
from relationship_city import City
from relationship_state import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, joinedload


if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
