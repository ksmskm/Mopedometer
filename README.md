# Mopedometer

A Raspberry Pi based data display & logger. Relies heavily on Adafruit products & libraries. Primarily designed to gather temperature data on Moped engines.

## Current status

Exhaust Gas Temp. sensor, display, logging & server are working. topics are being worked on as available parts & schedule permit.

TODO list:

* integrating a thermistor to monitor cylinder head temp. requires logarithmic curve tuning in software & an analog to digital converter integrated circuit (this step is well underway)

* restructure modules & organize program to run completely from onboard buttons & power switch (underway).

* beef up data visualization capabilities.

* integrate Realtime-Clock to improve data logging.

## Goal

User friendly dash mounted Mopedometer with a minimum of wires (hint: wifi connectivity & database server with graphing support)

## Links

[Thermocouple Library](https://learn.adafruit.com/max31855-thermocouple-python-library)

[Analog-to-Digital resources](https://gist.github.com/ladyada/3151375)

[Display Library](https://learn.adafruit.com/rgb-lcd-shield)
