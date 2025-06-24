# TAC YANTRA - 3x3 Macro Keypad with Rotary Encoder

This is a custom 9-key macro pad with a rotary encoder, powered by the XIAO RP2040 and running KMK firmware. It supports media control, number input, and layer extensibility — all programmable in CircuitPython using KMK.

---

## Overview

Here's a picture of my work! This is a submission for HackPad!

Shaded            |  WireFrame
:-------------------------:|:-------------------------:
![Bottom Base - TAC v5 shaded](https://github.com/user-attachments/assets/b33aa44e-7c4c-46c1-b122-d0d98e246d67)  |  ![Bottom Base - TAC v5](https://github.com/user-attachments/assets/521b8432-4ac8-4405-b809-29eab201513f)


---



##  PCB
PCB            |  Schematic
:-------------------------:|:-------------------------:
![PCB Front](https://github.com/user-attachments/assets/fe14e158-7bf4-4130-a9e4-d2c2ffe600b3)  |  ![PCB Back](https://github.com/user-attachments/assets/0920f8ec-823d-4420-902b-3d1fbaa8548c)


---
## How It Fits Together

![v2](https://github.com/user-attachments/assets/cf59dbf2-dfe0-481d-8c75-dcc189d6321b)


It uses HeatSet Inserts at the bottom that are secured by M3 x 16mm screws from the top.
 
---


##  Features

- 9 programmable keys (currently set to numbers `1–9`)
- EC11 rotary encoder for volume control
- Push-to-toggle Play/Pause
- KMK firmware written in Python for rapid iteration
- USB HID support (works on macOS, Windows, Linux)
  
---

## ⚙️ Bill of Materials (BOM)

| Quantity | Item                           |
|----------|--------------------------------|
| 9        | Cherry MX Switches             |
| 9        | DSA Keycaps                    |
| 4        | M3x5x4 Heatset Inserts         |
| 4        | M3x16mm Socket Head Cap Screws |
| 9        | 1N4148 DO-35 Diodes            |
| 1        | EC11 Rotary Encoder            |
| 1        | Seeed XIAO RP2040              |
| 1        | Case (2 printed parts)         |


---

##  Firmware

This project uses [KMK Firmware](https://github.com/KMKfw/kmk_firmware), a keyboard firmware built on CircuitPython. Code can be modified directly on the board via USB like a flash drive.

`code.py` handles:
- Matrix setup
- Encoder input
- Volume + media key support


---

##  TAC YANTRA

**TAC YANTRA** is the name of this device:

- **TAC** – a nod to tactical utility and control  
- **YANTRA** – a Sanskrit term meaning *"instrument" or "machine"*, often used to describe spiritual diagrams or sacred mechanisms that focus energy or intent  

Together, **TAC YANTRA** represents a **tactical interface device** designed with both **mechanical precision**. Very funny name ik ik lol. 

---
