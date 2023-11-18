import json
from pathlib import Path

fn = Path(__file__).parent / 'db.json'


DB_FILE = Path(__file__).parent / 'db.json'

def get():
	content = None
	with open(DB_FILE, 'r') as file: 
		content = json.load(file)

	return content
	

def set(content):
	with open(DB_FILE, 'w') as file: 
		file.write(json.dumps(content))