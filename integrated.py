import RPi.GPIO as GPIO
import spidev
import time

# MCP3008 Constants for IR reader and setup
# ADC_CHANNEL = 1
SPI_PORT = 0
SPI_DEVICE_ADC = 1
START_BIT = 1
ADC_CHANNEL = 0
REF_VOLTAGE = 3.4
COMMAND_OFFSET = 4
SET_SIGNAL_MODE = 8
OUTPUT_CODE_CONST = 1024
DEVICE_SPEED_HZ = 5000

spi = spidev.SpiDev()
spi.open(SPI_PORT, SPI_DEVICE_ADC)
spi.max_speed_hz = DEVICE_SPEED_HZ


# Stepper motor constants and setup
GPIO.setmode(GPIO.BCM)

STEP_PINS = [13,16,26,21]
CURRENT_ANGLE = 0
STEP_MULT = 5.833
STEPPER_SEQ = []
STEPPER_SEQ.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.LOW])
STEPPER_SEQ.append([GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
STEPPER_SEQ.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.LOW])
STEPPER_SEQ.append([GPIO.LOW, GPIO.LOW, GPIO.LOW,GPIO.HIGH])
# 360_STEPS = 2100

def read_adc():
  # Full transaction with MCP3008
  # Signal Mode ensures first byte of SGL-DIFF/D2/D1/D0 is 1; the next
  # 3 bits for 0 to 7 specify channel number. Offset by 4 bits to finish
  # the second of 3 bytes. Last, transfer a set of 8 0-bits as do-not-care.
  res = spi.xfer2([START_BIT, (SET_SIGNAL_MODE + ADC_CHANNEL) << COMMAND_OFFSET, 0])

def parse_ir(adc_res):1
  data = ((adc_res[1] & 3) << 8) + adc_res[2]
  # Output code = (1024 * VoltageIn) / VoltageReg. We want VoltageIn
  data_scale = (data * REF_VOLTAGE) / float(OUTPUT_CODE_CONST)
  data_scale = round(data_scale, 2)
  return data_scale

def rotate_stepper(deg):
    # Keep track of our current angle. Since the call to rotate will
    # block, we don't have to worry about this being hit multiple
    # times before the rotation is finished.
    CURRENT_ANGLE += int(deg)

    if CURRENT_ANGLE >= 360:
      CURRENT_ANGLE -= 360

    steps = (int(deg) * STEP_MULT) / 4
    print("input %d degrees, stepsations: %d", deg, steps)

    while steps > 0:
      for row in STEPPER_SEQ:
        GPIO.output(STEP_PINS,row)
        time.sleep(0.02)
      steps -= 1


try:
  while True:
    # Get IR reading
    adc_res = read_adc()
    ir_val = parse_ir(adc_res)
    print("ir_val: ", ir_val)

    # Output current reading to LED display

    # If something is detected in front, rotate motor 90deg
    # Assume detection happens at 2.0 volt threshold

    if ir_val >= 2.0
      rotate_stepper(90)

    # Display current motor position on LED strip
    # Display # of revolutions on second LED display

    # Listen for button input and do... something

    time.sleep(0.5)
except KeyboardInterrupt:
  pass

spi.close()
GPIO.cleanup()

