# TI SensorTag CC2650STK Container App Example (Python3) - Scan, Pair, Connect, and Read


This Python application is for the Cassia Gateway Container v2.0.1 and above.

Download the v2.0.1 container here: [ubuntu_XE1000_2.0.1.tar.gz](https://www.cassianetworks.com/download/firmware/container/ubuntu_XE1000_2.0.1.tar.gz)

This application should run with Python 3.5.3 and above, but it is recommended to run with Python 3.6 and above.

This application uses the [Cassia SDK and Cassia RESTful API](https://github.com/CassiaNetworks/CassiaSDKGuide/wiki).

The device referenced in this sample appliaction is the [TI SensorTag CC2650STK](https://www.ti.com/tool/CC2650STK).

<br>

Here is what needs to be done before running this application:
 
1. Download the v2.0.1 container here:
https://www.cassianetworks.com/download/firmware/container/ubuntu_XE1000_2.0.1.tar.gz

2. Download the SamplePython3App.1.0.tar.gz file or build it yourself using the package.sh script located in the example app main directory.

3. Install the v2.0.1 container locally on the gateway webpage:
* Log in to the gateway webpage.
* Go to the Container tab.
* Click on Select File, and select the downloaded v2.0.1 container.
* Click on Install, and wait for the container to install.
* Refresh the page, and the container page should show up.
* Wait for the Container Status to change to "running". Refresh the page to check.

4. Scroll down to Install APP.

5. Click on Select File and select the SamplePython3App.1.0.tar.gz file.

6. Click on Install.

7. Wait for the app to finish installing. The gateway will reboot.

8. After the reboot, go back to the Container tab to see the processes running on the container.

9. Your application process shoudl show up under the "Programs in operation" section.

10. That's all! The app is running.