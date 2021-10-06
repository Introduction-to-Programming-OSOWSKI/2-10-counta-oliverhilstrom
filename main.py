#WRITE YOUR CODE IN THIS FILE
def countA(w):
    x = 0
    for i in range(0, len(w)):
        if w[i] == "a":
            x = x + 1
    return x 
print(countA("alabama"))

