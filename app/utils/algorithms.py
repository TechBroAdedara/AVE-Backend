# ----------------------------------------Geolocation Logic/Algorithm--------------------------------------------
import math
import random
import string

from app.models.geofence import Geofence


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    )
    return (
        2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a)) * 1000
    )  # Convert to meters


def check_user_in_circular_geofence(user_lat, user_lng, geofence: Geofence):
    latitude = geofence.latitude
    longitude = geofence.longitude
    radius = geofence.radius
    distance = haversine(user_lat, user_lng, latitude, longitude)
    return distance <= radius


def generate_alphanumeric_code(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

