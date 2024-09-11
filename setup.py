from setuptools import setup, find_packages

setup(
    name="qr-cli",
    version="0.1",
    packages=find_packages(),
    install_requires=["qrcode[pil]"],

    entry_points={
        'console_scripts': [
            'qr=qr_cli.cli:main',
        ],
    },

    # Metadata
    author="Pulkit Sharma",
    author_email="pulkitsh1@outlook.com",
    description="A simple CLI tool to generate QR codes",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/pulkitsh1/QR-CLI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
