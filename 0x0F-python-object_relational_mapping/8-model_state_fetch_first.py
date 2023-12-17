#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]

        engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
            pool_pre_ping=True,
        )

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        first_state = session.query(State).order_by(State.id).first()

        print(
            f"{first_state.id}: {first_state.name}"
            if first_state
            else "Nothing"
        )

        session.close()
