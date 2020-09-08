#從螢幕輸入語法：  變數 = input([提示字串])

name = input("你的名字是")
print("你好",name)

# 從當案輸入 ，並轉成數值

# 格式1：一直讀到檔案結束，with 會自動關閉
with open('in/in101.txt') as f:
    for line in f:
        print(eval(line))


# 格式2：一行一行讀，再關閉
f= open('in/in101.txt')
a=eval(f.readline())
b=eval(f.readline())
c=eval(f.readline())
d=eval(f.readline())
f.close()        