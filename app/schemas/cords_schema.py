# Copyright (c) [2024] [Adedara Adeloro].
# Licensed for non-commercial use only. For details, see the LICENSE file.

from pydantic import basemodel

class Cords(basemodel):
    fence_code: str
    latitude: float
    longitude: float