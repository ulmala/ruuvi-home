import datetime
import json
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
        data = RuuviTagSensor.get_data_for_sensors(MACS, TIMEOUT)
        for _, v in data.items():
            v['datetime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            reading = json.loads(
                json.dumps(v), object_hook=lambda d: SensorReading(**d)
            )
            sensor_reading_repository.insert_sensor_reading(reading)

if __name__ == "__main__":
    main()