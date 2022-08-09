import datetime
import json
from entities.sensor_reading import SensorReading
from ruuvitag_sensor.ruuvi import RuuviTagSensor
from services.sensor_service import sensor_service


TIMEOUT = 10

def main():
    macs = [sensor.full_mac for sensor in sensor_service.all_sensors()]
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = RuuviTagSensor.get_data_for_sensors(macs, TIMEOUT)
    for _, v in data.items():
        v['datetime'] = current_time
        reading = json.loads(
            json.dumps(v), object_hook=lambda d: SensorReading(**d)
        )
        sensor_service.insert_sensor_reading(reading)

if __name__ == "__main__":
    main()