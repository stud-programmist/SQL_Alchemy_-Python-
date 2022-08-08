from sqlalchemy import Column, Integer, String, ForeignKey, Float
# from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Отношение таблиц:
# Houses - Flats : один к одному
# Flats - Resident: один к одному
# Flats - Houses: один к одному
# Flats - Owners: один к одному
# Relatives - Resident; Relatives - Owners: одно ко многому

class Relatives(Base):
    __tablename__ = 'Relatives'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('Owners.id'))
    resident_id = Column(Integer, ForeignKey('Residents.id'))
    owner = relationship('Owners', back_populates='relat')  #
    resident = relationship('Residents', back_populates='relats')  #

    def __repr__(self):
        return f'<owner_id={self.owner_id}, resident_id={self.resident_id}>'


class Owners(Base):
    __tablename__ = 'Owners'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    flat_id = Column(Integer, ForeignKey('Flats.id'))
    benefit_type = Column(String)
    account_number = Column(Integer)
    deleted = Column(String)
    relat = relationship('Relatives', back_populates='owner')  #
    flat = relationship('Flats', back_populates='owners')  #

    def __repr__(self):
        return f'<full_name={self.full_name}, flat_id={self.flat_id}, benefit_type={self.benefit_type}, account_number={self.account_number} >'

class Residents(Base):
    __tablename__ = 'Residents'
    id = Column(Integer, primary_key=True)
    flat_id = Column(Integer, ForeignKey('Flats.id'))
    full_name = Column(String)
    deleted = Column(String)
    relats = relationship('Relatives', back_populates='resident')  #
    flat = relationship('Flats', back_populates='resident')  #

    def __repr__(self):
        return f'< flat_id={self.flat_id}, full_name={self.full_name}>'

class Flats(Base):
    __tablename__ = 'Flats'
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, ForeignKey('Houses.id'))
    house = relationship('Houses', back_populates='flats')  #
    amount_of_space = Column(Float)
    number_of_rooms = Column(Integer)
    apartment_number = Column(Integer)
    # owners_id = Column(Integer, ForeignKey('Owners.id'))
    owners = relationship('Owners', back_populates='flat')  #
    # resident_id = Column(Integer, ForeignKey('Residents.id'))
    resident = relationship('Residents', back_populates='flat')  #

    def __repr__(self):
        return f'<house_id={self.house_id}, amount_of_space={self.amount_of_space}, number_of_rooms={self.number_of_rooms}, apartment_number ={self.apartment_number}>'

class Houses(Base):
    __tablename__ = 'Houses'
    id = Column(Integer, primary_key=True)
    address = Column(String)
    number_of_rooms = Column(Integer)
    living_space = Column(Float)
    flats = relationship('Flats', back_populates='house')  #
    # flat_id = Column(Integer, ForeignKey('Flats.id'))

    def __repr__(self):
        return f'<address={self.address}, number_of_rooms={self.number_of_rooms}, living_space={self.living_space}>'