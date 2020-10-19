"""Scan for the PhysBryks and output a list of devices and services.
"""

import asyncio
from physbrykweb import physbrykweb as pb
from bleak import BleakClient


bryks = []

async def scan():
    _bryks = await pb.bryks_discover()
    for b in _bryks:
        bryks.append(b)


async def print_services(mac_addr: str):
    async with BleakClient(mac_addr) as client:
        svcs = await client.get_services()
        for s in svcs:
            print(s)
            for c in s.characteristics:
                print(c.uuid)

loop = asyncio.get_event_loop()
loop.run_until_complete(scan())

print(f'{len(bryks)} bryks found')
for b in bryks:
    print(f"{b.getName()} found @ {b.getAddress()}")

for b in bryks:
    loop.run_until_complete(print_services(b.getAddress()))

print('done')