#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from the database 'hbtn_0e_6_usa'
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session


if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    session.execute(
        delete(State).where(State.name.like("%a%")),
        execution_options={"synchronize_session": False})
    session.commit()
    session.close()
