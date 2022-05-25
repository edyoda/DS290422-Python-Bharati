print(__name__)

def addition():
    print("Addition call ho raha hai phele")
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    add = no1 + no2
    return add

def division():
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    div = no1 / no2
    return div

if __name__ == "__main__":
    result = addition()
    print("Addition : ",result)