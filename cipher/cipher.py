# cipher.py

def XOR_cipher(file_unencrypted, file_key, file_encrypted='encrypted.txt'):
    with open(file_encrypted, 'w+') as output_file, open(file_unencrypted, 'rt') as input_file, open(file_key, 'rt') as key_file:
        unencrypted_character = input_file.read(1)

        # Do until we run out of text.
        while unencrypted_character:
            # Get key character.
            key_character = key_file.read(1)
            if not key_character:
                key_file.seek(0, 0)
                key_character = key_file.read(1)

            # Get encrypted number.
            encrypted_character = chr(
                ord(unencrypted_character) ^ ord(key_character)
            )

            output_file.write(encrypted_character)
            unencrypted_character = input_file.read(1)

def XOR_uncipher(file_encrypted, file_key, file_unencrypted='unencrypted.txt'):
    XOR_cipher(file_encrypted, file_key, file_encrypted=file_unencrypted)

XOR_cipher('unencrypted.txt', 'key.txt')
XOR_uncipher('encrypted.txt', 'key.txt', file_unencrypted='unencrypted_after_encryption.txt')
