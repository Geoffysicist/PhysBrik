"""Module1 - A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = SampleClass()
  
  bar = foo.public_method(required_variable, optional_variable=42)
"""

import uuid
from adafruit_ble.characteristics import Characteristic
from adafruit_ble.characteristics.int import Int32Characteristic, Uint32Characteristic
from adafruit_ble.services import Service
from adafruit_ble.attributes import Attribute


DEBUG = True

class PhysBrykService(Service): # does this have to be a service?
    """Common superclass for all Adafruit board services."""

    @staticmethod
    # def adafruit_service_uuid(n):
    #     """Generate a VendorUUID which fills in a 16-bit value in the standard
    #     Adafruit Service UUID: ADAFnnnn-C332-42A8-93BD-25E905756CB8.
    #     """
    #     return VendorUUID("ADAF{:04x}-C332-42A8-93BD-25E905756CB8".format(n))

    def baseUUID(url='https://github.com/Geoffysicist/PhysBrykPy'):
        """generates a base uuid from a url.

        the third 4 digit sequence is set to 0x0000
        the first 2 digit of this sequence will be used for service uuids
        the last will be used for characteristic uuids

        Args:
            url (string)

        Returns:
            base_uuid (uuid)
        """
        base_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, url)
        base_uuid = str(base_uuid)
        base_uuid = base_uuid.replace(base_uuid[19:23],"0000")
        base_uuid = uuid.UUID(base_uuid)
        if DEBUG: print(base_uuid, type(base_uuid))
        return base_uuid

    @staticmethod
    def serviceUUID(base_uuid, service_id):
        """generates a service uuid from a base uuid.

        the first 2 digits of the third 4 digit sequence is set to service_id
        the last will be used for characteristic uuids

        Args:
            service_id (hex int between 0x01 and 0xEE)

        Returns: 
            service_uuid (uuid)
        """
        
        service_uuid = str(base_uuid)
        service_uuid = service_uuid[:19] + f'{service_id:02x}' + service_uuid[21:]
        if DEBUG: print(service_uuid, type(service_uuid))
        service_uuid = uuid.UUID(service_uuid)
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





def baseUUID(url='https://github.com/Geoffysicist/PhysBrykPy'):
    """generates a base uuid from a url.

    the third 4 digit sequence is set to 0x0000
    the first 2 digit of this sequence will be used for service uuids
    the last will be used for characteristic uuids

    Args:
        url (string)

    Returns:
        base_uuid (uuid)
    """

    base_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, url)
    base_uuid = str(base_uuid)
    base_uuid = base_uuid.replace(base_uuid[19:23],"0000")
    base_uuid = uuid.UUID(base_uuid)
    if DEBUG: print(base_uuid, type(base_uuid))
    return base_uuid

def serviceUUID(service_id, base_uuid=baseUUID()):
    """generates a service uuid from a base uuid.

    the first 2 digits of the third 4 digit sequence is set to service_id
    the last will be used for characteristic uuids

    Args:
        base_uuid (uuid)
        service_id (hex int between 0x01 and 0xEE)

    Returns: 
        service_uuid (uuid)
    """

    service_uuid = str(base_uuid)
    service_uuid = service_uuid[:19] + f'{service_id:02x}' + service_uuid[21:]
    if DEBUG: print(service_uuid, type(service_uuid))
    service_uuid = uuid.UUID(service_uuid)
    if DEBUG: print(service_uuid, type(service_uuid))
    return service_uuid

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


def main():
    this_base_uuid = PhysBrykService.baseUUID()
    this_service_uuid = PhysBrykService.serviceUUID(this_base_uuid, 0x01)
    this_characteristic_uuid = PhysBrykService.characteristicUUID(this_service_uuid, 0x0e)
    PhysBrykService.measurement_period_charac()
    PhysBrykService.service_version_charac()

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

 