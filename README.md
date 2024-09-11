# QR-CLI

A simple Python-based command-line interface (CLI) tool for generating QR codes from text or URLs. The QR code is saved as an image file, allowing easy sharing of data encoded in a QR format.

## Features

- Generate QR codes from any text or URL.
- Save the generated QR code as a PNG image.
- Simple and easy to use via the command line.

## Requirements

- Python 3.6 or higher
- `qrcode` library (automatically installed during setup)

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/pulkitsh1/QR-CLI.git
cd QR-CLI
```

### Installing required Libraries
Use pip to install the package globally or locally. Run the following command from the root of the project (where setup.py is located):

```bash
pip install .
```

### Usage
Once the tool is installed, you can generate QR codes directly from the command line. Use the following syntax:

```bash
qr -u "< data >" -o <output_file>
```

< data > : You can replace '< data >' with an actual url which you want to embed in the QR Code.

<output_file> : You can replace '<output_file>' with the name you want for the QR Code Image.
