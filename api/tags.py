from flask import abort
import time
import db


def read_all_associated(station_uuid):
	stations = db.get()

	if station_uuid in stations:
		#return list(stations[station_uuid]['tags'].values()) if stations[station_uuid]['tags'] else []
		return stations[station_uuid]['tags']
	else:
		abort(404, f'Station with id {id} not found')


def associate_with_station(station_uuid, body):
	stations = db.get()

	if station_uuid not in stations:
		abort(404, f'Station with id {station_uuid} not found')

	if not body or 'tag_uuid' not in body:
		abort(400, f'Tag id missing')

	tag_uuid = body['tag_uuid']

	# Remove tag from other station if already associated
	# This allows us to keep the state of the tag serverside
	existing_tag = None
	for _, station in stations.items():
		existing_tag = station['tags'].pop(tag_uuid, None)

		if existing_tag:
			break

	tag = existing_tag if existing_tag else body

	tag['last_seen'] = int(time.time())
	tag['previously_seen'] += 1

	stations[station_uuid]['tags'][tag_uuid] = tag

	db.set(stations)

	return tag


def read_all():
	stations = db.get()

	# I have no idea what this does 
	# It works and it's pythonic, so yeah?
	return [tag for station in stations.values() for tag in station['tags'].values()]


def read_one(tag_uuid):
	tags = read_all()
	tag = [tag for tag in tags if tag['tag_uuid'] == tag_uuid]

	if tag:
		return tag[0]
	else:
		abort(404, f'Tag with id {tag_uuid} not found' )