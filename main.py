from flask import Flask, request, render_template, redirect
import requests


def get_joke():
    url = 'https://v2.jokeapi.dev/joke/Any'
    response = requests.get(url, headers={'Accept': 'application/json'}, params={
        "flags": {
            "nsfw": request.form.get('nsfw'),
            "religious": request.form.get('religious'),
            "political": request.form.get('political'),
            "racist": request.form.get('racist'),
            "explicit": request.form.get('explicit')
        },
    })
    data = response.json()
    return data


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        res = get_joke()
        if res["type"] == "single":
            joke = res["joke"]
            return render_template("index.html", joke=joke)
        else:
            setup = res["setup"]
            delivery = res["delivery"]
            return render_template("index.html", setup=setup, delivery=delivery)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
