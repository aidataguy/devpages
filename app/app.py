from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_api.decorators import set_renderers
from flask_api.renderers import JSONRenderer
import markdown

app = FlaskAPI(__name__)


@app.route('/')
def home():
    return ("HI from main page")

@app.route('/readme')
def readme():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return md_template_string



if __name__ == "__main__":
    app.run(debug=True)
