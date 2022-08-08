from db_connection import get_db_connection
from entities.sensor import Sensor
from sqlite3 import IntegrityError


class SensorRepository:
    def __init__(self, con):
        self._con = con

    def add(self, sensor):
        cur = self._con.cursor()
        try:
            cur.execute(
                'insert into sensors (mac, name) values (?, ?)',
                (sensor.mac, sensor.name)
            )
            self._con.commit()
        except IntegrityError:
            print(f'Sensor with MAC: {sensor.mac} already exsits!')

    def get_all_sensors(self):
        cur = self._con.cursor()
        cur.execute('select * from sensors')
        rows = cur.fetchall()
        if len(rows) == 0:
            return []
        return [Sensor(row['mac'], row['name']) for row in rows]


sensor_repository = SensorRepository(get_db_connection())