from datetime import datetime
seed = datetime.now().microsecond // 1000

def get_random(seed):
    rand = (1103515245 * seed + 12345) % (2**31)
    return rand

def random(mod):
    global seed
    rand = get_random(seed)
    seed = rand
    rand_num = rand % mod
    return rand_num

print(random(100))

print(random(100))
