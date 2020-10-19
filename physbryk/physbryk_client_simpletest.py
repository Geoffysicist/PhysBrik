import time

import adafruit_ble

from physbryk import PhysBrykServerAdvertisement
from physbryk import CoreService
# from physbryk import MotionService, MagnetService, EMRService, BatteryService
# from physbryk import DummyService, DummySensor
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
        core_service = connection[CoreService]
        # control_service = connection[MotionService]
        # control_service = connection[MagnetService]
        # control_service = connection[EMRService]
        # control_service = connection[BatteryService]
        # dummy_service = connection[DummyService]

        
        # print(connection._constructed_services.keys)
        # print(connection._constructed_services.items())
            
        
        
        while connection.connected:
        #     # print(adafruit_ble.decode_data(connection))
        #     print(connection.__dict__)
        #     print("Dummy value: ", dummy_service.value)
        #     print(f'type of {type(dummy_service)}')
            print("Acceleration values: ", core_service.acceleration)
        #     print(f'Measurement period: {control_service.measurement_period}')
        #     control_service.measurement_period -= 5
        #     print(f'Measurement period: {control_service.measurement_period}')
        #     time.sleep(1)
