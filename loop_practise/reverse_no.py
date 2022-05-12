no_1 = int(input("Enter a value : "))

rev = 0

# mod = no_1 % 10   #6
# rev = rev * 10 + mod  #6
# no_1 = no_1 // 10 #45

# mod = no_1 % 10 #5
# rev = rev * 10 + mod #6 * 10 + 5 = 65
# no_1 = no_1 // 10 #4

# mod = no_1 % 10 #4
# rev = rev * 10 + mod #65 * 10 + 4 = 654
# no_1 = no_1 // 10 #0

while no_1!=0:
    mod = no_1 % 10   
    rev = rev * 10 + mod  
    no_1 = no_1 // 10 # 0

print("Reverse : ",rev)



# Deepshika's Logic (Please go through it)
num=int(input("Enter the number : "))
while num!=0:
    mod=num%10 #6
    num//=10
    print(mod,end="")



