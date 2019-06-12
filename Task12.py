def count():
    num = 0
    sentence = (input("Write a sentence: ")).split()
    for i in sentence:
        num += 1
    print(num)
count()

