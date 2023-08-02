from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        # Add more data or fetch data from your storage here
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run()