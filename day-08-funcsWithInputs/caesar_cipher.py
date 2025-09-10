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

def display_logo():
    logo = """
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║     ███████║█████╗  ███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                           Written by Se@n
"""
    print(logo)

def get_user_choice():
    while True:
        choice = input("请选择操作 (encode/decode): ").lower().strip()
        if choice in ['e', 'en', 'encode']:
            return 'encode'
        elif choice in ['d', 'de', 'decode']:
            return 'decode'
        print("请输入有效的选择: encode/e/en 或 decode/d/de")

def get_continue_choice():
    while True:
        choice = input("是否继续? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        print("请输入 y/yes 或 n/no")

def main():
    display_logo()
    
    while True:
        print("=" * 50)
        choice = get_user_choice()
        
        if choice == 'encode':
            text = input("请输入要加密的文本: ")
        else:
            text = input("请输入要解密的文本: ")
        
        while True:
            try:
                shift = int(input("请输入偏移量 (数字): "))
                if shift == 0:
                    print("偏移量为0将不会改变文本，请输入非零数字")
                    continue
                break
            except ValueError:
                print("请输入一个有效的数字")
        
        print("-" * 30)
        if choice == 'encode':
            result = caesar_encode(text, shift)
            print(f"加密结果: {result}")
        else:
            result = caesar_decode(text, shift)
            print(f"解密结果: {result}")
        print("-" * 30)
        
        if not get_continue_choice():
            print("\n感谢使用 Caesar Cipher 工具!")
            break
        print("\n")

if __name__ == "__main__":
    main()