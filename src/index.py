import datetime
import json
import time
from entities.sensor_reading import SensorReading
from repositories.sensor_reading_repository import sensor_reading_repository
from ruuvitag_sensor.ruuvi import RuuviTagSensor

MACS = [
    'D3:FD:F8:3E:33:67',
    'D9:2E:2A:EE:68:43'
]

TIMEOUT = 5

def main():
    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = RuuviTagSensor.get_data_for_sensors(MACS, TIMEOUT)
        for _, v in data.items():
            v['datetime'] = current_time
            reading = json.loads(
                json.dumps(v), object_hook=lambda d: SensorReading(**d)
            )
            sensor_reading_repository.insert_sensor_reading(reading)
        time.sleep(25)

if __name__ == "__main__":
    main()