from entities.sensor import Sensor
from repositories.sensor_repository import (
    sensor_repository as default_sensor_repository
)
from repositories.sensor_reading_repository import (
    sensor_reading_repository as default_sensor_reading_repository
)


class SensorService:
    def __init__(self,
                 sensor_repository=default_sensor_repository,
                 sensor_reading_repository=default_sensor_reading_repository):
        self._sensor_repository = sensor_repository
        self._sensor_reading_repository = sensor_reading_repository

    def add_sensor(self, mac, name):
        self._sensor_repository.add(Sensor(mac, name))

    def all_sensors(self):
        sensors = self._sensor_repository.get_all_sensors()
        return sensors

    def insert_sensor_reading(self, reading):
        self._sensor_reading_repository.insert_sensor_reading(reading)

    def get_readings(self, sensor):
        return self._sensor_repository.get_sensor_readings(sensor)

sensor_service = SensorService()
