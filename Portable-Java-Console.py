#-*- coding: UTF-8 -*-
import shutil, os

def main():
    print("Portable Java Console v1.0")
    print(" ")
    print("Modify the config file to set your JDK bin directory path")
    PATH = readConfig()
    print("Current path: " + PATH)
    print(" ")
    while True:
        print("1) Run a java file")
        print("2) Help")
        print("3) Exit")
        shell = input(">> ")
        if shell == "1":
            try:
                print("Insert the file name without the extension")
                filename = input("$> ")
                open(filename + ".java")
            except IOError:
                print("Error: File not found - " + filename)
                print(" ")
        elif shell == "2":
            Help(PATH)
        elif shell == "3":
            break
        
def readConfig():
    f = open("config.txt")
    for ff in f.readlines():
        file= ff.strip()
    if file != file + "/":
        file= file+ "/"
    return file

def Help(PATH):

if __name__ == "__main__":
    main()
