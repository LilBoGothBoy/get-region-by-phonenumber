from flask_restful import Api, Resource
from flask import Flask
import json
import logging
import requests
import sys


app = Flask(__name__)
api = Api(app)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


class Bot_Answer(Resource):
    def get(self, phone_number):
        phone_number = phone_number.replace(" ", "")
        response = requests.get(
            f'http://rosreestr.subnets.ru/?get=num&num={phone_number}&format=json')
        todos = json.loads(response.text)
        if len(phone_number) == 11:
            return todos['0']['region'], 200
        else:
            return 'Error!', 404


api.add_resource(Bot_Answer, '/get_region/<string:phone_number>')
if __name__ == '__main__':
    app.run(debug=True)
