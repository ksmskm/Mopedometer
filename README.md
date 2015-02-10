# Mopedometer

A Raspberry Pi based data display & logger. Relies heavily on Adafruit products & libraries. Primarily designed to gather temperature data on Moped engines.

## Current status

Exhaust Gas Temp. sensor, display & logging is working.

TODO list:

0. integrating a thermistor to monitor cylinder head temp. requires logarthmic curve tuning in software & an analog to digital converter integrated circuit.

1. restructure modules & organize program to run completely of onboard buttons & power switch.

2. beef up data visualization capabilities.

Still heavily wired :(

## Goal

User friendly dash mounted Mopedometer with a minimum of wires (hint: wifi connectivity & database server)

## Links

[Thermocouple Library](https://learn.adafruit.com/max31855-thermocouple-python-library)

[Analog-to-Digital Docs](https://gist.github.com/ladyada/3151375)

[Display Library](https://learn.adafruit.com/rgb-lcd-shield)
