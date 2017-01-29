#a program to decode secret messages with Gabe
from numpy import zeros

def decode(msg, shift):
    bin_msg = ""
    for letter in msg:
        if letter == '|':
            bin_msg += '1'
        elif letter == '_':
            bin_msg += '0'
        else:
            bin_msg += letter
    #print(bin_msg)
    
    nums = zeros(300, dtype="int") 
    i = 0
    num = ""
    for letter in bin_msg:
        if letter in ('0','1'):
            num += letter
        else:
            if num != "":
                nums[i] = int(num)
                i += 1
                num = ""
            if letter == " ":
                nums[i] = -1
                i += 1
    #print(nums)
    
    last = 0
    for i in range(300):
        if nums[i] == 0:
            last = i
            break
        elif nums[i] == -1:
            continue
        else:
            nums[i] = int(str(nums[i]), 2) - 1

    alpha = "abcdefghijklmnopqrstuvwxyz"
    letters = ""
    for i in range(300):
        if i == last:
            break
        if nums[i] == -1:
            letters += " "
            continue
        x = nums[i] - shift
        if x < 0:
            x += 26
        new_letter = alpha[x]
        if new_letter == 'f':
            new_letter = 'n'
        elif new_letter == 'z':
            new_letter = 'k'
        elif new_letter == 'c':
            new_letter = 'm'
        elif new_letter == 'o':
            new_letter = 'c'
        elif new_letter == 'u':
            new_letter = 'o'
        elif new_letter == 'n':
            new_letter = 'u'
        elif new_letter == 'm':
            new_letter = 'x'
        elif new_letter == 'q':
            new_letter = 'p'
        
        letters += new_letter
        
    return letters;

def main():
    
    code = "|__|_-||_-||__|-|__-||___-|___|, ||_-||-|__-|____-|_|||! ||| |_-||__|-|____-|| |___|-||__|-|_||| |__|_-||_-||__|-|__|_ |-|_||| ||_|_-|||-|____-|__|_-||_-|_-||__|-|_||| |_|_|-||__|-|___| |||-|__-|_-||-||-|_ |___|-|_|_|-||-|_|_-|_|_, ||__|-|__-|_ |_-||-||_|-|__||-|_-|||-|__-|_| |_|||-|__||-||__-|____ |___|-||-||_|-|____-||-|__|_ |-||-|___|-|___|-||__|-|_|-|| |_|_|-||__|-|___| ||__|-|__ ||-|__-||_|-||_-||__|-|__-|__|_-|||-|__-|_| ||-|_||-||||-||-|____-|||-||-|__-||_|-||.";

    print( decode(code,24) + "\n" )
		
main()
