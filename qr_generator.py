# qr_generator.py

import qrcode
import os

def generate_qr_code(data, filename="qr_code.png", folder="assets"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    qr = qrcode.make(data)
    file_path = os.path.join(folder, filename)
    qr.save(file_path)
    return file_path
