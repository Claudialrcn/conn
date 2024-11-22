import os
from typing import Optional

from dotenv import load_dotenv
from sqlmodel import Field, SQLModel, create_engine, Session

load_dotenv()

username = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
hostname = os.getenv("ORACLE_HOSTNAME")
sid = os.getenv("ORACLE_SID")


class Recipe2(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30)


recipe_1 = Recipe2(id=1, name="Taco")
recipe_2 = Recipe2(id=2, name="Cinnamon roll")
recipe_3 = Recipe2(id=3, name="Pizza dough")

conn_string = f"oracle+oracledb://{username}:{password}@{hostname}/{sid}"

engine = create_engine(conn_string, echo=True)


SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(recipe_1)
    session.add(recipe_2)
    session.add(recipe_3)
    session.commit()
