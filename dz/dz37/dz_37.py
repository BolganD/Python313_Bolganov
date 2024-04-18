from parse import Parser


def main():
    url = "https://rutor-gamer.info/games/page/{}/"
    pars = Parser(url, "dz_37.txt")
    pars.run()


if __name__ == '__main__':
    main()