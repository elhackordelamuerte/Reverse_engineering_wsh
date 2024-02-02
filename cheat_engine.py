#!/bin/env python3
import sys

if __name__ == "__main__":
    with open(sys.argv[1], "rb+") as f:
        sav = bytearray(f.read())
        if sav[0x2590]:
            sav[0x2598] = 0x83
            sav[0x2599] = 0x80
            sav[0x259A] = 0x91
            sav[0x259B] = 0x8A
            sav[0x259C] = 0x82
            sav[0x259D] = 0x80
            sav[0x259E] = 0x93
        checksum = 0xff
        for i in sav[0x2598:0x3523]:
            checksum -= i
        sav[0x3523] = checksum & 0xff
        f.seek(0, 0)
        f.write(sav)