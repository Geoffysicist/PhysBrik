"""Scan for the PhysBryks and return a list of devices found.
"""

import asyncio
from physbrykweb import physbrykweb as pb

bryks = []

async def run():
    bryks = await pb.bryks_discover()
    if len(bryks):
        for b in bryks:
            print(f'{b.getName()} found @ {b.getAddress()}')
    else:
        print('No PhysBryk found')

    
    print(len(bryks))

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
