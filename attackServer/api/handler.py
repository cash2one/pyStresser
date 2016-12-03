import sys
import os
import json

class udp():
	def __init__(self):
		return

	def attack(self, target, method, time):
		try:
			return json.dumps({'success': True, 'message': 'Attack launched on %s using %s for %s seconds.'%(target, method, time)})
		except:
			return json.dumps({'success': False, 'message': 'Launching attack failed, unsure why.'})

attacks = {
	'udp': udp,
}