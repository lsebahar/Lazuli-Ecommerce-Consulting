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
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
        # Extract the input
        product_description_lenght = flask.request.form['product_description_lenght']
        product_photos_qty = flask.request.form['product_photos_qty']
        Is_It_Late = flask.request.form['Is_It_Late']
        Payment_Type = flask.request.form['Payment_Type']
        Total_Order_Value = flask.request.form['Total_Order_Value']


        # Make DataFrame for model
        input_variables = pd.DataFrame([[product_description_lenght, product_photos_qty, Is_It_Late, Payment_Type,
                                        Total_Order_Value]],
                                       columns=['product_description_lenght', 'product_photos_qty', 'Is_It_Late',
                                       'Payment_Type', 'Total_Order_Value'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',
                                     original_input={'product_description_lenght':product_description_lenght,
                                                     'product_photos_qty':product_photos_qty,
                                                     'Is_It_Late':Is_It_Late,
                                                     'Payment_Type':Payment_Type,
                                                     'Total_Order_Value':Total_Order_Value},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run(debug=True)