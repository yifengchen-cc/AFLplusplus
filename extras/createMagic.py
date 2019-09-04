#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import binascii
import csv
import optparse


def manualImport():
    magic_name = input("Input Magic Name:")
    f = open(magic_name, "wb+")
    tmp_input = input("Input Magic(eg:42 4d ('BM')):")
    magic = binascii.unhexlify(tmp_input.replace(' ', ''))
    f.write(magic)
    f.close()


def autoImport(file_name):
    csv_reader = csv.reader(open(file_name, encoding='utf-8'))
    for row in csv_reader:
        magic_name, tmp_input = row
        f = open(magic_name, "wb+")
        magic = binascii.unhexlify(tmp_input.replace(' ', ''))
        f.write(magic)
        f.close()


def main():

    parser = optparse.OptionParser()
    parser.add_option('-m',
                      '--manual',
                      action='store_true',
                      dest='manual',
                      default=False,
                      help='import file magic manually')
    parser.add_option('-a',
                      '--auto',
                      action='store',
                      type='string',
                      dest='filename',
                      metavar="FILE",
                      help='import file magic from csv file')
    (options, args) = parser.parse_args()
    if options.manual is True:
        manualImport()
    else:
        autoImport(options.filename)


if __name__ == '__main__':
    main()
