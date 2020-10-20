from adafruit_ble import BLERadio
from physbryk import PhysBrykServerAdvertisement
from physbryk import CoreService
from physbryk import DummySensor

import board
import time
import adafruit_lsm6ds.lsm6ds33 # motion
import adafruit_lis3mdl #magnetometer
    

core_service = CoreService()
last_update = 0

ble = BLERadio()
i2c = board.I2C()

# dummy_sensor = DummySensor()
motion = adafruit_lsm6ds.lsm6ds33.LSM6DS33(i2c)
magnetometer = adafruit_lis3mdl.LIS3MDL(i2c)        
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

        if now_msecs - last_update >= core_service.measurement_period:
            core_service.acceleration = motion.acceleration # m/s/s
            core_service.gyro = motion.gyro # rad/s
            core_service.magnetic = magnetometer.magnetic # uT
            # dummy_svc.value = dummy_sensor.value
            # dummy_sensor.update()
            last_update = now_msecs


print('done')