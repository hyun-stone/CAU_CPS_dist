from math import gcd
import sys
p =int(input("p를 입력하세요")) # p 입력
q= int(input("q를 입력하세요"))  # q 입력

n = p * q
phi_n = (p-1) * (q-1)

while True:
    e = int(input("n = {0} 과 서로소이면서 1보다 크고 phi_n = {1} 보다 작은 수 입력".format(str(n),str(phi_n)))) # e 입력
    if gcd(e,n) == 1:    #e가 서로소라면 break
        break
        
d = 0
mod = 0

while True:
    d += 1
    mod = (e*d) % phi_n
    if mod == 1:
        break
        
# print(d)

# Encryption
# c = p^e mod n

plane = list(input("평문을 입력하세요.")) # 평문 입력

plane_list = [ord(x) for x in plane]

cipher = []
for i in plane_list:
    x = (i ** e) % n
    cipher.append(int(x))

    
# Decryption
# p =c^d mod n

decrypted = []
for i in cipher:
    x = (i ** d) % n
    decrypted.append(int(x))

print("plane text", plane_list)
print("cipher text", cipher)
print("dedecrypted text", decrypted)

decrypted_text = ''.join ([chr(x) for x in decrypted])
print(decrypted_text)
