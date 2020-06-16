from datetime import datetime
from flask import Flask
from flask import jsonify, request
from flask_restful import Resource, Api
import pymongo

from rectangular import Rectangular
# connect to database
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
# bulid a database
my_db = my_client["Rectangular"]
# bulid a collection 
my_col = my_db["FilteredRec"]

app = Flask(__name__)
api = Api(app)

class Respond(Resource):
    """ 
    description: 
        main class for Filtering Service
    """

    def post(self):
        """ 
        description: 
        it takes a JSON with the special format and saves proper rectangular
        """
        _json = request.json
        _main = _json["main"]
        _input = _json["input"]
        # set it as object of Rectangular class
        main_rectangular =Rectangular(*_main.values())
        # iterable(generator) of input rectangulars(in fact as object of Rectangular class)
        rectangular_list = (Rectangular(*item.values()) for item in _input)  
        # A List of python dict so we can insert it in DB 
        ready_to_insert = main_rectangular.filter_accepted_rectangular(rectangular_list)
        # try:
            # X is object that we can rich to ObjectId of each inserted instance
        my_col.insert_many(ready_to_insert)
            # check the number of accepted rectangulars and inserted rectangulars 
        return {"note":"insertion success"}
        # except:
        #     return {"note":"someting went Wrong"}

    def get(self):
        """ 
        description: 
        it returns a JSON with the special format and saves proper rectangular
        """
        return [x for x in my_col.find({},{ '_id': 0})]
            


api.add_resource(Respond,"/")


if __name__ == "__main__":
    app.run(debug=True)