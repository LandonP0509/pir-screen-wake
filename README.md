# pir-screen-wake
Script for a wake and dim feature via a PIR sensor with a Raspberry Pi.

# Kitchen Display

A Raspberry Pi 4B based kitchen shopping list display running AnyList 
in kiosk mode, with a PIR sensor for automatic screen sleep/wake.

## Hardware

- Raspberry Pi 4B
- iPistBit 10.1" Touchscreen Monitor (1024x600)
- HC-SR501 PIR Motion Sensor
- Female-to-female jumper wires

## PIR Wiring

| HC-SR501 | Raspberry Pi 4B |
|----------|----------------|
| VCC      | Pin 2 (5V)     |
| GND      | Pin 6 (Ground) |
| OUT      | Pin 11 (GPIO 17)|

## Dependencies

```bash
pip3 install RPi.GPIO --break-system-packages
```

## Usage

```bash
python3 pir_wake.py
```

Runs automatically on boot via autostart. Screen sleeps after 30 minutes 
of no motion and wakes instantly when the PIR detects movement.

## Configuration

In `pir_wake.py` adjust these variables at the top of the file:
- `PIR_PIN` — GPIO pin number the PIR signal wire is connected to
- `SLEEP_MINUTES` — minutes of inactivity before screen sleeps

## Setup

See the autostart config in `/home/youruser/.config/autostart/` for the 
kiosk and PIR boot configuration.
