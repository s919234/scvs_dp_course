
f= open('in/in101.txt')
a=eval(f.readline())
b=eval(f.readline())
c=eval(f.readline())
d=eval(f.readline())
f.close()

print('|{:5d} {:5d}|'.format(a,b))  
print('|{:5d} {:5d}|'.format(c,d)) 
print('|{:<5d} {:<5d}|'.format(a,b))
print('|{:<5d} {:<5d}|'.format(c,d))
input('按任意鍵結束')