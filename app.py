from flask import Flask, jsonify, request

app = Flask(__name__)
users = []


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


@app.route("/users/<id_>", methods=["GET"])
def get_user(id_):
    user = [u for u in users if u['id'] == id_]
    if user:
        return jsonify(user.pop()), 200
    else:
        return "user not found", 404


@app.route("/users", methods=["POST"])
def create_user():
    user = request.get_json()
    users.append(user)
    return user, 200


@app.route("/users/<id_>", methods=["DELETE"])
def delete_user(id_):
    users.remove([u for u in users if u['id'] == int(id_)].pop())
    return jsonify(users), 200


@app.route("/users/<id_>", methods=["PUT"])
def update_user(id_):
    user = [u for u in users if u['id'] == id_]
    if not user:
        return "user not found", 404
    user = user.pop()
    user = request.get_json()
    return jsonify(user), 200


app.run(host='0.0.0.0', port='5555')