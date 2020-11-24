# PhysBryk

Small robust bluetooth microcontroller and sensors for conducting high school physics investigations based on the [Adafruit Feather nRF52840 Sense](https://learn.adafruit.com/adafruit-feather-sense/overview) and coded in [CircuitPython](https://circuitpython.org/libraries).

## Sensors

### On Board
- [LSM6DS33](https://learn.adafruit.com/lsm6ds33-6-dof-imu=accelerometer-gyro): 6-DoF IMU accelerometer + gyroscope
- [LIS3MDL](https://learn.adafruit.com/lis3mdl-triple-axis-magnetometer): Triple-axis Magnetometer
- [APDS9960](https://learn.adafruit.com/adafruit-apds9960-breakout): Proximity, Light, RGB and Gesture Sensor
- [PDM MEMS Microphone](https://learn.adafruit.com/adafruit-pdm-microphone-breakout)
- [SHT31-D]([Temperature & Humidity Sensor](https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout)): Temperature & Humidity Sensor
- [BMP280](https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout): Barometric Pressure + Temperature Sensor


### Accessory
- [INA260](https://learn.adafruit.com/adafruit-ina260-current-voltage-power-sensor-breakout): Current + Voltage + Power Sensor


## Bluetooth Services and Characteristics
Base uuid: a0d1nnnn-0eaa-5b52-bc84-818888dc7dc5



## Other helper guides
[ulab](https://learn.adafruit.com/ulab-crunch-numbers-fast-with-circuitpython): a numpy like library for faster data crunching
[Surface Mount is Easy](https://geoffg.net/SurfaceMount.html)

## Notes and resources

[Adafruit feather footprints ofr pcbs](https://github.com/adafruit/Adafruit-FeatherWing-Proto-Doubler-Tripler-and-Quad)

Prototype web app is [here on glitch](https://glitch.com/edit/#!/physbryk) but it is likely this will be abandoned in favour or an app based on jupyter

Circuit diagrams and other stuff [here on lucidchart](https://lucid.app/invitations/accept/f6d50b76-4089-42c6-90ed-853e881d3e9f)

For the Arduino version see [PhysBrykC](https://github.com/Geoffysicist/PhysBrykC) though this may also be abandoned

## TODO
See the [github repo projects](https://github.com/Geoffysicist/PhysBrykPy/projects)


## Imported libraries API references
- [Adafruit BLE Library](https://circuitpython.readthedocs.io/projects/ble/en/latest/#)
- [Adafruit BLE Adafruit Library](https://circuitpython.readthedocs.io/projects/ble_adafruit/en/latest/#)
- [ulab](https://circuitpython.readthedocs.io/en/latest/shared-bindings/ulab/)

- [Adafruit LSM6DS Library](https://circuitpython.readthedocs.io/projects/lsm6dsox/en/latest/)
- [Adafruit LSM6DS Library](https://circuitpython.readthedocs.io/projects/lsm6dsox/en/latest/)
- [ Adafruit APDS9960 Library](https://circuitpython.readthedocs.io/projects/apds9960/en/latest/)
- [ Adafruit SHT31D Library](https://circuitpython.readthedocs.io/projects/sht31d/en/latest/)
- [Adafruit BMP280 Library](https://circuitpython.readthedocs.io/projects/bmp280/en/latest/)
- [Adafruit INA260 Library](https://circuitpython.readthedocs.io/projects/ina260/en/latest/index.html)

