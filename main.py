# main.py

from qr_generator import generate_qr_code

def main():
    data = input("Enter text or link to encode in QR code: ")
    filename = input("Enter filename to save (e.g., 'my_qr.png'): ") or "qr_code.png"
    
    path = generate_qr_code(data, filename)
    print(f"✅ QR Code saved at: {path}")

if __name__ == "__main__":
    main()
