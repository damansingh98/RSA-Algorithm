# 1 st Step
P = random_prime (2^25) #Prime1
Q = random_prime (2^25) #Prime2
N = P * Q
print (P, Q, N) # p r i n t s Prime1 , prime2 and product of Prime1 and Prime2
                                                                                    
phi = euler_phi (N)
print ( phi ) # p r i n t s number of elements in N


# 2nd Step
#Find E or Encryption Key
# Let
E = 79 # E i s a prime number and not a f a c t o r of phi (N)
L = gcd (E, phi )
print (L) #Prints gcd (E, phi ) = 1


# 3 rd Step
#Find D or Decryption Key
D = inverse_mod (E, phi )
print (D)

# 4 th Step
#Public = (N, E) and Private = (P, Q, D)
# RSA Encryption
#Encrypting Bob' s Message , M# => 02 05 19 21 18 05 20 15 04 
18 9 14 11 25 15 21 18 15 22 01 12 20 09 14 05.
#Perform ==> (M#)^E mod N
#All 25 i t e r a t i o n s . . . . . .
E1 = mod(2^E, N)
print (E1)
E2 = mod(5^E, N)
1
print (E2)
E3 = mod(19^E, N)
print (E3)
E4 = mod(21^E, N)
print (E4)
E5 = mod(18^E, N)
print (E5)
E6 = mod(05^E, N)
print (E6)
E7 = mod(20^E, N)
print (E7)
E8 = mod(15^E, N)
print (E8)
E9 = mod(4^E, N)
print (E9)
E10 = mod(18^E, N)
print (E10)
E11 = mod(9^E, N)
print (E11)
E12= mod(14^E, N)
print (E12)
E13= mod(11^E, N)
print (E13)
E14 = mod(25^E, N)
print (E14)
E15= mod(15^E, N)
print (E15)
E16 = mod(21^E, N)
print (E16)
E17= mod(18^E, N)
print (E17)
2
E18 = mod(15^E, N)
print (E18)
E19 = mod(22^E, N)
print (E19)
E20 = mod(01^E, N)
print (E20)
E21 = mod(12^E, N)
print (E21)
E22 = mod(20^E, N)
print (E22)
E23= mod(9^E, N)
print (E23)
E24 = mod(14^E, N)
print (E24)
E25 = mod(5^E, N)
print (E25)


# RSA Decryption
# perform => (E#)^D mod N
#a l l 25 i t e r a t i o n s
D1 = mod(E1^D, N)
print (D1) # p r i n t s = 2 or Alphabet = B
D2 = mod(E2^D, N)
print (D2) # p r i n t s = 5 or Alphabet = E
D3 = mod(E3^D, N)
print (D3) #p r i n t s = 19 or Alphabet = S
D4 = mod(E4^D, N)
print (D4) #p r i n t s = 21 or Alphabet = U
D5 = mod(E5^D, N)
print (D5) #p r i n t s = 18 or Alphabet = R
D6 = mod(E6^D, N)
print (D6) #p r i n t s = 5 or Alphabet = E
3
D7 = mod(E7^D, N)
print (D7) #p r i n t s = 20 or Alphabet = T
D8 = mod(E8^D, N)
print (D8) #p r i n t s = 15 or Alphabet = O
D9 = mod(E9^D, N)
print (D9) #p r i n t s = 4 or Alphabet = D
D10 = mod(E10^D, N)
print (D10) #p r i n t s = 18 or Alphabet = R
D11 = mod(E11^D, N)
print (D11) #p r i n t s = 9 or Alphabet = I
D12 = mod(E12^D, N)
print (D12) #p r i n t s = 14 or Alphabet = N
D13 = mod(E13^D, N)
print (D13) #p r i n t s = 11 or Alphabet = K
D14 = mod(E14^D, N)
print (D14) #p r i n t s = 25 or Alphabet = Y
D15 = mod(E15^D, N)
print (D15) #p r i n t s = 15 or Alphabet = O
D16 = mod(E16^D, N)
print (D16) #p r i n t s = 21 or Alphabet = U
D17 = mod(E17^D, N)
print (D17) #p r i n t s = 18 or Alphabet = R
D18 = mod(E18^D, N)
print (D18) #p r i n t s = 15 or Alphabet = O
D19 = mod(E19^D, N)
print (D19) #p r i n t s = 22 or Alphabet = V
D20 = mod(E20^D, N)
print (D20) #p r i n t s = 1 or Alphabet = A
D21 = mod(E21^D, N)
print (D21) #p r i n t s = 12 or Alphabet = L
D22 = mod(E22^D, N)
print (D22) #p r i n t s = 20 or Alphabet = T
4
D23 = mod(E23^D, N)
print (D23) #p r i n t s = 9 or Alphabet = I
D24 = mod(E24^D, N)
print (D24) #p r i n t s = 14 or Alphabet = N
D25 = mod(E25^D, N)
print (D25) #p r i n t s = 5 or Alphabet = E

# BE SURE TO DRINK YOUR OVALTINE

