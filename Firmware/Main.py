import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# === Encoder support ===
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# === Optional: Layer support (not used yet) ===
layers = Layers()
keyboard.modules.append(layers)

# === Define matrix ===
keyboard.matrix = MatrixScanner(
    cols=(board.MISO, board.SCK, board.SDA),  # Cols: GPIO4, GPIO5, GPIO6
    rows=(board.A1, board.A2, board.A0),      # Rows: GPIO27, GPIO28, GPIO26
    diode_orientation=DiodeOrientation.COL2ROW
)

# === Rotary Encoder Pins ===
encoder_handler.pins = ((board.GP0, board.GP1),)  # CLK, DT
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),  # Rotate left/right
]

# === Define keymap ===
keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,   # Row 0
        KC.N4, KC.N5, KC.N6,   # Row 1
        KC.N7, KC.N8, KC.N9,   # Row 2
        KC.MPLY               # Encoder button (GPIO7, assumed last in scan list)
    ]
]

# === Run KMK ===
if __name__ == '__main__':
    keyboard.go()
