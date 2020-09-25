from flask import jsonify


def GenerateResponse(data, msg):
    response_data = {}
    data_list = []
    try:
        for i in data:
            temp = {}
            temp["S_NO"] = i[0]
            temp["MENU"] = i[1]
            temp["TYPE"] = i[2]
            temp["PRICE "]=i[3]
            data_list.append(temp)
            response_data["data"] = data_list

        response_data["msg"] = msg
        print(f"Respone data : {response_data}")
        return jsonify(response_data)
    except IndexError as e:
        print(e)
        return str(e)
