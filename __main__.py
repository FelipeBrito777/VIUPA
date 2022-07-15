import sys
from healthy.Healthy import Game

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("Main module speaking")

    game = Game()
    game.run()

if __name__ == '__main__':
    sys.exit(main())