#getting decimal num
decimal_num = None
while not type(decimal_num) == int:
    decimal_num = input("Enter decimal num:\t")
    try:
        decimal_num = int(decimal_num)
    except:
        decimal_num = None

#getting base num
base = None
while not type(base) == int:
    base = input("Enter base(max: 16):\t")
    try:
        base = int(base)
    except:
        base = None

#convert decimal to base
def dec_to_base(decimal_num):
    nums = []
    while True:
        if decimal_num < base: #check if base is larger that num
            nums.append(decimal_num)
            break #stops scripts
        num = decimal_num // base
        num = decimal_num - (base * num) #checks remainders
        decimal_num = decimal_num // base
        nums.append(num) #adds remainders to list
    return nums

LETTERS = ["A", "B", "C", "D", "E", "F"] 
num_list = dec_to_base(decimal_num)
result = ""
for i in range(len(num_list)):
    num = 0
    if num_list[i] >= 10:
            for x in range(10, 16):
                if num_list[i] == x:
                    num = LETTERS[x-10]
    else:
        num = num_list[i]
    result = str(num) + result

print(result)
