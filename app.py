from flask import Flask, render_template, request, redirect, url_for
from config import Config
import requests
app = Flask(__name__)

# API endpoints
RECIPE_FINDER_URL = 'https://api.edamam.com/api/recipes/v2'

# initialize the app
@app.route('/', methods=['GET', 'POST'])
def index():
    
    recipes = []
    if request.method == 'POST':

        # parameters for the API request
        params = {
            'type': 'public',
            'q': request.form.get('query'),
            'app_id': Config.RECIPE_FINDER_ID,
            'app_key': Config.RECIPE_FINDER_KEY,
        }
        
        response = requests.get(RECIPE_FINDER_URL, params=params)
        
        # if the request is successful, the recipes will be displayed
        if response.status_code == 200:
            data = response.json()
            recipes = data.get('hits')

        # if there are no recipes, the user will be redirected to the success page
        else:
            print('Error:', response.status_code, response.text)
            recipes = []
        
    return render_template('index.html', recipes=recipes)

# if the form is submitted successfully, the user will be redirected to the success page
@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
