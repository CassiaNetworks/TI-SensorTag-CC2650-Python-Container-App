"""This module contains a class that interfaces with the Cassia RESTful API.

The CassiaApi class contains methods that interface with the
Cassia RESTful API for the container, router, and AC.

  The api_type parameter

  Typical usage example:

  cassia_api = CassiaApi('router', '10.10.10.254')

TODO: Add more Cassia RESTful API methods.
"""

from enum import Enum
from aiohttp_sse_client import client as sse_client
import asyncio
import json

class CassiaApi:
    CONTAINER_ADDRESS = "10.10.10.254";
    class ApiType(Enum):
        CONTAINER = 'container'
        ROUTER = 'gateway'
        AC = 'ac'

    def __init__(self, api_type, api_domain=CONTAINER_ADDRESS, api_url_protocol='http'):
        try:
            self.ApiType(api_type)

        except ValueError as ve:
            print(ve)
            print("Please provide a valid api_type value:"
                  "'container', 'router', 'ac'")
        else:
            self.api_type = api_type

        self.api_domain = api_domain
        self.api_url_protocol = api_url_protocol
        self.__is_sse_scan = False
        self.__is_sse_notify = False
        self.__ac_access_token = ''

    async def scan(self, filters, scanned_devices=[]):
        sse_url = ''.join([
                    self.api_url_protocol, '://',
                    self.api_domain,
                    '/gap/nodes?event=1'
                ])

        if len(filters):
            sse_url = sse_url + '&' + '&'.join(filters)

        async with sse_client.EventSource(sse_url) as event_source:
            try:
                async for event in event_source:
                    data = json.loads(event.data)
                    scanned_devices.append(data['bdaddrs'][0]['bdaddr'])
                    print(data['bdaddrs'][0]['bdaddr'])
            except ConnectionError as e:
                print(e)
                sse_client.resp.close()

    async def pair(self, devices):
        print('pair')
        pass

    async def connect(self):
        print('connect')
        pass

    async def disconnect(self):
        print('disconnect')
        pass

    async def read(self):
        print('read')
        pass
