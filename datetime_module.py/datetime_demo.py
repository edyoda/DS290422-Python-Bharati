import datetime as dt

date = dt.datetime.now()

print(date)

print(date.month)

print(date.year)

print(date.day)

print(date.hour)

print(date.minute)

print(date.second)

print("A : ",date.strftime("%A"))

print("a : ",date.strftime("%a"))

print("B : ",date.strftime("%B"))

print("b : ",date.strftime("%b"))

print("C : ",date.strftime("%C"))

print("c : ",date.strftime("%c"))

print("A : ",date.strftime("%D"))

print("A : ",date.strftime("%d"))

print("W : ",date.strftime("%w"))

print("M : ",date.strftime("%m")) #month

print("Y : ",date.strftime("%Y"))

print("y : ",date.strftime("%y"))

print("H : ",date.strftime("%H"))

print("I : ",date.strftime("%I"))

print("P : ",date.strftime("%p"))

print("M : ",date.strftime("%M")) #minute

print("S : ",date.strftime("%S"))

print("V : ",date.strftime("%V"))

print("f : ",date.strftime("%f"))

print("j : ",date.strftime("%j"))

print("U : ",date.strftime("%U"))

print("x : ",date.strftime("%x"))

print("X : ",date.strftime("%X"))

print("% : ",date.strftime("%%"))

print("% : ",date.strftime("%G"))

print("% : ",date.strftime("%u"))


# date = dt.datetime(2022,6,5,4,30,45,5746)
# print(date)