from flask import abort
import db

def read_all():
	return db.get()


def create(body):
	stations = db.get()
	
	uuid = body.get('station_uuid')
	name = body.get('name')

	# Make sure call is idempotent
	if not uuid or uuid in stations:
		abort(406, f'Location with uuid {uuid} already exists')

	# Create a new station
	stations[uuid] = {
		'station_uuid': uuid,
		'name': name,
		'tags': {}
	}

	db.set(stations)

	return stations[uuid], 201


def read_one(station_uuid):
	stations = db.get()

	if station_uuid in stations:
		return stations[station_uuid]
	else:
		abort(404, f'Location with uuid {station_uuid} not found')