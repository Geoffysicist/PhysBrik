import time

import adafruit_ble

from physbryk import PhysBrykServerAdvertisement
from physbryk import ControlService
from physbryk import DummyService, MotionService
from physbryk import DummySensor
# from adafruit_ble_adafruit.temperature_service import TemperatureService

# PyLint can't find BLERadio for some reason so special case it here.
ble = adafruit_ble.BLERadio()  # pylint: disable=no-member

connection = None

while True:
    print("Scanning for an PhysBryk Server advertisement...")
    for adv in ble.start_scan(PhysBrykServerAdvertisement, timeout=10):
        print(adv)
        # print(bytes(adv))
        print(f'Complete name: {adv.complete_name}')
        if adv.complete_name and ("PhysBryk" in adv.complete_name):
            connection = ble.connect(adv)
            print(f"Connected to PhysBryk {connection}")
            break

    # Stop scanning whether or not we are connected.
    ble.stop_scan()

    if connection and connection.connected:
        dummy_service = connection[DummyService]
        motion_service = connection[MotionService]
        control_service = connection[ControlService]
        
        
        while connection.connected:
            print("Dummy value: ", dummy_service.value)
            print("Acceleration values: ", motion_service.acceleration)
            print(f'Measurement period: {control_service.measurement_period}')
            control_service.measurement_period -= 5
            print(f'Measurement period: {control_service.measurement_period}')
            time.sleep(1)
