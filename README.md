# Mopedometer

A Raspberry Pi based data display & logger. Relies heavily on Adafruit products & libraries. Primarily designed to gather temperature data on Moped engines. The Design is oriented toward some specifc requests of the client (my cousin) & is currently far ahead of other parts of the project.

## Current branches

* master: consists of working prototypes for all topics & retains some code that won't be used (cylinder.py will change due a new circuit plan).

* database: is for developing a more user friendly database format. Ideally, seperate runs will be browsable from the server & some significant db queries will be available. 

## TODO list:

* setup RPi as wifi access point for direct connection on the track

* switch from thermistor to an all-digital circuit 

* beef up data visualization capabilities.

* integrate Realtime-Clock to improve data logging.

## Goal

User friendly dash mounted Mopedometer with a minimum of wires (hint: wifi connectivity & database server with graphing support)

## Links

[Thermocouple Library](https://learn.adafruit.com/max31855-thermocouple-python-library)

[Analog-to-Digital resources](https://gist.github.com/ladyada/3151375)

[Display Library](https://learn.adafruit.com/rgb-lcd-shield)

[graphing Library](http://matplotlib.org/)
test
