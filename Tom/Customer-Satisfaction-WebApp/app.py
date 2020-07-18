import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
with open(f'customer_satisfaction.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))

    if flask.request.method == 'POST':
        # Extract the input
        Total Order Value = flask.request.form['Total Order Value']
        product_description_lenght = flask.request.form['product_description_lenght']
        Customer City = flask.request.form['Customer City']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[Total Order Value, product_description_lenght, Customer City]],
                                       columns=['Total Order Value', 'product_description_lenght', 'Customer City'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('index.html',
                                     original_input={'Temperature':Total Order Value,
                                                     'product_description_lenght':product_description_lenght,
                                                     'Customer City':Customer City},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()