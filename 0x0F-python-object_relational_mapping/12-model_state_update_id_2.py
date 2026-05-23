#!/usr/bin/python3
"""
Changes the name of a State object from the database 'hbtn_0e_6_usa'
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    request = select(State).where(State.id == 2)
    state = session.scalars(request).first()

    if state:
        state.name = "New Mexico"
        session.commit()
    session.close()
