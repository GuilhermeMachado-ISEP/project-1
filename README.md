# CypherCLI

An image-based encryption tool that uses pixel data from a source image to transform text via a CLI interface.

## How it works

1. A source image (`baseimg.jpg`) is resized and randomly cropped based on the input length. It's ideal this image is on a 1:1 scale in order to assure better encryption results
2. Each character's ASCII value is modified by RGB pixel values from the cropped region using alternating add/subtract operations
3. Values are clamped to the printable ASCII range (0–127) using modulo 128
4. Random crop coordinates are appended to the ciphertext for decryption

## Requirements

- Python 3
- `Pillow`
- `numpy`

Install dependencies:

```bash
pip install Pillow numpy
```

## Usage

```bash
python main.py
```

Enter a string when prompted. The program prints both the encrypted output and the decrypted result (verifying correctness).

## Files

| File | Description |
|------|-------------|
| `main.py` | CLI entry point |
| `encrypt.py` | Encryption logic |
| `decrypt.py` | Decryption logic |
| `image_to_code.py` | Image pixel extraction utilities |
| `imaghnaghtest.jpg` | Source image used as key material |
