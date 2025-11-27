import time
import sys

def mostrar_hora():
    while True:
        agora = time.strftime("%H:%M:%S")
        sys.stdout.write(f"\r {agora}")
        sys.stdout.flush()
        time.sleep(1)

def main():
    try:
        mostrar_hora()
    except KeyboardInterrupt:
        print("\n PROGRAMA ENCERRADO!")
main()