# Exit codes
ALL_OK=100
ERR_PARAM=-10
D_SMALLER_ZERO=-20

# ----------------
def validate_param(param):
    try:
        int(param)
        return True
    except:
        return False
# ----------------
def discriminant(a, b, c):
    return b ** 2 - 4 * a * c
# ----------------
def roots(d, a, b):
    # we dont calculate when D<0
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return [x1, x2]
# ----------------
def square_print(roots):
    print("RESULTS: ")
    print(roots)
# ----------------
def solv_square(a, b, c):
    d = discriminant(a, b, c)
    if d >= 0:
        X = roots(d, a, b)
        square_print(X)
        return True
    else:
        return False
#------------------
if __name__ == '__main__':
    print('Script a*x2+b*x+c=0')
    a = input('Input a: ')
#---------check A -------
    cnt=0
    while validate_param(a)==False:
        print("Param is not integer! You can try max 3 times again")
        a = input('Input a again: ')
        if cnt==2:
            break
        cnt+=1
    if validate_param(a)==False:
        exit(ERR_PARAM)
    a = int(a)
# ---------check B -------
    b = input('Input b: ')
    cnt = 0
    while validate_param(b) == False:
        print("Param is not integer! You can try max 3 times again")
        b = input('Input b again: ')
        if cnt == 2:
            break
        cnt += 1
    if validate_param(b) == False:
        exit(ERR_PARAM)
    b = int(b)
# ---------check C -------
    c = input('Input c: ')
    cnt = 0
    while validate_param(c) == False:
        print("Param is not integer! You can try max 3 times again")
        c = input('Input c again: ')
        if cnt == 2:
            break
        cnt += 1
    if validate_param(c) == False:
        exit(ERR_PARAM)
    c = int(c)
# ------------------------
    if solv_square(a, b, c)==False:
        exit(D_SMALLER_ZERO)
    exit(ALL_OK)


