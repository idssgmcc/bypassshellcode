import os
import re

binname = input("请输入二进制文件名：\n")

cmd = f"hexdump {binname} | cut -d \" \" -f 2-8 | sed '$s/.*//' > out.txt"
os.system(cmd)

f = open("out.txt", "r")
counter = 1
shellcode = ""
comb = ""

raw = str(f.read())
hex_code = re.sub("\s+", "", raw)

for i in hex_code:
    if counter % 2 == 0:
        shellcode += '\\x' + str(comb)
        comb = ""
    comb += str(i)
    counter += 1

print("\n\n")
print(shellcode)
f.close()
os.system("rm out.txt")
