from flask import Flask , request,jsonify
from flask_restful import Resource, Api,reqparse
from flask_migrate import Migrate
from datetime import datetime ,timedelta
import json
from .models import MAX_TABLE_CAPACITY
from .controller import create_reservation
from app import app




api = Api(app)
RESTAURANT_OPEN_TIME=16
RESTAURANT_CLOSE_TIME=22

class index(Resource):
  def post(self):
    data = reqparse.RequestParser()
    data.add_argument('reservation_datetime',type=str,required=True,default=datetime.now())
    data.add_argument('guest_name',type=str,required=True)
    data.add_argument('guest_phone',type=int,required=True)   
    data.add_argument('num_guests',type=int,required=True)
    data.add_argument('email_id',type=str,required=True)
    
    print("Time Now:",datetime.now())
    
    args = data.parse_args()
    args['reservation_datetime'] = datetime.strptime(args['reservation_datetime'],'%m%d%Y %H:%M:%S')
    if args['reservation_datetime'] < datetime.now():
      return {"message": "requested data","result":"You cannot book dates in the past"},200
    
    reservation_date = datetime.combine(args['reservation_datetime'], datetime.min.time())
    
    if args['reservation_datetime'] < reservation_date + timedelta(hours=RESTAURANT_OPEN_TIME) or \
        args['reservation_datetime'] > reservation_date + timedelta(hours=RESTAURANT_CLOSE_TIME):
            
            return {"message": "requested data","result":"The restaurant is closed at that hour!"},200
    reservation = create_reservation(args)
    
    #return {"message": "requested data","result":json.dumps(args)},201
    if reservation == 'capacity':            
            return {"message": "Request Status","result":"No tables with that size"},200
            #return redirect('/index')    
    elif not reservation:      
      return {"message": "Request Status","result":"That time is taken!  Try another time"},201
      #return redirect('/make_reservation')
    return {"message": "Request Status","result":"You reservation is confirmed"},201
  def get(self):
    return {"message": "Requested data","result": "nothing to display"},200
class booking(Resource):
  def get(self,num):
    return {"message": "Requested Data","result": num *3},200
api.add_resource(index,'/')
api.add_resource(booking, '/booking/<int:num>')

#if __name__ == "__main__":
#  app.run(debug = True)

