# Restaurant Reservation System

This is a simple restaurant reservation system built in Flask & Python

## Installation Requirements
This application requires Flask, the Flask SQL Alchemy extension (which installs SQL Alchemy), and the Migrate package

Flask:
```
pip install Flask
```

Flask SQL Alchemy
```
pip install Flask-SQLAlchemy
```

DB Migrate
```
pip install flask_migrate
```

## Running the application
Simply run "run.py", this will start the local web server.



## Notes
Metrics:
* Table utilization on the given day
* Reservation slot utilization (number of reservations on a given day vs number of possible reservations)

Additional metrics to gather:
* Since we are tracking guests who book a reservation, we can build a statistical profile of that guest (e.g. how often they dine, how big their parties are, etc)
* Study which tables are booked more frequently and at which times

Additional Features to add:
* Input validation
* A better date/time picker
* More dynamic tables, sorting, etc on the Admin side for studying reservations and table utilization
* The ability to delete or update tables
* A multi-restaurant interface (so you'd need a restaurant table to track that)
* Obviously a better visual design
* log in for user
* payment micro service
* sending email for the confirmed reservation
* messaging architecture other then rabbitMQ.
* Authentication 



## Table design
Guest
* ID - Primary Key
* name - String
* phone_number - String
* email_id -String

Table
* ID - Primary Key
* Capacity - Integer

Reservation
* ID - Primary Key
* guest_id - Foreign Key(Guest)
* table_id - Foreign Key(Table)
* num_guests - Integer
* reservation_time - DateTime

## Misc
Assumed reservation length - 1 hour 
Restaurant opening time - 4pm
Restaurant closing time - 10pm 
