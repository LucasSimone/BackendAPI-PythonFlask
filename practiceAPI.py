#Needed libraries we use
import flask
import json
from flask import request, Response

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Open our json file
with open('data.json') as json_file:
    data = json.load(json_file)

#This function takes the new data and updates the data.json with it
def updateDatabase(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)


#The homepage for the api
@app.route('/', methods=['GET'])
def home():
    return '''<h1>This is the API for Hatchaways Livebarn test</h1>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'''


#Fucntion for GET POST and PUT requests on /recipes page
@app.route('/recipes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_recipe():

    #This is where we return recipe names for GET Requests
    if request.method == 'GET':
        #Getting data requested from Json
        getData = {'recipeNames': []}
        for info in data['recipes']:
            getData["recipeNames"].append(info['name'])

        #Creating the response with the data, Status code, and output format(Json)
        response = app.response_class(
            response=json.dumps(getData),
            status=200,
            mimetype='application/json'
        )
        return response



    #This is where we take in POST Requests and add it to data
    if request.method == 'POST':
        createRecipe = {}
        createRecipe['name'] = request.json['name']
        createRecipe['ingredients'] = request.json['ingredients']
        createRecipe['instructions'] = request.json['instructions']

        #check if recipe already Exists
        for info in data['recipes']:
            if info['name'] == createRecipe['name']:
                #Recipe Exists
                #return empty json
                return Response(
                    json.dumps({}),
                    status=400,
                    mimetype='application/json'
                )

        #Recipe Dosent exist add to data
        data['recipes'].append(createRecipe)

        updateDatabase(data)

        return Response(
            json.dumps(createRecipe),
            status=201,
            mimetype='application/json'
        )

    #This is where we take in PUT Requests and modif data
    if request.method == 'PUT':
        recipeName = request.json['name']

        for info in data['recipes']:
            if info['name'] == recipeName:
                info['instructions'] = request.json['instructions']
                info['ingredients'] = request.json['ingredients']


                updateDatabase(data)

                return Response(
                    '',
                    status=204,
                    mimetype='application/json'
                )


        ret = { "error": "Recipe does not exist" }
        return Response(
            ret,
            status=404,
            mimetype='application/json'
        )


    #This is where we take in DELETE Requests
    if request.method == 'DELETE':
        delRecipe = request.json['name']


        #check if recipe already Exists
        for i in range(len(data['recipes'])):
            if data['recipes'][i]['name'] == delRecipe:
                #Recipe Exists
                del data['recipes'][i]

                updateDatabase(data)

                #return empty json
                return Response(
                    json.dumps({}),
                    status=204,
                    mimetype='application/json'
                )


        return Response(
            json.dumps({}),
            status=404,
            mimetype='application/json'
        )








# A get request to garlic pasta details
@app.route('/recipes/details/garlicPasta', methods=['GET'])
def api_garlicPasta_details():

    #Check if Gralic Pasta Recipe Exists
    for info in data['recipes']:
        if info['name'] == "garlicPasta":
            #Exists
            #Getting data requested from Json
            getData = {'details': {}}
            getData['details']['ingredients'] = (info['ingredients'])
            getData['details']['numSteps'] = len(info['instructions'])


            #Creating the response with the data, Status code, and output format(Json)
            return Response(
                response=json.dumps(getData),
                status=200,
                mimetype='application/json'
            )


    #Didnt hit first return
    #Does Not Exist
    #Creating the response for data not existing
    emptyDict = {}
    return Response(
        response = json.dumps({}),
        status=200,
        mimetype='application/json'
    )



app.run()
