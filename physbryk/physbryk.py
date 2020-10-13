"""PhysBryk module.
Services & Characteristics
MotionService       100
    acceleration    101
    gyro            102
MagnetometerService 200
    magnetic        201
EMRService          300
    intensity       301
    spectrum        302
    proximity       303
    

Base uuid for PhysBryk is a0d1839c-0eaa-5b52-bc84-818888dc7dc5

  Typical usage example:

  foo = SampleClass()
  
  bar = foo.public_method(required_variable, optional_variable=42)
"""

import random as rn
import struct

from micropython import const

from adafruit_ble.advertising import Advertisement, LazyObjectField
from adafruit_ble.advertising.standard import ManufacturerData, ManufacturerDataField
from adafruit_ble.characteristics import Characteristic, StructCharacteristic
from adafruit_ble.characteristics.int import Int32Characteristic, Uint32Characteristic, Uint16Characteristic
from adafruit_ble.characteristics.float import FloatCharacteristic
from adafruit_ble.uuid import VendorUUID
from adafruit_ble.services import Service
from adafruit_ble.attributes import Attribute
from adafruit_ble import BLERadio

from adafruit_ble_adafruit.adafruit_service import AdafruitService

_MANUFACTURING_DATA_ADT = const(0xFF)
_ADAFRUIT_COMPANY_ID = const(0x0822)
_PID_DATA_ID = const(0x0001)  # This is the same as the Radio data id, unfortunately.

MEASUREMENT_PERIOD = 100

class PhysBrykServerAdvertisement(Advertisement):
    """Advertise the Adafruit company ID and the board USB PID.

    TODO find how to change this from the Adafruit one for a more general advertisement.
    """

    match_prefixes = (
        struct.pack(
            "<BHBH",
            _MANUFACTURING_DATA_ADT,
            _ADAFRUIT_COMPANY_ID,
            struct.calcsize("<HH"),
            _PID_DATA_ID,
        ),
    )
    manufacturer_data = LazyObjectField(
        ManufacturerData,
        "manufacturer_data",
        advertising_data_type=_MANUFACTURING_DATA_ADT,
        company_id=_ADAFRUIT_COMPANY_ID,
        key_encoding="<H",
    )
    pid = ManufacturerDataField(_PID_DATA_ID, "<H")
    """The USB PID (product id) for this board."""

    def __init__(self):
        super().__init__()
        self.connectable = True
        self.flags.general_discovery = True
        self.flags.le_only = True


class PhysBrykService(Service):
    """Common superclass for all PhysBryk board services."""

    @staticmethod
    def physbryk_service_uuid(n):
        """Generate a VendorUUID which fills in a 16-bit value in the standard
        PhysBryk Service UUID: a0d1839c-0eaa-5b52-nnnn-818888dc7dc5.
        """
        # return VendorUUID("ADAF{:04x}-C332-42A8-93BD-25E905756CB8".format(n))
        return VendorUUID('a0d1{:04x}-0eaa-5b52-bc84-818888dc7dc5'.format(n))

    @classmethod
    def measurement_period_charac(cls, msecs=MEASUREMENT_PERIOD):
        """Create a measurement_period Characteristic for use by a subclass."""
        return Int32Characteristic(
            uuid=cls.physbryk_service_uuid(0x0001),
            properties=(Characteristic.READ | Characteristic.WRITE),
            initial_value=msecs,
        )

    @classmethod
    def service_version_charac(cls, version=1):
        """Create a service_version Characteristic for use by a subclass."""
        return Uint32Characteristic(
            uuid=cls.physbryk_service_uuid(0x0002),
            properties=Characteristic.READ,
            write_perm=Attribute.NO_ACCESS,
            initial_value=version,
        )


