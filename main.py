'''
Author: Deeshan Sharma
Date: June 6, 2020
Purpose: Magic trick to guess the user's number
'''

from win32com.client import Dispatch

def speak(line):
    speaker_number = 1
    spk = Dispatch("SAPI.SpVoice")
    vcs = spk.GetVoices()
    spk.Voice
    spk.SetVoice(vcs.Item(speaker_number))
    spk.Speak(line)

def displayList(lis, con):
    i = 0
    while i < 5:
        temp = input(f"Is your number present in this list (Please look carefully) {lis[i]} (y/n) = ").lower()
        if temp == 'y' or temp == 'n':
            con.append(temp)
            i += 1
        else:
            print("Wrong Input...")
    return check(lis, con)

def result(lis):
    Sum = lis[0]
    return Sum

def check(lis, con):
    res = 0
    for i, j in zip(lis, con):
        if j == 'y':
            res += result(i)
    return res

print("This is a magic trick where I will guess your number...\nLet's start")
print("\nGuess any number between 1-30")
set1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
set2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30]
set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30]
set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30]
set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
alllist = [set1, set2, set3, set4, set5]
con = []
# res = 0

res = displayList(alllist, con)
speak(f"Your number is {res}")