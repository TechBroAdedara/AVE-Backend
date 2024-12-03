# Copyright (c) [2024] [Adedara Adeloro].
# Licensed for non-commercial use only. For details, see the LICENSE file.

from datetime import datetime

from pydantic import BaseModel, EmailStr


class GeofenceCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    radius: float
    fence_type: str
    start_time: datetime
    end_time: datetime

    class Config:
        from_attributes = True
