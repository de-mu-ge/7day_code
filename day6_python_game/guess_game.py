import random

print('欢迎来到猜数字小游戏')
print('我已经想好了一个1-100之间的数字')

while True:
    ans = random.randint(1, 100)
    count = 0
    while True:
        try:
            guess = int(input('请输入你猜的数字：'))
        except ValueError:
            print('请输入一个整数')
            continue
        count += 1
        if guess > ans:
            print('猜大了')
        elif guess < ans:
            print('猜小了')
        else:
            print('恭喜你猜对了，一共猜了', count, '次')
            break
    again = input('还要再玩一次吗？(y/n)：')
    if again != 'y':
        print('游戏结束，下次再见')
        break
