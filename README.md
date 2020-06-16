# Filtering Service
this is a service that can select the proper rectangular based on Response class. It implemented with flask and MongoDB and for Restful leveraged from flask-restful.

## Installation
first, build a virtual environment then run
```
pip install -r requirements.txt
```


## Respond class
It has two methods (post and get). 
Post method take json file on http://localhost:5000/ in this format
```
{
    "main": {"x": number , "y": number , "width": number , "height": number },
    "input": [
    {"x": number , "y": number , "width": number , "height": number },
    {"x": number , "y": number , "width": number , "height": number },
    ...
    ]
}
``` 
Get method answer on http://localhost:5000/ in this manner
```
[
    {"x": number , "y": number , "width": number , "height": number , "time":"YYYY-MM-DD HH:mm:ss"},
    {"x": number , "y": number , "width": number , "height": number , "time":"YYYY-MM-DD HH:mm:ss"},
    ...
]
```
## examples
```
POST http://localhost:5000/
Request: (time: 2019-01-01 18:00:00)
{
    "main": {"x":0, "y": 0, "width": 10, "height": 20},
    "input": [
    {"x":2, "y": 18, "width": 5, "height": 4},
    {"x":12, "y": 18, "width": 5, "height": 4},
    {"x":-1, "y": -1, "width": 5, "height": 4}
    ]
}
POST http://localhost:5000/
Request: (time: 2019-01-02 09:30:00)
{
    "main": {"x": 3, "y": 2, "width": 5, "height": 10},
    "input": [
        {"x": 4, "y": 10, "width": 1, "height": 1},
        {"x": 9, "y": 10, "width": 5, "height": 4}
    ]
}
GET http://localhost:5000/
Response:
[
    {"x": 2, "y": 18, "width": 5, "height": 4, "time": "2019-01-01 18:00:00"},
    {"x": -1, "y": -1, "width": 5, "height": 4, "time": "2019-01-01 18:00:00"},
    {"x": 4, "y": 10, "width": 1, "height": 1, "time": "2019-01-02 09:30:00"}
]
```
