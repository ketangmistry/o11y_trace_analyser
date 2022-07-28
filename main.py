import os

from flask import Flask, jsonify
from flask_cors import CORS
from pubsub.subscription import Subscripton

import pubsub.message_reader as mr

GCP_PROJECT_NO = os.environ.get('GCP_PROJECT_NO')
GCP_REGION = os.environ.get('GCP_REGION')
GCP_ZONE_ID = os.environ.get('GCP_ZONE_ID')
GCP_PUBSUB_SUB_ID = os.environ.get('GCP_PUBSUB_SUB_ID')


def create_app(config=None):
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    CORS(app)

    @app.route("/")
    def home():
        return "The o11y Trace Analyser webapp"

    @app.route("/subscriptions")
    def subscriptions():
        s = Subscripton(GCP_PROJECT_NO, GCP_REGION, GCP_ZONE_ID, GCP_PUBSUB_SUB_ID)
        s.get_subscriptions()
        return jsonify({"found": s.found})

    return app


if __name__ == "__main__":
    # start the pubsub reader thread
    mr.start_reader()

    port = int(os.environ.get("PORT", 8000))

    print(f'app_start: starting flask on port {port}.')
    app = create_app()
    app.run(host="0.0.0.0", port=port)