from pydantic import basemodel

class Cords(basemodel):
    fence_code: str
    latitude: float
    longitude: float