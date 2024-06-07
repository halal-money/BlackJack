from interface import Screen


class Main:
    def __init__(self):
        self.screen = Screen()

    def run(self):
        self.screen.run()


if __name__ == '__main__':
    main = Main()
    main.run()