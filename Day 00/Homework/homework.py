def hw1(a,b,c):
    if a % c == 0 and b % c != 0:
        return (b-a)//c+1
    else:
        return (b-a)//c
    
print(hw1(1,20,5))
print(hw1(5,16,4))
print(hw1(3,502,13))
converter = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, 
    "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, 
    "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, 
    "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
    "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
}


def hw2(num,x):
    if "." in str(num):
        num = str(num)
        listn = num.split(".")
        sum = 0
        a = listn[0]
        b = listn[1]
        y = 0
        for i in range(len(a)-1,-1,-1):
            sum += int(a[i]) * (x**y)
            y += 1
        z= -1
        for i in range(len(b)):
            sum += int(b[i]) * (x**z)
            z -= 1
        return sum
    else:
        num = str(num)
        sum = 0
        y = 0
        for i in range(len(num)-1,-1,-1):
            sum += converter[num[i]] * (x**y)
            y += 1
        return sum
    
print(hw2(520.3,6))
print(hw2(1052,16))
print(hw2("FFF1",16))
        


