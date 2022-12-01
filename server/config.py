from flask import Flask
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
      MONGO_URI=os.environ.get("MONGO_URI"),
      TWILIO_ACCOUNT_SID=os.environ.get("TWILIO_ACCOUNT_SID"),
      TWILIO_AUTH_TOKEN=os.environ.get("TWILIO_AUTH_TOKEN"),
    )

    return app

