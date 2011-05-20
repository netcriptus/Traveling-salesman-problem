#!/usr/bin/python

def main(argv):
    number_of_cities = stdin.readline()
    salesman = Salesman(int(number_of_cities))
    salesman.getCities()
    salesman.mountMap()

    tour, distance = salesman.travel()
    stdout.write("%.2f\n" % distance)
    for city in tour:
        stdout.write("%d " % city)

    stdout.write("\n")
    return 0

if __name__ == "__main__":
    from sys import exit, argv, stdin, stdout, stderr, path
    path.append("src/lib")
    from salesman import Salesman
    exit(main(argv))
