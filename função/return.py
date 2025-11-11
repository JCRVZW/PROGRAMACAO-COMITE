import random
def lista ():
    for i in range(10):
        list = [random.randint(1,100)]
    return max(list)

def main():
    print(lista)
main()