import asyncio
import struct
from bleak import discover, BleakClient # BleakScanner


class PhysBryk(object):
    
    def __init__(self, device=None):
        '''deivce is a PnysBryk BLE device'''
        self._device = device
    
    def setDevice(self, ble_device):
        self._device = ble_device
        
    def getAddress(self):
        return self._device.address

    def getName(self):
        return self._device.name

async def bryks_discover():
    """Discover all PhysBryks.
    
    Returns: list of all discovered PhysBryks
    """
    bryks = []
    print('Searching...')
    devices = await discover()
    print(f'{len(devices)} BLE devices found')
    
    for d in devices:
        if 'PhysBryk' in d.name:
            b = PhysBryk(d)
            bryks.append(b)
    
    return bryks
    
