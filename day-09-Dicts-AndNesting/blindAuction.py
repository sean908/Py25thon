import os
import json
from datetime import datetime

def print_auction_hammer(session_id):
    """打印拍卖槌的ASCII图案和期号"""
    print(f"\n{'='*50}")
    print(f"           {session_id} 拍卖")
    print(f"{'='*50}")
    hammer_art = '''
                         ___________
                         \\         /
                          )_______(
                          |''' + '"""""""' + '''|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )''' + '"""""""' + '''(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
                           
                     欢迎来到盲拍竞价系统！
    '''
    print(hammer_art)

def clear_screen():
    """清空屏幕"""
    os.system('cls' if os.name == 'nt' else 'clear')

def save_bid_to_file(name, bid, session_id):
    """将竞价信息保存到文件"""
    bid_data = {"name": name, "bid": bid, "session_id": session_id, "timestamp": datetime.now().isoformat()}
    
    # 检查文件是否存在，如果存在则读取现有数据
    try:
        with open("auction_data.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    
    # 添加新的竞价数据
    existing_data.append(bid_data)
    
    # 保存到文件
    with open("auction_data.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=2)

def get_winner():
    """从文件中读取所有竞价数据并确定获胜者"""
    try:
        with open("auction_data.json", "r", encoding="utf-8") as file:
            bid_data = json.load(file)
        
        if not bid_data:
            return None, 0, []
        
        # 找到最高出价者
        winner = max(bid_data, key=lambda x: x["bid"])
        return winner["name"], winner["bid"], bid_data
    
    except (FileNotFoundError, json.JSONDecodeError):
        return None, 0, []

def generate_session_id():
    """生成拍卖期号：yyyymmdd+序列号"""
    today = datetime.now().strftime("%Y%m%d")
    
    # 检查今天已有的期号
    try:
        with open("ba_log.txt", "r", encoding="utf-8") as file:
            content = file.read()
        
        # 查找今天的期号
        today_sessions = content.count(f"{today}")
        sequence = today_sessions + 1
    except FileNotFoundError:
        sequence = 1
    
    return f"{today}{sequence:02d}"

def save_to_log(session_id, winner_name, winning_bid, all_bids):
    """保存拍卖记录到ba_log.txt文件"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 准备日志内容
    log_content = f"{now} - {session_id}期次拍卖开始\n"
    log_content += "竞价情况：\n"
    
    for bid in all_bids:
        log_content += f"{bid['name']} - {bid['bid']}\n"
    
    log_content += "最终结果:\n"
    log_content += f"{winner_name} 以 {winning_bid} 赢得了 {len(all_bids)}人 的竞拍\n\n"
    
    # 追加到文件
    with open("ba_log.txt", "a", encoding="utf-8") as file:
        file.write(log_content)

def is_continue_auction(user_input):
    """判断用户是否想继续拍卖"""
    positive_responses = ['y', 'yes', 'Y', 'YES', 'Yes']
    return user_input.strip() in positive_responses

def main():
    """主程序"""
    # 生成本次拍卖期号
    session_id = generate_session_id()
    
    # 清空auction_data.json文件
    if os.path.exists("auction_data.json"):
        os.remove("auction_data.json")
    
    # 显示拍卖槌和期号
    print_auction_hammer(session_id)
    
    while True:
        # 获取用户姓名
        name = input("请输入您的姓名: ").strip()
        while not name:
            name = input("姓名不能为空，请重新输入: ").strip()
        
        # 获取竞价金额
        while True:
            try:
                bid = float(input("请输入您的竞价金额: "))
                if bid <= 0:
                    print("竞价金额必须大于0，请重新输入。")
                    continue
                break
            except ValueError:
                print("请输入有效的数字。")
        
        # 保存竞价信息到文件
        save_bid_to_file(name, bid, session_id)
        print(f"竞价信息已保存：{name} - ¥{bid}")
        
        # 询问是否还有下一位竞价者
        continue_input = input("是否还有下一位参与竞价者？(y/n): ")
        
        # 清空屏幕
        clear_screen()
        
        # 判断是否继续
        if not is_continue_auction(continue_input):
            break
        
        # 重新显示期号信息
        print(f"\n{'='*50}")
        print(f"           {session_id} 拍卖")
        print(f"{'='*50}\n")
    
    # 确定并公布获胜者
    winner_name, winning_bid, all_bids = get_winner()
    
    if winner_name:
        print("🎉 拍卖结束！")
        print(f"🏆 恭喜 {winner_name} 以 ¥{winning_bid} 的价格赢得了此次拍卖！")
        
        # 保存到日志文件
        save_to_log(session_id, winner_name, winning_bid, all_bids)
        print(f"📝 拍卖记录已保存到ba_log.txt (期号: {session_id})")
    else:
        print("没有有效的竞价记录。")

if __name__ == "__main__":
    main()