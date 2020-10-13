import physbryk as pb

DEBUG = True
BOARD = True #flag indicating whether attached to a board.
BASE_UUID = 'a0d1839c-0eaa-5b52-0000-818888dc7dc5'

try:
    import board
except NotImplementedError:
    # no board attached so mock sensors, services etc
    import mock as mk
    print('No valid board. Using mock sensors and services')
    BOARD = False


import adafruit_lsm6ds.lsm6ds33
import time

if BOARD: #valid board present
    # Accelerometer and gyro
    lsm6ds33 = adafruit_lsm6ds.lsm6ds33.LSM6DS33(board.I2C())
    
    # Create and initialize the available services.
    accel_svc = AccelerometerService()
    ble = BLERadio()
    adv = AdafruitServerAdvertisement()

else: #use mock sensors and services
    
    # Accelerometer and gyro
    lsm6ds33 = mk.Sensor()

    ble = mk.Service()
    accel_svc = mk.Service()
    adv = mk.Service()

ble.name = "PhysBryk"
accel_svc.measurement_period = 100 # millis

accel_last_update = 0

while True:
    # Advertise when not connected.
    ble.start_advertising(adv)
    if DEBUG: print('Connecting...')
    while not ble.connected:
        pass
    ble.stop_advertising()
    if DEBUG:
            print('Connected!')
    
    while ble.connected:
        now_msecs = time.monotonic_ns() // 1000000  # pylint: disable=no-member

        if now_msecs - accel_last_update >= accel_svc.measurement_period:
            accel_svc.acceleration = lsm6ds33.acceleration
            accel_last_update = now_msecs

            if DEBUG: print(accel_svc.acceleration)
            if not BOARD:
                for s in mk.sensors: s.update()

