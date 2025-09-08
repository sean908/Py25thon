import random

def load_words():
    """从文件中加载单词列表"""
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            words = [word.strip().lower() for word in file.readlines()]
        return words
    except FileNotFoundError:
        print("单词文件 words.txt 未找到！")
        return ['python', 'computer', 'programming', 'hangman']

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

def demo_game():
    """演示游戏过程"""
    print("=== Hangman 游戏演示 ===\n")
    
    words = load_words()
    word = "python"  # 使用固定单词进行演示
    guessed_letters = set()
    tries = 6
    
    # 模拟游戏过程
    demo_guesses = ['p', 'x', 'y', 'z', 't', 'h', 'o', 'n']
    
    print(f"要猜的单词: {word}")
    print(f"单词长度: {len(word)} 个字母")
    print(display_hangman(tries))
    print(f"当前状态: {display_word(word, guessed_letters)}")
    print("-" * 40)
    
    for i, guess in enumerate(demo_guesses):
        print(f"\n第 {i+1} 次猜测: '{guess}'")
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"✅ 正确！字母 '{guess}' 在单词中")
        else:
            tries -= 1
            print(f"❌ 错误！字母 '{guess}' 不在单词中，剩余机会: {tries}")
        
        print(display_hangman(tries))
        print(f"当前状态: {display_word(word, guessed_letters)}")
        print(f"已猜字母: {', '.join(sorted(guessed_letters))}")
        
        # 检查是否获胜
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 恭喜！成功猜出单词: '{word}'")
            break
            
        # 检查是否失败
        if tries == 0:
            print(f"\n💀 游戏失败！正确答案是: '{word}'")
            break
        
        print("-" * 40)

if __name__ == "__main__":
    demo_game()