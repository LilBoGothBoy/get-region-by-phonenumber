from flask_restful import Api, Resource
from flask import Flask
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
        phone_number = phone_number.replace("-", "")
        phone_number = phone_number.replace("(", "")
        phone_number = phone_number.replace(")", "")
        phone_number = phone_number.replace("+", "")
        response = requests.get(
            f'http://rosreestr.subnets.ru/?get=num&num={phone_number}&field=region&format=csv')
        if len(phone_number) != 11 and phone_number[0] not in ("7", "8"):
            phone_number = "8" + phone_number
        if len(phone_number) == 11:
            return response.text, 200
        else:
            return 'Error!', 404


api.add_resource(Bot_Answer, '/get_region/<string:phone_number>')
if __name__ == '__main__':
    app.run(debug=True)
