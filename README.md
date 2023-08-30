# nsall

A Python script to resolve and print unique hostnames from a CIDR block.

## Installation

To use `nsall`, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Bunyatov/nsall.git
   cd nsall
   chmod +x nsall.py
   sudo mv nsall.py /usr/bin/nsall
   ```

## Usage
Once installed, you can use nsall to resolve and print hostnames from a CIDR block. For example:

```bash
nsall -v 172.16.0.0/12
```
nsall --help
usage: nsall [-h] [-v] cidr

Resolve and print unique hostnames from a CIDR block

positional arguments:
  cidr           CIDR block to scan for hostnames

options:
  -h, --help     show this help message and exit
  -v, --verbose  Print IP address along with hostname
