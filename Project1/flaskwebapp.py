from flask import Flask, jsonify, make_response, abort, request
import logging
import requests
import json

app = Flask(__name__,
            static_url_path='')


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route('/ui')
def index():
    return app.send_static_file("charter.html")


@app.route('/benchmarkdailyreturn', methods=['POST'])
def getDailyReturn():
    logging.info(request.data)
    if not request.data:
        abort(400)
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data={})
    logging.info(response.text)
    resp = make_response(response.text.encode('utf-8'))  # here you could use make_response(render_template(...)) too
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run(debug=True, port=5050)