import sys,re

key_word = ['BEGIN','END','FOR','IF','THEN','ELSE']
delimiters = [':','+','*',',','(',')',':=']


input = sys.argv[1]
lines = open(input,'r').readlines()
for line in lines:
    word = ''
    i = 0
    while i <len(line):
        if line[i]==' ' or line[i]=='\t' or line[i]=='\r' or line[i]=='\n':
            i+=1
            continue
        else:
            word=''
        
        if line[i].isalpha():
            while i <len(line) and (line[i].isalpha() or line[i].isdigit()):
                word+=line[i]
                i+=1
            i-=1
            if word in key_word:
                key_index=key_word.index(word)
                if key_index==0:
                    print("Begin")
                elif key_index==1:
                    print("End")
                elif key_index==2:
                    print("For")
                elif key_index==3:
                    print("If")
                elif key_index==4:
                    print("Then")
                elif key_index==5:
                    print("Else")
            else:
                print("Ident("+word+")")
        elif line[i].isdigit():
            while i <len(line) and line[i].isdigit():
                word+=line[i]
                i+=1
            i-=1
            print("Int("+word.lstrip('0')+")")
        elif line[i] in delimiters:
            d_index=delimiters.index(line[i])
            if d_index==0:
                if i+1<len(line) and line[i+1]=='=':
                    i+=1
                    print("Assign")
                else:
                    print("Colon")
            elif d_index==1:
                print("Plus")
            elif d_index==2:
                print("Star")
            elif d_index==3:
                print("Comma")
            elif d_index==4:
                print("LParenthesis")
            elif d_index==5:
                print("RParenthesis")
        else:
            print("Unknown")
            exit(0)
        i+=1