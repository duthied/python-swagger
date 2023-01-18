# main.py
from flask import Flask
from blueprints.basic_endpoints import blueprint as basic_endpoint
from blueprints.jinja_endpoint import blueprint as jinja_template_blueprint

app = Flask(__name__)
app.register_blueprint(basic_endpoint)
app.register_blueprint(jinja_template_blueprint)

if __name__ == "__main__":
  app.run()
