#from flask_migrate import Migrate
from .models import Table, Guest, Reservation
from app import db
import datetime

#Migrate(app,db)
DEFAULT_RESERVATION_LENGTH = 1 # 1 hour

def create_reservation(input_data):
    guest = Guest.query.filter_by(phone_number=input_data['guest_phone']).first()
    if guest is None:
        guest = Guest(name=input_data['guest_name'], phone_number=input_data['guest_phone'],email_id =input_data['email_id'] )
        db.session.add(guest)

    # now check table availability
    capacity = int(input_data['num_guests'])
    tables = Table.query.filter(Table.capacity >= capacity).order_by(Table.capacity.desc()).all()
    t_ids = [t.id for t in tables]
    if not t_ids:
        # no tables with that size
        return 'capacity'

    # check reservations
    begin_range = input_data['reservation_datetime'] - datetime.timedelta(hours=DEFAULT_RESERVATION_LENGTH)
    end_range = input_data['reservation_datetime'] + datetime.timedelta(hours=DEFAULT_RESERVATION_LENGTH)
    # reservations = Reservation.query.filter(Reservation.table.in_(
    #     t_ids), Reservation.reservation_time >= begin_range, Reservation.reservation_time <= end_range).all()
    reservations = Reservation.query.join(Reservation.table).filter(Table.id.in_(t_ids),
                    Reservation.reservation_time >= begin_range, Reservation.reservation_time <= end_range).order_by(Table.capacity.desc()).all()
    if reservations:
        if len(t_ids) == len(reservations):
            # no available tables, sorry
            # still add guest
            db.session.commit()
            return False
        else:
            # get available table
            table_id = (set(t_ids) - set([r.table.id for r in reservations])).pop()
            reservation = Reservation(guest=guest, table=Table.query.get(int(table_id)),
                                      num_guests=capacity, reservation_time=input_data['reservation_datetime'])
    else:
        # we are totally open
        reservation = Reservation(guest=guest, table=Table.query.get(int(t_ids[0])), num_guests = capacity, reservation_time=input_data['reservation_datetime'])

    db.session.add(reservation)
    db.session.commit()
    return reservation
def get_reservation(guestid):
    reservation = Reservation.query.filter_by(guest_id=int(guestid)).first()
    if reservation is not None:
        return reservation
    else:
      return ''
def get_guest_id(input_data):
    guest = Guest.query.filter_by(phone_number=input_data['guest_phone']).first()
    if guest is not None:
        return guest
    else:
      return ''
    