import time

import adafruit_ble

from physbryk import PhysBrykClient

bryk = PhysBrykClient()
bryk.connect()

while bryk.connected():
    print(f"Bryk name: {bryk.getName()}")
    print(f"Battery status {bryk.get_battery():.2f} V")
    print("Bryk acceleration values: {:.2f} {:.2f} {:.2f} m/s/s".format(*bryk.getAcceleration()))
    print(f"Bryk net acceleration values: {bryk.getNetAcceleration():.3f} m/s/s")
    print("Bryk magnetometer values: {:.2f} {:.2f} {:.2f} rad/s".format(*bryk.getMagnetic()))
    time.sleep(2)

