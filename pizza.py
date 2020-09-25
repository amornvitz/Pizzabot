from flask import Flask, request, jsonify
import Mysqlconnector as connect
import GenerateResponse as res
import Error as err

app= Flask(__name__)
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

@app.route("/fetch", methods=["get", "post"])
def fetch():
    conn = connect.ConnectMySql()
    print(f"Connection status : {conn}")

    if(conn is False):
        return err.ReturnConnectionError()
    else:
        try:
            cur = conn.cursor()
            print(f"Cursor object : {cur}")
            query = ("select * from pizza")
            cur.execute(query)
            msg = "Data fetched succesfully"
            return res.GenerateResponse(cur,msg)
        except Exception as e:
            print(e)
            return err.ReturnFetchError()
        finally:
            conn.close()

@app.route("/fetch1", methods=["get", "post"])
def fetch():
    conn = connect.ConnectMySql()
    print(f"Connection status : {conn}")

    if(conn is False):
        return err.ReturnConnectionError()
    else:
        try:
            cur = conn.cursor()
            print(f"Cursor object : {cur}")
            query = ("select * from customer")
            cur.execute(query)
            msg = "Data fetched succesfully"
            return res.GenerateResponse(cur,msg)
        except Exception as e:
            print(e)
            return err.ReturnFetchError()
        finally:
            conn.close()

@app.route("/insert", methods=["post"])
def insertdata():
    data=reponse.json
    pass

    if intent == 'Welcome':
            { "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            webhookresponse
                        ]

                    }
                },
                    {
                        "text":
                        {
                            "text": [
                                "Hello :) Welcome to YoYo Pizza , Hope you are staying at home safe! What can I do for you?"
                            ]
                        }
                        ]
                    }
        }

    elif intent == 'Order':
            { "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            webhookresponse
                        ]

                    }
                }
                    {
                        "text":
                        {
                            "text": [
                                "Please select what kind of pizza do you want? veg or nonveg"
                            ]
                        }
                        ]
                    }
        }
    elif intent == 'Order':
            {"fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            webhookresponse
                        ]

                    }
                }
                {
                    "text":
                        {
                            "text": [
                                "Please select what kind of pizza do you want? veg or nonveg"
                            ]
                        }
            ]
            }
            }

    elif intent == "Veg":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)
    elif intent == "NonVeg":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)
    elif intent == "NonVeg":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)
    elif intent == "Toppings":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)
    elif intent == "Toppings2":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)
    elif intent == "Order":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)
    elif intent == "Quantity":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)
    elif intent == "Mobile_number":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)
    elif intent == "Size":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)
    elif intent == "Address":
            fulfillmentText = result.get("fulfillmentText")
            log.saveConversations(query_text, fulfillmentText, intent, db)



    if __name__ == '__main__':
    app.run(debug=True,port=3000)