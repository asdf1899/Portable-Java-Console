#-*- coding: UTF-8 -*-
import shutil, os

def main():
    print("Portable Java Console v1.0")
    print(" ")
    print("Modify the config file to set your JDK bin directory path")
    PATH = readConfig()

def readConfig():
    f = open("config.txt")
    for ff in f.readlines():
        file= ff.strip()
    if file != file + "/":
        file= file+ "/"
    return file

if __name__ == "__main__":
    main()
