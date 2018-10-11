#!/usr/bin/python

import os, sys

def main():
    fname = sys.argv[1]
    no_res = []
    bad_assert = []

    with open(fname, 'r') as f:
        l = f.readline()
        while l:
            if l[0] == 'F':
                id = l.split(' -- ')[1].rstrip()[:-1]
                n = f.readline()
                if 'No response from server' in n:
                    no_res.append(id)
                else:
                    bad_assert.append(id)
            l = f.readline()    

    print("No response from server: {}".format(no_res))
    print("Assert failure: {}".format(bad_assert))
    if bad_assert:
        print("Test failed")
        exit(1)

if __name__ == "__main__":
    main()



