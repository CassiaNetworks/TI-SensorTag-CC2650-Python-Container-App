from cassiadevtools.cassia_api import CassiaApi

import asyncio


async def scan_devices(api):
    await api.scan()

async def connect_devices(api):
    await api.connect()

async def main():
    api = CassiaApi('container', '192.168.4.27')
    await asyncio.gather(scan_devices(api), connect_devices(api))

if __name__ == '__main__':
    asyncio.run(main())
