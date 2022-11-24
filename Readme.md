# Library for reading serial data

Python library for reading serial off Chargery BMS

## Requirements

- Chargery BMS
- I2C serial adapter
- Python serial lib

## Command Line Parameters

**TODO**: FIX more

"""params and their usage here

"""

## License

**TODO**: FIX here

- MIT or GPL?
Use this project at your own risk

## TODO fixing

- more smart looping/updating (perhaps reading data only every 10s)
- parsing each type of packet into readable format
- returning any/all data into machine readable format (JSON/csv?)
- DB connector for persistent storage of date
- basic local DB for displaying such data on localhost/network
- Unit tests?

-----------------------------

## Testing commands

use this to scan COMS `python -m serial.tools.list_ports`

`python -m serial.tools.miniterm "spy:///dev/ttyUSB0?file=/dev/pts/2&color" 115200`
sudo python -m serial.tools.miniterm "spy:///dev/ttyUSB0?file=/dev/pts/2&color" 115200
