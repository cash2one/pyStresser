import handler

from flask import Flask
app = Flask(__name__)

@app.route("/attack/<api_key>/<method>/<target>")
def attack(api_key, method, target):
	attack = handler.attacks[method]()
	return attack.attack()

if __name__ == "__main__":
    app.run()