from cassiadevtools.cassia_api import CassiaApi

import asyncio
from collections import defaultdict

API_DOMAIN_OR_IP_ADDRESS = '192.168.4.27'

async def scan_devices(api, filters, scanned_devices):
    await api.scan(filters, scanned_devices)

async def pair_devices(api, scanned_devices, paired_devices, paired_devices_lock):
    for scanned_dev in scanned_devices:
        pair_response = await api.pair(scanned_dev)
        async with paired_device_lock:
            for device_mac in paired_list:
                if device_mac not in paired_devices:
                    paired_devices[device_mac] = 'disconnected'

async def connect_devices(api, paired_devices):
    for paired_dev in paired_devices.items():
        if paired_dev[1] == 'disconnected':
            await api.connect(paired_dev[0])  # Use the device MAC address to connect.
            paired_devices[paired_dev[0]] = 'connected'


async def main():
    api = CassiaApi('container', API_DOMAIN_OR_IP_ADDRESS)
    paired_devices_lock = asyncio.Lock()
    paired_devices = {}  # value 0 for not connected, 1 for connected.
    scanned_devices = []
    scan_filters = ['filter_rssi=-70']
    await asyncio.gather(
        scan_devices(api, scan_filters, scanned_devices),
        pair_devices(api, scanned_devices, paired_devices, paired_devices_lock),
        connect_devices(api, paired_devices)
    )

if __name__ == '__main__':
    asyncio.run(main())
