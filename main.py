import os

from flask import Flask, jsonify
from flask_cors import CORS
from pubsub.subscription import Subscripton


def create_app(config=None):
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    CORS(app)

    @app.route("/")
    def hello_world():
        return "Hello World"

    @app.route("/foo/<someId>")
    def foo_url_arg(someId):
        return jsonify({"echo": someId})

    @app.route("/pubsub/subscriptions")
    def pubsub_subscription():
        GCP_PROJECT_NO = os.environ.get('GCP_PROJECT_NO')
        GCP_REGION = os.environ.get('GCP_REGION')
        GCP_ZONE_ID = os.environ.get('GCP_ZONE_ID')
        GCP_PUBSUB_SUB_ID = os.environ.get('GCP_PUBSUB_SUB_ID')
        s = Subscripton(GCP_PROJECT_NO, GCP_REGION, GCP_ZONE_ID, GCP_PUBSUB_SUB_ID)
        s.get_trace_subscription()
        return jsonify({"response": s.response})

    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)