import flask
from flask import Flask, request, render_template, make_response, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = mysql_schema + '//benchmarkdbuser:benchmarkdbpass@%s:3306/hello_world?charset=utf8' % DBHOST
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
db = SQLAlchemy(app)
dbraw_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], connect_args={'autocommit': True}, pool_reset_on_return=None)


def json_response(obj):
    res = make_response(json.dumps(obj))
    res.mimetype = "application/json"
    return res


@app.route("/json")
def hello():
    return jsonify(message='Hello, World!')


@app.route('/plaintext')
def plaintext():
    """Test 6: Plaintext"""
    response = make_response(b'Hello, World!')
    response.content_type = 'text/plain'
    return response



try:
    import meinheld
    meinheld.server.set_access_logger(None)
    meinheld.set_keepalive(120)
except ImportError:
    pass

# entry point for debugging
if __name__ == "__main__":
    app.run(debug=True)
