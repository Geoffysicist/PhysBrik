"""PhysBryk module.

  Typical usage example:

  foo = SampleClass()
  
  bar = foo.public_method(required_variable, optional_variable=42)
"""

# DEBUG = True
# BOARD = True #flag indicating whether attached to a board.
# BASE_UUID = 'a0d1839c-0eaa-5b52-0000-818888dc7dc5'

# try:
#     import board
# except NotImplementedError:
#     # no board attached so mock sensors, services etc
#     import mock as mk
#     print('No valid board. Using mock sensors and services')
#     BOARD = False


# import adafruit_lsm6ds.lsm6ds33
# import time

from adafruit_ble_adafruit.adafruit_service import AdafruitServerAdvertisement

from adafruit_ble.characteristics import Characteristic
from adafruit_ble.characteristics.int import Int32Characteristic, Uint32Characteristic
from adafruit_ble.services import Service
from adafruit_ble.attributes import Attribute
from adafruit_ble import BLERadio

from adafruit_ble_adafruit.accelerometer_service import AccelerometerService

class PhysBrykService(Service): # does this have to be a service?
    """Common superclass for all PhysBryk board services."""

    @staticmethod
    # def adafruit_service_uuid(n):
    #     """Generate a VendorUUID which fills in a 16-bit value in the standard
    #     Adafruit Service UUID: ADAFnnnn-C332-42A8-93BD-25E905756CB8.
    #     """
    #     return VendorUUID("ADAF{:04x}-C332-42A8-93BD-25E905756CB8".format(n))

    @staticmethod
    def service_uuid(service_id):
        """generates a service uuid from a base uuid.

        the first 2 digits of the third 4 digit sequence is set to service_id
        the last will be used for characteristic uuids

        Args:
            service_id (hex int between 0x01 and 0xEE)

        Returns: 
            service_uuid (uuid)
        """
        
        service_uuid = service_uuid[:19] + f'{service_id:02x}' + service_uuid[21:]
        if DEBUG: print(service_uuid, type(service_uuid))
        service_uuid = VendorUUID(service_uuid)
        if DEBUG: print(service_uuid, type(service_uuid))
        return service_uuid

    @staticmethod
    def characteristicUUID(service_uuid, characteristic_id):
        """generates a characteristic uuid from a service uuid.

        the last 2 digits of the third 4 digit sequence is set to service_id
        
        Args:
            service_uuid (uuid)
            characteristic_id (hex int between 0x01 and 0xEE)

        Returns:
            characteristic_uuid (uuid)
        """

        characteristic_uuid = str(service_uuid)
        characteristic_uuid = characteristic_uuid[:21] + f'{characteristic_id:02x}' + characteristic_uuid[23:]
        if DEBUG: print(characteristic_uuid, type(characteristic_uuid))
        characteristic_uuid = uuid.UUID(characteristic_uuid)
        if DEBUG: print(characteristic_uuid, type(characteristic_uuid))
        return characteristic_uuid


    @classmethod
    def measurement_period_charac(cls, msecs=1000):
        """Create a measurement_period Characteristic for use by a subclass."""
        base_uuid = cls.baseUUID()
        mpc = Int32Characteristic(
            uuid=cls.characteristicUUID(base_uuid, 0x01),
            properties=(Characteristic.READ | Characteristic.WRITE),
            initial_value=msecs,
        )
        if DEBUG: print(mpc, type(mpc))
        return mpc

    @classmethod
    def service_version_charac(cls, version=1):
        """Create a service_version Characteristic for use by a subclass."""
        base_uuid = cls.baseUUID()
        svc = Uint32Characteristic(
            uuid=cls.characteristicUUID(base_uuid, 0x02),
            properties=Characteristic.READ,
            write_perm=Attribute.NO_ACCESS,
            initial_value=version,
        )
        if DEBUG: print(svc, type(svc))
        return svc

def main():
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


if __name__ == "__main__":
    main()


class SampleClass(object):
    """Summary of class here.

    Longer class information....
    
    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Longer description of desired functionality

        Args:
            required_variable: A required argument
            optional_variable: An optional argument

        Returns:
            None: but if it did you would describe it here

        Raises:
            NoError: but if it did you would describe it here
        """
        return None

def function_name(required_variable, optional_variable=None):
    """Short description.

    Longer description of desired functionality

    Args:
        required_variable: A required argument
        optional_variable: An optional argument

    Returns:
        None: but if it did you would describe it here

    Raises:
        NoError: but if it did you would describe it here
    """
    return None

 