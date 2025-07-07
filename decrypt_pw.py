#!/usr/bin/env python3
import base64

# Must match the XOR key used in the app’s encryptPassword()
KEY = ord('K')

def decrypt(enc_str: str) -> str:
    """Decrypts a Base64-encoded, XOR-obfuscated string and restores original order."""
    raw       = base64.b64decode(enc_str)
    # XOR each byte, build the decrypted string
    decrypted = ''.join(chr(b ^ KEY) for b in raw)
    # reverse it to correct the order
    return decrypted[::-1]

if __name__ == "__main__":
    try:
        enc = input("Enter encrypted password (paste here): ").strip()
        if not enc:
            print("No input provided. Exiting.")
        else:
            dec = decrypt(enc)
            print("\nDecrypted password:")
            print(dec)  # copy-friendly output
    except Exception as e:
        print(f"Error during decryption: {e}")
    finally:
        input("\nPress Enter to exit.")
