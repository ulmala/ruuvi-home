from dataclasses import dataclass, field

@dataclass
class Sensor:
    mac: str
    name: str
    full_mac: str = field(init=False)

    def __post_init__(self):
        self.full_mac = ':'.join(self.mac[i : i + 2] for i in range(0,12,2)).upper()
