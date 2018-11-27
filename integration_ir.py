# CP320 - Final Project
# Author: Alex Kirsopp and Pillip Lee
# Version 5

import spidev
import time

SPI_PORT = 0
SPI_DEVICE_ADC = 1
START_BIT = 1
ADC_CHANNEL = 0
REF_VOLTAGE = 3.3
COMMAND_OFFSET = 4
SET_SIGNAL_MODE = 8
OUTPUT_CODE_CONST = 1024
DEVICE_SPEED_HZ = 5000

spi = spidev.SpiDev()
spi.open(SPI_PORT, SPI_DEVICE_ADC)
spi.max_speed_hz = DEVICE_SPEED_HZ

def infrared_On():
	# Get value from ADC converter, and parse the response
	# to the appropriate voltage reading.
  adc_res = read_adc()
  ir_val = parse_ir(adc_res)
  return ir_val

def read_adc():
  # Full transaction with MCP3008
  # Signal Mode ensures first byte of SGL-DIFF/D2/D1/D0 is 1; the next
  # 3 bits for 0 to 7 specify channel number. Offset by 4 bits to finish
  # the second of 3 bytes. Last, transfer a set of 8 0-bits as do-not-care.
  res = spi.xfer2([START_BIT, (SET_SIGNAL_MODE + ADC_CHANNEL) << COMMAND_OFFSET, 0])
  return res

def parse_ir(adc_res):
  data = ((adc_res[1] & 3) << 8) + adc_res[2]
  # Output code = (1024 * VoltageIn) / VoltageReg. We want VoltageIn
  data_scale = (data * REF_VOLTAGE) / float(OUTPUT_CODE_CONST)
  data_scale = round(data_scale, 2)
  return data_scale
