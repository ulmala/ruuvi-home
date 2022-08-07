from entities.sensor import Sensor
from repositories.sensor_repository import (
    sensor_repository as default_sensor_repository
)


class SensorService:
    def __init__(self, sensor_repository=default_sensor_repository):
        self._sensor_repository = default_sensor_repository

    def add_sensor(self, mac, name):
        self._sensor_repository.add(Sensor(mac, name))
