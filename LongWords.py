t = int(input())

for i in range(t):
    word = input().strip()


    if len(word) > 10:
        print(f"{word[0]}{len(word)-2}{word[-1]}")
    else:
        print(f"{word}")
