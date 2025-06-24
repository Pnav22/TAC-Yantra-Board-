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

_Replace the placeholders below with your PCB images._

![PCB Front](images/pcb_front_placeholder.png)  
![PCB Back](images/pcb_back_placeholder.png)  
![PCB Wiring](images/pcb_wiring_placeholder.png)

---

## 🧾 Features

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

## 🔌 Wiring Summary

- **Key Matrix**: 3 rows × 3 columns using 1N4148 diodes (COL2ROW)
- **Encoder**:
  - A → GP0  
  - B → GP1  
  - Button → GP7 (or matrix)
- **Matrix Pins**:
  - Rows: GP27 (A1), GP28 (A2), GP26 (A0)  
  - Cols: GP4 (MISO), GP5 (SCK), GP6 (SDA)

---

## 💻 Firmware

This project uses [KMK Firmware](https://github.com/KMKfw/kmk_firmware), a keyboard firmware built on CircuitPython. Code can be modified directly on the board via USB like a flash drive.

📂 `code.py` handles:
- Matrix setup
- Encoder input
- Volume + media key support

---

## 🚀 Getting Started

1. Flash CircuitPython onto your XIAO RP2040  
2. Copy `code.py` and the `lib/` folder from KMK into the CIRCUITPY volume  
3. Plug it in and test!

---

## 🧠 Customization Ideas

- Add layers using KMK’s `Layers` module  
- Program macros (e.g., copy/paste or OBS shortcuts)  
- Add an OLED display to show current layer or media state  
- Swap encoder behavior for scrolling or app switching

---

## 🔱 TAC YANTRA

**TAC YANTRA** is the name of this device:

- **TAC** – a nod to tactical utility and control  
- **YANTRA** – a Sanskrit term meaning *"instrument" or "machine"*, often used to describe spiritual diagrams or sacred mechanisms that focus energy or intent  

Together, **TAC YANTRA** represents a **tactical interface device** designed with both **mechanical precision** and **intentional design** — bridging modern tech with ancient meaning.

---

## 📄 License

MIT License.  
Feel free to remix and share!

---

_Designed by [Your Name]_
