base_64_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def change_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    without_padding = len(binary) % 24
    if without_padding:
        binary += '0' * (24 - without_padding)
    return binary


def change_to_binary_with_chars(text):
    binarny = ''
    for znak in text:
        if znak == '=':
            break
        indeks = base_64_chars.index(znak)
        binarny += format(indeks, '06b')
    return binarny


def encode_base64(text):
    binary_text = change_to_binary(text)

    encoded_text = ''
    for i in range(0, len(binary_text), 6):
        index = int(binary_text[i:i + 6], 2)
        encoded_text += base_64_chars[index]

    padding = len(binary_text) % 24
    if padding:
        encoded_text += '=' * (4 - padding // 6)

    return encoded_text


def decode_base_64(text):
    binary_text = change_to_binary_with_chars(text)

    decoded_text = ''
    for i in range(0, len(binary_text), 8):
        decoded_text += chr(int(binary_text[i:i + 8], 2))

    return decoded_text


# Example usage
if __name__ == '__main__':
    text_to_encode = 'To jest przykladowy tekst do zaszyfrowania'
    print(f'Text to encode:>>{text_to_encode}<<')
    result = encode_base64(text_to_encode)
    print(f'Encoded text:>>{result}<<')
    # Decoded usage
    result = decode_base_64(result)
    print(f'Decoded text:>>{result}<<')
