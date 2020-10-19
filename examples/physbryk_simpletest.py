from adafruit_ble import BLERadio
from physbryk import PhysBrykServerAdvertisement, DummyService, DummySensor

import time

dummy_svc = DummyService()
dummy_svc.measurement_period = 100
dummy_last_update = 0

ble = BLERadio()

dummy_sensor = DummySensor()


# Unknown USB PID, since we don't know what board we're on
adv = PhysBrykServerAdvertisement()
adv.pid = 0x0000

while True:
    # Advertise when not connected.
    print(adv)
    print(bytes(adv))
    ble.start_advertising(adv)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        now_msecs = time.monotonic_ns() // 1000000  # pylint: disable=no-member

        if now_msecs - dummy_last_update >= dummy_svc.measurement_period:
            dummy_svc.value = dummy_sensor.value
            dummy_sensor.update()
            dummy_last_update = now_msecs


print('done')