class MotionService(PhysBrykService):  # pylint: disable=too-few-public-methods
    """Accelerometer and Gyroscope values."""

    uuid = PhysBrykService.physbryk_service_uuid(0x100)
    acceleration = StructCharacteristic(
        "<fff",
        uuid=PhysBrykService.physbryk_service_uuid(0x101),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Tuple (x, y, z) float acceleration values, in m/s^2"""

    gyro = StructCharacteristic(
        "<fff",
        uuid=PhysBrykService.physbryk_service_uuid(0x102),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Tuple (x, y, z) float gyroscope values, in rad/s"""
    measurement_period = PhysBrykService.measurement_period_charac()
    """Initially 1000ms."""


class MagnetometerService(PhysBrykService):  # pylint: disable=too-few-public-methods
    """Magnetometer values."""

    uuid = PhysBrykService.physbryk_service_uuid(0x200)
    magnetic = StructCharacteristic(
        "<fff",
        uuid=PhysBrykService.physbryk_service_uuid(0x201),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Tuple (x, y, z) float magnetometer values, in micro-Teslas (uT)"""
    
    measurement_period = PhysBrykService.measurement_period_charac()
    """Initially 1000ms."""


class EMRService(PhysBrykService):  # pylint: disable=too-few-public-methods
    """Light sensor value."""

    uuid = PhysBrykService.physbryk_service_uuid(0x300)

    intensity = FloatCharacteristic(
        uuid=PhysBrykService.physbryk_service_uuid(0x301),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Uncalibrated light level (float)"""

    spectrum = StructCharacteristic(
        "<fff",
        uuid=PhysBrykService.physbryk_service_uuid(0x302),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Tuple (r, g, b) red/green/blue color values, each in range 0-65535 (16 bits)"""

    proximity = Uint16Characteristic(
        uuid=PhysBrykService.physbryk_service_uuid(0x303),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        read_perm=Attribute.OPEN,
        write_perm=Attribute.NO_ACCESS,
    )
    """
    A higher number indicates a closer distance to the sensor.
    The value is unit-less.
    """

    measurement_period = PhysBrykService.measurement_period_charac()
    """Initially 1000ms."""


class DummyService(PhysBrykService):  # pylint: disable=too-few-public-methods
    """Random Data values."""

    uuid = PhysBrykService.physbryk_service_uuid(0x1000)
    value = StructCharacteristic(
        "<fff",
        uuid=PhysBrykService.physbryk_service_uuid(0x1001),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Tuple (x, y, z) random values between 1 and 100"""

    measurement_period = PhysBrykService.measurement_period_charac()
    """Initially 1000ms."""


class DummySensor(object):
    """Creates a dummy sensor which generates a tuple of 3 random numbers.
    """

    def __init__(self, likes_spam=False):
        self.name = "Dummy_Sensor"
        self.value = ()
        self.update()

    def update(self):
        """updates all the sensor values
        """
        self.value = (rn.randrange(16), rn.randrange(16), rn.randrange(16))

def main():
    DEBUG = True
    BOARD = True #flag indicating whether attached to a board.

    try:
        import board
    except NotImplementedError:
        # no board attached so mock sensors, services etc
        import mock as mk
        print('No valid board. Using mock sensors and services')
        BOARD = False

    # sensors
    import adafruit_lsm6ds.lsm6ds33 # motion
    import adafruit_lis3mdl # magnetometer
    import adafruit_apds9960.apds9960 # EMR

    import time

    dummy_sensor = DummySensor()

    if BOARD: # valid board present use real sensors
        motion = adafruit_lsm6ds.lsm6ds33.LSM6DS33(board.I2C())
        magnetic = adafruit_lis3mdl.LIS3MDL(board.I2C())
        emr = adafruit_apds9960.apds9960.APDS9960(board.I2C())
        # emr.enable_proximity = True
        emr.enable_color = True

        
        # Create and initialize the available services.
        motion_svc = MotionService()
        magnetic_svc = MagnetometerService()
        emr_svc = EMRService()
        dummy_svc = DummyService()
        ble = BLERadio()
        adv = PhysBrykServerAdvertisement()

    else: #use mock sensors and services
        
        # Accelerometer and gyro
        motion = mk.Sensor()
        magnetic = mk.Sensor()
        emr = mk.Sensor()

        ble = mk.Service()
        motion_svc = mk.Service()
        magnetic_svc = mk.Service()
        emr_svc = mk.Service()
        dummy_svc = mk.Service()
        adv = mk.Service()


    ble.name = "PhysBryk"
    # accel_svc.measurement_period = 100 # millis

    last_update = 0
    

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

            if now_msecs - last_update >= MEASUREMENT_PERIOD:
                motion_svc.acceleration = motion.acceleration
                motion_svc.gyro = motion.gyro
                magnetic_svc.magnetic = magnetic.magnetic
                r, g, b, c = emr.color_data
                emr_svc.intensity = c
                emr_svc.spectrum = (r, g, b)
                emr_svc.proximity = emr.proximity
                dummy_svc.value = dummy_sensor.value
                dummy_sensor.update()
                last_update = now_msecs

                if DEBUG:
                    print(f'motion acceleration: {motion_svc.acceleration}')
                    print(f'motion gyro: {motion_svc.gyro}')
                    print(f'magnetic magnetic: {magnetic_svc.magnetic}')
                    print(f'emr intensity: {emr_svc.intensity}')
                    print(f'emr spectrum: {emr_svc.spectrum}')
                    print(f'emr proximity: {emr_svc.proximity}')
                    print(f'dummy: {dummy_svc.value}')
                if not BOARD:
                    for s in mk.sensors: s.update()



if __name__ == "__main__":
    main()

