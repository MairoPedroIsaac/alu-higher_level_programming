#!/usr/bin/python3
import sys
if __name__ == "__main__":

    sys.argv[1:] = list(map(int, sys.argv[1:]))
    print(sum(sys.argv[1:]))
