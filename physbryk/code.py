from adafruit_ble import BLERadio
from physbryk import PhysBrykServerAdvertisement
from physbryk import ControlService
from physbryk import DummyService, MotionService
from physbryk import DummySensor

import board
import time
import adafruit_lsm6ds.lsm6ds33 # motion
    

control_service = ControlService()
motion_svc = MotionService()
dummy_svc = DummyService()
dummy_svc.measurement_period = 100
last_update = 0

ble = BLERadio()

dummy_sensor = DummySensor()
motion = adafruit_lsm6ds.lsm6ds33.LSM6DS33(board.I2C())
        
adv = PhysBrykServerAdvertisement()
adv.complete_name = "PhysBrykAlpha"

while True:
    # Advertise when not connected.
    print('advertising...')
    ble.start_advertising(adv)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        now_msecs = time.monotonic_ns() // 1000000  # pylint: disable=no-member

        if now_msecs - last_update >= dummy_svc.measurement_period:
            motion_svc.acceleration = motion.acceleration # m/s/s
            dummy_svc.value = dummy_sensor.value
            dummy_sensor.update()
            last_update = now_msecs


print('done')