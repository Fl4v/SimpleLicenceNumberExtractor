from functions import licence_nr_extractor
import json
import flask

app = flask.Flask(__name__)

@app.route('/extract_licence_number', methods=['POST'])
def ocr_image():
    req_data = flask.request.get_data()
    binary_image = req_data['binary']
    return json.dumps({'licence_nr': 'tbc'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
