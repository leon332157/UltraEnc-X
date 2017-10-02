#!/usr/bin/python

from random import randint

def generate_otp(sheets, length):
        for sheet in range(sheets):
                with open("027." + str(sheet+1) + ".uep","w") as f:
                        for i in range(length):
                                f.write(str(randint(0,26))+"\n")

def load_sheet(filename):
        with open(filename, "r") as f:
                contents = f.read().splitlines()
        return contents

def get_plaintext():
        plaintext = input('请输入你要加密的文字信息： ')
        return plaintext.lower()

def load_file(filename):
        with open(filename, "r") as f:
                contents = f.read()
        return contents

def save_file(filename, data):
        with open(filename + ".ued", 'w') as f:
                f.write(data)