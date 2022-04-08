from config.Railway_form import *


class RailwayForm(Base):
    __tablename__ = "railwayform"
    trainNoName = Column("trainnoname", String, primary_key=True)
    dateOfJourney = Column("dateofjourney", String)
    noOfBerth = Column("noofberth", Integer)
    stationFrom = Column("stationfrom", String)
    stationTo = Column("stationto", String)
    boardingAt = Column("boardingat", String)
    reservationUpto = Column("reservationupto", String)
