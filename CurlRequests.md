# Examples of curl requests

1. Add new data
> curl -X POST -H "Content-Type: application/json" -d '{"data": "3,12;1,4;1,5;1,5;3,8;5,3;5,8"}' 
> http://localhost:8000/data/add/

2. Get data
> curl -X GET -H "Cache-Control: no-cache" "http://localhost:8000/data/get?a=3&b=12"
