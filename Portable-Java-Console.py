#-*- coding: UTF-8 -*-
import shutil, os

def main():
    print("Portable Java Console v1.0")
    print(" ")
    print("Modify the config file to set your JDK bin folder path")
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
                try:
                    execute(PATH, filename)
                except IOError:
                    print("Error: " + PATH + " doesn't exit")
                    print(" ")
            except IOError:
                print("Error: File not found - " + filename)
                print(" ")
        elif shell == "2":
            Help(PATH)
        elif shell == "3":
            break

def execute(PATH, filename):
    currentFile = os.path.realpath(filename + ".java")
    currentDir = os.path.dirname(currentFile)
    shutil.copy2(currentFile, PATH + filename + ".java")
    os.popen("start " + PATH+ "javac " + PATH + filename + ".java").read()
    shutil.copy2(PATH + filename + ".class", currentDir);
    executeBat(PATH, filename)
    #os.popen("start " + PATH + "java " + filename).read()

def readConfig():
    f = open("config.txt")
    for ff in f.readlines():
        file= ff.strip()
    if file != file + "/":
        file= file+ "/"
    return file

def Help(PATH):
    print(" ")
    print("Portable Java Console v1.0 Copyright 2016 Anas Araid")
    print(" ")
    print("Current path: " + PATH)
    print(" ")
    print("Set your JDK bin folder path in the config.txt ")
    print("The path MUST NOT have spaces or quotation marks. So move it somewhere else. ")
    print("Ex. wrong path --> 'C:/Program Files/Java/jdk-version/bin'")
    print("Ex. right path --> 'C:/jdk-version/bin' ")
    print(" or F:/jdk-version/bin")
    print(" ")
    print("Insert the script file name without the extension.")
    print("Ex. filename")
    print(" ")

if __name__ == "__main__":
    main()
