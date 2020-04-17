import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World!'

@app.route('/items', methods = ['POST'])
def add_item():
   #Get item from the POST body
   req_data = request.get_json()
   item = req_data['item']
   
   #Add item to the list
   res_data = helper.add_to_list(item)

   #Return error if item not added
   if res_data is None:
      response = Response("{'error': 'Item not added - '}"  + item, status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   
   return response

@app.route('/items', methods = ['GET'])
def get_all_items():
   # Get items from the helper
   res_data = helper.get_all_items()
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   return response

@app.route('/items/<id>', methods=['GET'])
def get_item(id):   
   # Get items from the helper
   item = helper.get_item(id)
   
   #Return 404 if item not found
   if item is None:
      response = Response("{'error': 'Item Not Found - "  + str(id) + "'}", status=404 , mimetype='application/json')
      return response

   response = Response(json.dumps(item), status=200, mimetype='application/json')
   return response

@app.route('/items/<id>/status/<status>', methods = ['PUT'])
def update_status(id,status):   
   #Update item in the list
   res_data = helper.update_status(id, status)
   if res_data is None:
      response = Response("{'error': 'Error updating item - '" + str(id) + ", " + status   +  "}", status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   
   return response

@app.route('/items/<id>', methods = ['DELETE'])
def delete_item(id):   
   #Delete item from the list
   res_data = helper.delete_item(id)
   if res_data is None:
      response = Response("{'error': 'Error deleting item - '" + str(id) +  "}", status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   
   return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')   