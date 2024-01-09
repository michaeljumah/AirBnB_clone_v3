# api/v1/views/places_amenities.py
from flask import jsonify, abort
from api.v1.views import app_views
from models import storage, Place, Amenity

@app_views.route('/places/<place_id>/amenities', methods=['GET'], strict_slashes=False)
def get_place_amenities(place_id):
    '''gets the place amenity id'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    
    if storage.__class__.__name__ == 'DBStorage':
        amenities = [amenity.to_dict() for amenity in place.amenities]
    else:
        amenity_ids = place.amenity_ids
        amenities = [storage.get(Amenity, amenity_id).to_dict() for amenity_id in amenity_ids]
    
    return jsonify(amenities)

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    '''deletes the object amenity '''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    
    if storage.__class__.__name__ == 'DBStorage':
        if amenity not in place.amenities:
            abort(404)
        place.amenities.remove(amenity)
        storage.save()
    else:
        if amenity_id not in place.amenity_ids:
            abort(404)
        place.amenity_ids.remove(amenity_id)
        storage.save()
    
    return jsonify({}), 200

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'], strict_slashes=False)
def link_place_amenity(place_id, amenity_id):
    '''links amenity objects'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    if storage.__class__.__name__ == 'DBStorage':
        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        place.amenities.append(amenity)
        storage.save()
    else:
        if amenity_id in place.amenity_ids:
            return jsonify(amenity.to_dict()), 200
        place.amenity_ids.append(amenity_id)
        storage.save()

    return jsonify(amenity.to_dict()), 201
