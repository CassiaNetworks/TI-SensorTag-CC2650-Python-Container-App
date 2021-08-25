from cassiadevtools.cassia_api import CassiaApi
from collections import defaultdict
import asyncio
import shutil
import os
import warnings
import sys

# Data file size limits are in bytes.
SIZE_100KB = 100000
SIZE_500KB = 500000
SIZE_1MB = 1000000
SIZE_10MB = 10000000
SIZE_100MB = 100000000
SIZE_500MB = 500000000

DATA_FILE_SIZE_LIMIT = SIZE_100KB
MAX_USED_STORAGE_RATIO = 0.7

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


async def write_results_to_file(data, data_file_num_state):
    total, used, free = shutil.disk_usage("/")
    data_dir_path = '../data'
    data_file_count = 3
    cur_data_file_count = 0

    try:
        os.mkdir(data_dir_path)
    except FileExistsError as e:
        pass
    except Exception as e:
        print(e)
        exit()

    while (os.path.isfile(data_dir_path + 
           '/data{count}.txt'.format(count=data_file_num))):
        data_file_num += 1

    if data_file_num == 1:
        file_str = (
            '{path}/data{count}.txt'.format(path=data_dir_path, 
                                            count=data_file_num))        
        with open(file_str,'x'):
                print('Created data file: {}'.format(file_str))
    else:
        data_file_num -= 1

    while cur_data_file_count < data_file_count:
        if used < total * MAX_USED_STORAGE_RATIO:
            if (sys.getsizeof(data) + os.path.getsize(
                '{path}/data{count}.txt'.format(
                    path=data_dir_path,
                    count=data_file_num)) >= DATA_FILE_SIZE_LIMIT):

                data_file_num += 1
                file_str = (
                    '{path}/data{count}.txt'.format(path=data_dir_path, 
                                                    count=data_file_num))
                with open(file_str,'x'):
                    print('Created data file: {}'.format(file_str))

                cur_data_file_count += 1

            file_str = (
                '{path}/data{count}.txt'.format(path=data_dir_path, 
                                                count=data_file_num))

            with open(file_str, 'a') as data_file:
                data_file.write(data)
        else:
            warnings.warn(
                ('Storage is {}"%" used! Data files cannot be created until '
                 'space is freed.').format(MAX_USED_STORAGE_RATIO * 100),
                ResourceWarning)

async def main():
    api = CassiaApi('container', API_DOMAIN_OR_IP_ADDRESS)
    paired_devices_lock = asyncio.Lock()
    paired_devices = {}  # value 0 for not connected, 1 for connected.
    scanned_devices = []
    # The active=1 filter allows the Scan API to show the "CC2650 SensorTag" name
    # in scan results. Using the filter_name filter, we can just match the
    # first part of the name using the pattern "CC2650*".
    scan_filters = ['active=1', 'filter_rssi=-70', 'filter_name=CC2650*']
    await asyncio.gather(
        scan_devices(api, scan_filters, scanned_devices),
        pair_devices(api, scanned_devices, paired_devices, paired_devices_lock),
        connect_devices(api, paired_devices)
    )

if __name__ == '__main__':
    asyncio.run(main())
