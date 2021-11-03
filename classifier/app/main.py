from flask import Flask, json, request


api = Flask(__name__)

@api.route('/classify', methods=['GET'])
def classify():
    term = request.args.get('term')
    data = [{"id": 1, "category": "Cat"}, {"id": 2, "category": "Dog"}]
    data.append({
        "id": 3,
        "name": term
    })
    return json.dumps(data)

if __name__ == '__main__':
    api.run()