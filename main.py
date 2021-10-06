#WRITE YOUR CODE IN THIS FILE
def countA(w):
    x = 1
    for i in range(0, len(w)):
        if w[i] == "a":
            return len(w[i])
        else:
            return 0
        x = x + 1
print(countA("bench"))

