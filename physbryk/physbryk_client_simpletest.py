'''physbryl_client_simpletest

Connects to the physbryk and prints results for each of the core services
'''

import time

import adafruit_ble

from physbryk import PhysBrykClient

bryk = PhysBrykClient()
bryk.connect()

SAMPLE_PERIOD = 2000 # ms
last_update = 0

while bryk.connected():

    now_msecs = time.monotonic_ns() // 1000000  # pylint: disable=no-member

    if now_msecs - last_update >= SAMPLE_PERIOD:
        print(f"Bryk name: {bryk.getName()}")
        print(f"Battery status {bryk.get_battery():.2f} V")
        print("Bryk acceleration values: {:.2f} {:.2f} {:.2f} m/s/s".format(*bryk.getAcceleration()))
        print(f"Bryk net acceleration values: {bryk.getNetAcceleration():.3f} m/s/s")
        print("Bryk magnetometer values: {:.2f} {:.2f} {:.2f} rad/s".format(*bryk.getMagnetic()))
        print(f"Bryk light intensity: {bryk.get_lux():.2f} lux")
        print("Bryk spectral values (RGB): {} {} {}".format(*bryk.get_spectrum()))
        
        last_update = now_msecs

