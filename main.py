# A
a = list(map(int, input().split()))
print(*a[::2])


# B
a = list(map(int, input().split()))
print(*[x for x in a if x % 2 == 0])


# C
a = list(map(int, input().split()))
print(sum(1 for x in a if x > 0))


# D
a = list(map(int, input().split()))
print(*[a[i] for i in range(1, len(a)) if a[i] > a[i - 1]])


# E
a = list(map(int, input().split()))
for i in range(len(a) - 1):
    if a[i] * a[i + 1] > 0:
        print(a[i], a[i + 1])
        break


# F
a = list(map(int, input().split()))
count = 0
for i in range(1, len(a) - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        count += 1
print(count)


# G
a = list(map(int, input().split()))
m = max(a)
print(m, a.index(m))


# H
a = list(map(int, input().split()))
print(min(x for x in a if x > 0))


# I
a = list(map(int, input().split()))
odd = [x for x in a if x % 2 != 0]
print(min(odd) if odd else 0)


# J
a = list(map(int, input().split()))
x = int(input())
print(sum(1 for h in a if h >= x) + 1)


# K
a = list(map(int, input().split()))
print(len(set(a)))


# L
a = list(map(int, input().split()))
print(*a[::-1])


# M
a = list(map(int, input().split()))
n = len(a)
for i in range(n // 2):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]
print(*a)


# N
a = list(map(int, input().split()))
for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(*a)


# O
a = list(map(int, input().split()))
last = a[-1]
for i in range(len(a) - 1, 0, -1):
    a[i] = a[i - 1]
a[0] = last
print(*a)

