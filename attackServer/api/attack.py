import handler
import json
import re

from flask import Flask
app = Flask(__name__)

@app.route("/attack/<api_key>/<method>/<target>/<length>")
def attack(api_key, method, target, length):
	access_keys = json.loads(open('keys.json', 'r').read())
	
	if api_key in access_keys['keys']:
		pass
	else:
		return json.dumps({'success': False, 'message': 'Sorry, your key is invalid! Fuck off hacker scum.'})
	
	if re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', target):
		pass
	else:
		return json.dumps({'success': False, 'message': 'Not a valid target. Please reconsider your life. :)'})

	#attack = handler.attacks[method]()
	#return attack.attack()

if __name__ == "__main__":
    app.run()