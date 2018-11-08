import spidev

spi = spidev.SpiDev()
spi.open(0,0)

while True:
	val = raw_input("value 0..255, q=quit:")

	if val == 'q':
		break
	else:
		value = int(val)
		dummy = spi.xfer2([21, value])

spi.close()

