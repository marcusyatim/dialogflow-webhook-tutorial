# import flask dependencies
from flask import Flask, request

# initialize the flask app
app = Flask(__name__)

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = 'xxx'
    query_result = req.get('queryResult')
    if query_result.get('action') == 'get.address':
        ### Perform set of executable code
        ### if required
        ### ...

        fulfillmentText = "Hi .. i am in"
    return {
            "fulfillmentText": fulfillmentText,
            "source": "webhookdata"
        }

# run the app
if __name__ == '__main__':
    app.run()
