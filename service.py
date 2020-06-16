from datetime import datetime
from flask import Flask
from flask import jsonify, request
from flask_restful import Resource, Api
import pymongo

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
        try:
            # X is object that we can rich to ObjectId of each inserted instance
            my_col.insert_many(ready_to_insert)
            # check the number of accepted rectangulars and inserted rectangulars 
            return {"note":"insertion success"}
        except:
            return {"note":"someting went Wrong"}

    def get(self):
        """ 
        description: 
        it returns a JSON with the special format and saves proper rectangular
        """
        return [x for x in my_col.find({},{ '_id': 0})]
            

class Rectangular():
    def __init__(self, x, y, width, height,time=None):
        """
        description: 
            difine a rectangular in X-Y coordinate
        args:
            x: horizontal coordinate
            y: vertical coordinate 
            width: the segment between x, x+ width 
            height: the segment between y, y+height
            time: timeStamp of the creation of this object
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.time = dt_string
    
    def _has_intersection(self,other):
        """
        description: 
            Check that the intersection of two objects(Intersection is symmetric).
            if just of vertex in second rectangular in main rectangular 
            then they have an intersection.
            WARNING: this definition excludes the boundary.
        args:
            Take a instace of Rectangular Class
        Return(boolen): 
            True if there exist a intersection Area
        """

        x1 = (self.x < other.x < (self.x+ self.width)) 
        x2 = (self.x < (other.x + other.width) < (self.x+ self.width))
        y1 = (self.y < other.y < (self.y + self.height))
        y2 = (self.y < (other.y + other.height) < (self.y + self.height))
        #these are four boolean that indcate the existence of vertices in main rectangular 
        x1y1 = (x1 and y1)
        x2y1 = (x2 and y1)
        x1y2 = (x1 and y2)
        x2y2 = (x2 and y2)
        if any([x1y1, x2y1, x1y2, x2y2]):
            return True
        return False

    def filter_accepted_rectangular(self, others):
        """
        description: 
            Select thoses rectangular that has intersection with main rectangular
        args:
            Take a instace of Rectangular Class
        Return: 
            List of dictionay of accepted Rectangular
        """
        accepted_list = []
        for item in others:
            if self._has_intersection(item):
                accepted_list.append(item.json_able())
        return accepted_list
    
    def json_able(self):
        """
        description: 
            it return just a dictionary of class attributes
        """
        
        ret = {"x":self.x, "y":self.y, "width":self.width, "height":self.height,"time":self.time}
        return ret

api.add_resource(Respond,"/")


if __name__ == "__main__":
    app.run()