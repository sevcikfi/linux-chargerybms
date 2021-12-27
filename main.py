

from struct import pack
import serial

#device name
DEVICE = "/dev/ttyUSB0"
#BAUDRATE
BAUDRATE = 115200
# define special unicode characters here
SPECIAL_DISPLAY_SYMBOLS = {
	'degree' : u'\u00b0',
	'ohm'    : u'\u03A9'
}


# example network packets form the chargery community protocol manual v1.25
BMS_TEST_PACKETS = {
	1 : bytearray.fromhex('2424570F0E240100E6008100845B27'),
	2 : bytearray.fromhex('2424570F0E240100E4008100845B25'),
	3 : bytearray.fromhex('2424570F0E240100E1008300845B24'),
	4 : bytearray.fromhex('2424562D0CFD0D040D040D020D030D040D060D010D080D020D050CFE0D060CFB0D0F0CFC76FED50263140E0095'),
	5 : bytearray.fromhex('2424582801E4000100030003000300020003000000000001000100010000000500020003000300CC'),
	6 : bytearray.fromhex('2424570F0E240100E4008300845B27'),
	7 : bytearray.fromhex('24245814012a000900040007000b000b00070010'),
	8 : bytearray.fromhex('2424570F0E240100E4008300845B27683A3A330D0A')
}
#Packet headers
PACKET_HEADER             = 0x24
PACKET_STATUS_CELLS       = 0x56
PACKET_STATUS_BMS         = 0x57
PACKET_STATUS_IMPEDANCES  = 0x58

PACKET_LENGTH_MINIMUM            = 10
PACKET_LENGTH_STATUS_CELLS       = [29, 45, 61]
PACKET_LENGTH_STATUS_BMS         = [19]

# Special handling here: the impedances packet length is dynamically
# and depends on how many cells are monitored. The minimum length of
# the network packet with headers, command, length, currentmode1, current1
# and checksum is 8 bytes. On 6 monitored cells the packet length will
# be 8+(2*6) = 20 bytes. Therefore, the smallest possible and valid
# impedances network packet will be 10 bytes
PACKET_LENGTH_STATUS_IMPEDANCES  = 10

MIN_CELL_VOLTAGE   = 1.0
MIN_CELL_IMPEDANCE = 0.0

# Again special handling: Negative temperatures will result in
# a buffer overflow we do handle this if temperature values
# are retruned above 65000 which is about - 53,6 degree celsius
MINUS_TEMPERATURE_OFFSET = 65000



data = BMS_TEST_PACKETS[1]
print(data)
print(list(data))






def init():
    with serial.Serial(DEVICE, BAUDRATE) as serial_port:
        then:bytes = b''
        now:bytes = b''
        packet = []
        while True:
            now = serial_port.read()
            print(ord(now), now)

            if((ord(now) == PACKET_HEADER) and (ord(then) == PACKET_HEADER)):
                command = serial_port.read()
                dataLen = (serial_port.read())
                print("Data length: {}, {} Command: {}, {}".\
                    format(ord(dataLen), dataLen, command, ord(command)))
                #data = command + dataLen + serial_port.read_until("2424")

                packet = [PACKET_HEADER]*2 + [ord(command)] + [ord(dataLen)] + list(serial_port.read(ord(dataLen) - 2))
                print(list(packet), len(packet))

            then = now

#__name__ == __main__ ----------------------------------------------------
if __name__ == '__main__':
    init()