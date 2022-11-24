from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

heart_records = {
    1 : {'heart_id':1, 'date':'November 24, 2022', 'heart_rate':'80bpm'}
}

class HeartRecords(Resource):
    def get(self): # gets all records
        return heart_records
    
    def post(self): # inserts a record
        newHeartRecord = request.get_json()
        heart_records['heart_id'] = {
            'heart_id':newHeartRecord['']['heart_id'],
            'date':newHeartRecord['']['date'],
            'heart_rate':newHeartRecord['']['heart_rate']
        }
        return "Heart record successfully added!"


class HeartRecord(Resource):
    def get(self, heart_id): # get a record by id
        return heart_records[heart_id]
    
    def delete(self, heart_id): # delete a record by id
        del heart_records[heart_id]
        return "Heart record successfully deleted!"

api.add_resource(HeartRecords, '/')
api.add_resource(HeartRecord, '/heartrecord/<int:heart_id>')


if __name__ == "__main__":
    app.run(port=5050)