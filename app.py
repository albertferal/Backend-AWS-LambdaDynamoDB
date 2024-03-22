from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URLs del backend
add_favorite_url = "https://gkxlflaqr8.execute-api.eu-west-1.amazonaws.com/dev/add-favorite"
list_favorites_url = "https://gkxlflaqr8.execute-api.eu-west-1.amazonaws.com/dev/list-favorite"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_favorite", methods=["POST"])
def add_favorite():
    org_id = request.form["org_id"]
    favorite_org_id = request.form["favorite_org_id"]

    response = requests.post(add_favorite_url, json={"org_id": org_id, "favorite_org_id": favorite_org_id})
    if response.status_code == 200:
        return "Favorite added successfully!"
    else:
        return "Failed to add favorite."

@app.route("/list_favorites")
def list_favorites():
    response = requests.get(list_favorites_url)
    if response.status_code == 200:
        favorites = response.json()
        return render_template("favorites.html", favorites=favorites)
    else:
        return "Failed to list favorites. Response: " + str(response.text)  # Imprimir respuesta del backend

if __name__ == "__main__":
    app.run(debug=True)
