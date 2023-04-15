from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, create_engine
import config

Base = declarative_base()


class Tier(Base):
    __tablename__ = 'Tier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, autoincrement=True, unique=True, nullable=False )

    def __repr__(self):
        return "<Tier(id='{}', name='{}')>".format(self.id, self.name)

class Instance(Base):
    __tablename__ = 'Instance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=False, nullable=False)
    price = Column(String, nullable=False)
    tier_id = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Instance(id='{}', name='{}', price='{}', tier_id='{}')>".format(self.id, self.name, self.price, self.tier_id)


if __name__ == '__main__':
    DATABASE_URI = config.db_conn_string
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
