def creation():
    for i in range (5):
        with open (f"Arquivo.txt{i+1}", "w") as arquivo:    
            arquivo.write("TRUFA!")


def main():
    creation()
main()