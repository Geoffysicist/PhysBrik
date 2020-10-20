import time

import adafruit_ble

from physbryk import PhysBrykClient

bryk = PhysBrykClient()
bryk.connect()

while bryk.connected():
    print(f"Bryk name: {bryk.getName()}")
    print("Bryk acceleration values: {:.2f} {:.2f} {:.2f}".format(*bryk.getAcceleration()))
    print(f"Bryk net acceleration values: {bryk.getNetAcceleration():.3f}")
    print("Bryk magnetometer values: {:.2f} {:.2f} {:.2f}".format(*bryk.getMagnetic()))
    time.sleep(1)

