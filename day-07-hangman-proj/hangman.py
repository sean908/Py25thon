import random
import os

def load_words():
    """从文件中加载单词列表"""
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            words = [word.strip().lower() for word in file.readlines()]
        return words
    except FileNotFoundError:
        print("单词文件 words.txt 未找到！")
        return ['python', 'computer', 'programming', 'hangman']

def get_random_word(word_list):
    """从单词列表中随机选择一个单词"""
    return random.choice(word_list)

def display_hangman(tries):
    """显示Hangman图形"""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def display_word(word, guessed_letters):
    """显示当前猜词状态"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def is_word_guessed(word, guessed_letters):
    """检查单词是否已被完全猜出"""
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def get_valid_guess(guessed_letters):
    """获取有效的用户输入"""
    while True:
        guess = input("请猜一个字母: ").lower().strip()
        
        if len(guess) != 1:
            print("请只输入一个字母！")
            continue
            
        if not guess.isalpha():
            print("请输入一个有效的字母！")
            continue
            
        if guess in guessed_letters:
            print("你已经猜过这个字母了！")
            continue
            
        return guess

def play_hangman():
    """主游戏函数"""
    words = load_words()
    word_to_guess = get_random_word(words)
    guessed_letters = set()
    tries = 6
    
    print("欢迎来到 Hangman 猜词游戏！")
    print(f"单词有 {len(word_to_guess)} 个字母")
    print(display_hangman(tries))
    print(display_word(word_to_guess, guessed_letters))
    
    while tries > 0 and not is_word_guessed(word_to_guess, guessed_letters):
        print(f"\n剩余机会: {tries}")
        print(f"已猜字母: {', '.join(sorted(guessed_letters)) if guessed_letters else '无'}")
        
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            print(f"好猜！字母 '{guess}' 在单词中。")
        else:
            tries -= 1
            print(f"很遗憾，字母 '{guess}' 不在单词中。")
        
        os.system('clear' if os.name == 'posix' else 'cls')
        print(display_hangman(tries))
        print(display_word(word_to_guess, guessed_letters))
    
    if is_word_guessed(word_to_guess, guessed_letters):
        print(f"\n🎉 恭喜你！你猜对了单词：'{word_to_guess}'")
    else:
        print(f"\n💀 游戏结束！正确答案是：'{word_to_guess}'")

def main():
    """主函数，处理游戏循环"""
    while True:
        play_hangman()
        
        play_again = input("\n想再玩一次吗？(y/n): ").lower().strip()
        if play_again != 'y' and play_again != 'yes':
            print("谢谢游玩！再见！")
            break
        
        os.system('clear' if os.name == 'posix' else 'cls')

if __name__ == "__main__":
    main()