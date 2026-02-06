#select mode
mode = None
while not type(mode) == int and not mode in range(0, 2):
    mode = input("Enter mode(0 for dec-to-base, 1 for base-to-dec):\t")
    try:
        mode = int(mode)
    except:
        mode = None

#getting base
base = None
while not type(base) == int and not base in range(0, 16):
    base = input("Enter base(max: 16):\t")
    try:
        base = int(base)
    except:
        base = None

LETTERS = ["A", "B", "C", "D", "E", "F"]

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

def base_to_dec(base_num):
    result = 0
    for i in range(0, len(base_num)):
        ind = (i+1)*-1
        multiplier = base**i
        num = base_num[ind] * multiplier
        result = num + result
    return result


#dec-to-base
if mode == 0:
    #getting decimal num
    decimal_num = None
    while not type(decimal_num) == int:
        decimal_num = input("Enter decimal num:\t")
        try:
            decimal_num = int(decimal_num)
        except:
            decimal_num = None
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

#base-to-dec
if mode == 1:
    #getting base num
    base_num = input("Enter base num:\t")
    edited_base = []
    for i in range(0, len(base_num)):
        edited_base.append(base_num[i])
    base_num = edited_base
    for i in range(0, len(base_num)): 
        if base_num[i] in LETTERS:
            for x in range(0, 6):
                if base_num[i] == LETTERS[x]:
                    base_num[i] = x+10
        base_num[i] = int(base_num[i])
    print(base_to_dec(base_num))

