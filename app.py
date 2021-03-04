import os
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
app.config["GITHUB_OAUTH_CLIENT_ID"] = "2d6432d7473dd5d82b4b"
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = "c5ab4101055c32325ce838504691a1577401a346"
github_bp = make_github_blueprint()
app.register_blueprint(github_bp, url_prefix="/github_login")



@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    if resp.ok:
        return "You are @{login} on GitHub".format(login=resp.json()["login"])
    return "<h1>Ooops!</h1>"


if __name__ == '__main__': app.run(debug=True)

    
    