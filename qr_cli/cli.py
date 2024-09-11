#!/usr/bin/env python3

import qrcode, argparse

def generate_qr(data, file_name):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill = "black", back_color = "white")

    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")

def main():
    parser = argparse.ArgumentParser(description="Generate QR codes via CLI.")
    parser.add_argument("-u","--url",help="The data/content you want to encode into the QR code.")
    parser.add_argument("-o","--output",default="qrcode.png",help="Output file name (with .png extension).")

    args = parser.parse_args()

    generate_qr(args.url, args.output)

if __name__ == "__main__":
    main() 