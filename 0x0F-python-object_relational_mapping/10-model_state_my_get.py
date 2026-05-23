#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database 'hbtn_0e_6_usa'
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    obj = session.scalars(select(State).where(State.name == sys.argv[4])).all()
    if len(obj) == 0:
        print("Not found")
    else:
        print(f"{obj[0].id}")
    session.close()
