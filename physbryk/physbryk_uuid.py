import uuid

DEBUG = True


def baseUUID(url):
    """generates a base uuid from a url.

    the third 4 digit sequence is set to 0x0000
    the first 2 digit of this sequence will be used for service uuids
    the last will be used for characteristic uuids

    Args: url (string)

    Returns: base_uuid (uuid)
    """

    base_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, url)
    print(base_uuid)
    base_uuid = str(base_uuid)
    base_uuid = base_uuid.replace(base_uuid[19:23],"0000")
    base_uuid = uuid.UUID(base_uuid)
    if DEBUG: print(base_uuid, type(base_uuid))
    return base_uuid

def serviceUUID(base_uuid, service_id):
    """generates a service uuid from a base uuid.

    the first 2 digits of the third 4 digit sequence is set to service_id
    the last will be used for characteristic uuids

    Args:
        base_uuid (uuid)
        service_id (hex int between 0x01 and 0xEE)

    Returns: service_uuid (uuid)
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

    Returns: characteristic_uuid (uuid)
    """

    characteristic_uuid = str(service_uuid)
    characteristic_uuid = characteristic_uuid[:21] + f'{characteristic_id:02x}' + characteristic_uuid[23:]
    if DEBUG: print(characteristic_uuid, type(characteristic_uuid))
    characteristic_uuid = uuid.UUID(characteristic_uuid)
    if DEBUG: print(characteristic_uuid, type(characteristic_uuid))
    return characteristic_uuid


def main():
    this_base_uuid = baseUUID('https://github.com/Geoffysicist/PhysBrykPy')

    this_service_uuid = serviceUUID(this_base_uuid, 0x01)
    this_characteristic_uuid = characteristicUUID(this_service_uuid, 0x0e)

if __name__ == "__main__":
    main()

