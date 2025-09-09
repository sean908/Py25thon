def caesar_encode(text, shift):
    result = ""
    shift = shift % 26  # Normalize shift to 0-25 range
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def caesar_decode(text, shift):
    return caesar_encode(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    
    while True:
        choice = input("请选择操作 (encode/decode): ").lower().strip()
        if choice in ['encode', 'decode']:
            break
        print("请输入有效的选择: encode 或 decode")
    
    text = input("请输入要处理的文本: ")
    
    while True:
        try:
            shift = int(input("请输入偏移量 (数字): "))
            if shift == 0:
                print("偏移量为0将不会改变文本，请输入非零数字")
                continue
            break
        except ValueError:
            print("请输入一个有效的数字")
    
    if choice == 'encode':
        result = caesar_encode(text, shift)
        print(f"编码结果: {result}")
    else:
        result = caesar_decode(text, shift)
        print(f"解码结果: {result}")

if __name__ == "__main__":
    main()