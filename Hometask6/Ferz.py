from random import randint

def check_ferz (ferz):
    for i in range(len(ferz)):
        for j in range(i + 1, len(ferz)):
            if ferz[i][0] == ferz[j][0] or ferz[i][1] == ferz[j][1] or abs(ferz[i][0] - ferz[j][0]) == abs(ferz[i][1] - ferz[j][1]):
                return False
    return True


def gen_ferz():
           
    ferz = []
    while len(ferz) < 8:
        new_ferz = (randint(1, 8), randint(1, 8))
        if new_ferz not in ferz:
            ferz.append(new_ferz)

    return ferz
def generate_successful_arrangements():
    
        
    successful_arrangements = []

    def generate_ferz(ferz, current_row):
        if current_row > 8: 
            successful_arrangements.append(ferz)
            return

        for col in range(1, 9):
            new_ferz = (current_row, col)

            if all(not (new_ferz[0] == q[0] or new_ferz[1] == q[1] or abs(new_ferz[0] - q[0]) == abs(new_ferz[1] - q[1])) for q in ferz):
                generate_ferz(ferz + [new_ferz], current_row + 1) 
    generate_ferz([], 1) 

    return successful_arrangements