import pandas as pd
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

    def get_sensor_readings(self, sensor):
        sql = f'''
            SELECT * FROM sensor_readings
            WHERE mac = '{sensor.mac}'
        '''
        df = pd.read_sql_query(sql, self._con)
        return df

sensor_repository = SensorRepository(get_db_connection())