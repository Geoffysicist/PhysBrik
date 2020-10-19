import time

import adafruit_ble

from physbryk import DummyService, DummySensor
from physbryk import PhysBrykServerAdvertisement
# from adafruit_ble_adafruit.temperature_service import TemperatureService

# PyLint can't find BLERadio for some reason so special case it here.
ble = adafruit_ble.BLERadio()  # pylint: disable=no-member

connection = None

while True:
    print("Scanning for an PhysBryk Server advertisement...")
    for adv in ble.start_scan(PhysBrykServerAdvertisement, timeout=5):
        connection = ble.connect(adv)
        print("Connected")
        break

    # Stop scanning whether or not we are connected.
    ble.stop_scan()

    if connection and connection.connected:
        dummy_service = connection[DummyService]
        while connection.connected:
            print("Dummy value: ", dummy_service.value)
            print(f'Dummy nme: {dummy_service.name}')
            time.sleep(1)
