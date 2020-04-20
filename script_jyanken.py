print("----------------------------")
print('Hello, world!')
print("This is Python lesson")
print('Lets play Rock-Paper-Scissors Game!')
print("----------------------------")

import random
computer_hand = random.randint(0,2)

def welcome(player_name):
    print(player_name +'さんようこそ！')

def judge(player, computer):
    if player == computer:
        return '引き分けです！もう一度！'
    elif player == 0 and computer == 1:
        return '勝ちました！おめでとう！'
    elif player == 1 and computer == 2:
        return '勝ちました！おめでとう！'
    elif player == 2 and computer == 0:
        return '勝ちました！おめでとう！'
    else:
        return '負けました。残念！'

def print_hand(hand, name):
    hands = ['グー','チョキ','パー']
    print(name + 'さんは' + hands[hand] + 'を出しました')

player_name = input('名前を入力してください：')
welcome(player_name)

print('それではじゃんけんを始めます')
print('どれを出しますか？ (0:グー、1:チョキ、2:パー)')
player_hand = int(input('数字を入力してください:'))
print_hand(player_hand, player_name)
print_hand(computer_hand, '相手')

result = judge(player_hand,computer_hand)
print('その結果、あなたは' + result)

def choise(Yes_No):
    choise = ['Yes','No']
print('もう一度しませんか？ 0:Yes 1:No')
choise = int(input('数字を入力してください:'))
if choise == 0:
        print("----------------------------")
        print('それではじゃんけんを始めます')
        print('どれを出しますか？ (0:グー、1:チョキ、2:パー)')
        player_hand = int(input('数字を入力してください:'))
        print_hand(player_hand, player_name)
        print_hand(computer_hand, '相手')

        result = judge(player_hand,computer_hand)
        print('その結果、あなたは' + result)
elif choise == 1:
        print('わかりました！バイバイ！')

