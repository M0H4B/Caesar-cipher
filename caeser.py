#! /usr/bin/python
import os
filename=raw_input("please enter the filename : ")
#while
key=input("please enter you secret key :")
mode=raw_input("encrypt or decrypt : ")
read= open(filename,"r+" )
lele=read.read().split("\n")
s=""
for m in lele:
	s+=m
	s+="\n"
s=s.upper()
letters='ABCDEFGHIGKLMNOPQRSTUVWXYZ'
result=''
for sy in s:
        if sy in letters:
                num=letters.find(sy)
                if mode == 'encrypt':
                        num=num+key
                elif mode == 'decrypt':
                        num=num - key

                if num >= len(letters):
                        num= num -len(letters)
                elif num < 0:
                        num = num + len(letters)

                result= result + letters[num]

        else :
                result = result + sy
result=result.lower()
read.close()
if mode == 'encrypt':
		os.rename(filename,"encrypted")
		write=open("encrypted","w+")
		write.write(result)
else:
		os.rename("encrypted","test.txt")
		write=open("test.txt","w+")
                write.write(result)

write.close()
print "Done ..."
