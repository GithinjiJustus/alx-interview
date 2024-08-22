#!/usr/bin/python3
"""
0-validate_utf8.py
"""

def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding.

    Args:
        data (list): List of integers where each integer represents 1 byte.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes to process for the current character
    num_bytes = 0

    # Masks to check leading bits of each byte
    mask_1_byte = 0b10000000  # 1-byte character: leading bit must be 0
    mask_2_bytes = 0b11100000  # 2-byte character: leading bits must be 110
    mask_3_bytes = 0b11110000  # 3-byte character: leading bits must be 1110
    mask_4_bytes = 0b11111000  # 4-byte character: leading bits must be 11110
    mask_continuation = 0b11000000  # Continuation byte: leading bits must be 10

    for byte in data:
        # Get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            if (byte & mask_1_byte) == 0:
                continue  # 1-byte character
            elif (byte & mask_2_bytes) == 0b11000000:
                num_bytes = 1  # 2-byte character
            elif (byte & mask_3_bytes) == 0b11100000:
                num_bytes = 2  # 3-byte character
            elif (byte & mask_4_bytes) == 0b11110000:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8 character
        else:
            # Check that the byte is a valid continuation byte
            if (byte & mask_continuation) != 0b10000000:
                return False
            num_bytes -= 1

    # If we processed all bytes, num_bytes should be 0
    return num_bytes == 0
