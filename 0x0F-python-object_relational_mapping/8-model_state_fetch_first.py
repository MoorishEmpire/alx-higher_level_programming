#!/usr/bin/python3

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy import select


if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    obj = session.scalars(select(State)).first()
    if obj is None:
        print('Nothing')
    else:
        print('{}: {}'.format(obj.id, obj.name))
    session.close()
