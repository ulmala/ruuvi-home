from db_connection import get_db_connection
from entities.sensor import Sensor


class SensorReadingRepository:
    def __init__(self, con):
        self._con = con

    def insert_sensor_reading(self, sensor_reading):
        cur = self._con.cursor()
        cur.execute(
            '''insert into sensor_readings (
                data_format,
                humidity,
                temperature,
                pressure,
                acceleration,
                acceleration_x,
                acceleration_y,
                acceleration_z,
                tx_power,
                battery,
                movement_counter,
                measurement_sequence_number,
                mac,
                datetime) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (
                sensor_reading.data_format,
                sensor_reading.humidity,
                sensor_reading.temperature,
                sensor_reading.pressure,
                sensor_reading.acceleration,
                sensor_reading.acceleration_x,
                sensor_reading.acceleration_y,
                sensor_reading.acceleration_z,
                sensor_reading.tx_power,
                sensor_reading.battery,
                sensor_reading.movement_counter,
                sensor_reading.measurement_sequence_number,
                sensor_reading.mac,
                sensor_reading.datetime
            )
        )
        self._con.commit()

sensor_reading_repository = SensorReadingRepository(get_db_connection())