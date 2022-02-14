import json
import requests

apiUrl = 'http://127.0.0.1:5000/recipes'

#Data we use to test the api
createData = {
	"name": "butteredBagel",
		"ingredients": [
			"1 bagel",
			"butter"
		],
	"instructions": [
		"cut the bagel",
		"spread butter on bagel"
	]
}

delData =         {
            "ingredients": [
                "500mL water",
                "100g spaghetti",
                "25mL olive oil",
                "4 cloves garlic",
                "Salt"
            ],
            "instructions": [
                "Heat garlic in olive oil",
                "Boil water in pot",
                "Add pasta to boiling water",
                "Remove pasta from water and mix with garlic olive oil",
                "Salt to taste and enjoy"
            ],
            "name": "garlicPasta"
        }


putData = {
	"name": "butteredBagel",
		"ingredients": [
			"1 bagel",
			"2 tbsp butter"
		],
	"instructions": [
		"cut the bagel",
		"spread butter on bagel"
	]
}


#Testing Recipe Names GET
print("Testing Recipe Names GET -- Code: 200")
r = requests.get(url=apiUrl)
print(r.status_code, r.reason, r.text, "\n")

#Testing garlicPasta recipes
print("Testing garlicPasta recipes -- Code: 200")
garlicUrl = 'http://127.0.0.1:5000/recipes/details/garlicPasta'
r = requests.get(url=garlicUrl)
print(r.status_code, r.reason, r.text, "\n")


# Testing garlic Pasta DELETE
print("Testing garlic Pasta DELETE -- Code: 204")
r = requests.delete(url=apiUrl, json=delData)
print(r.status_code, r.reason, r.text, "\n")

# Testing garlic Pasta DELETE When already Deleted
print("Testing garlic Pasta DELETE When already Deleted -- Code: 404")
r = requests.delete(url=apiUrl, json=delData)
print(r.status_code, r.reason, r.text, "\n")

# Testing bagel PUT When no recipe exists
print("Testing bagel PUT When no recipe -- Code: 404")
r = requests.put(url=apiUrl, json=putData)
print(r.status_code, r.reason, r.text, "\n")

# Testing Bagel POST
print("Testing Bagel POST  -- Code: 201")
r = requests.post(url=apiUrl, json=createData)
print(r.status_code, r.reason, r.text, "\n")

# Testing Bagel POST When already POSTED
print("Testing Bagel POST When already POSTED -- Code: 400")
r = requests.post(url=apiUrl, json=createData)
print(r.status_code, r.reason, r.text, "\n")

# Testing bagel PUT
print("Testing bagel PUT -- Code: 204")
r = requests.put(url=apiUrl, json=putData)
print(r.status_code, r.reason, r.text, "\n")

# Testing bagel PUT When Already PUT
print("Testing bagel PUT When Already PUT -- Code: 204")
r = requests.put(url=apiUrl, json=putData)
print(r.status_code, r.reason, r.text, "\n")

#Cleanu Up so json is the same as when we started
#Add garlic pasta
print("Post Garlic Pasta")
r = requests.post(url=apiUrl, json=delData)
print(r.status_code, r.reason, r.text, "\n")

#delete bagel
print("Delete bagel recipes")
r = requests.delete(url=apiUrl, json=putData)
print(r.status_code, r.reason, r.text, "\n")
