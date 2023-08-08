#1) 최대공약수 - 유클리드 호제법
# x / y를 계속하면서 나머지가 0일 때의 y값이 최대 공약수
# x에는 y값을, y에는 나머지를 넣으며 계속 반복

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

#2) 최소공배수 - x*y // 최대공약수
def lcd(x, y):
    return (x * y) // gcd(x, y)

x, y = map(int, input().split())
print(gcd(x, y))
print(lcd(x, y))