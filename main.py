# 1st program
print(9**0.5*5)  # variant 1
print((9**0.5)*5)    # variant 2

# 2st program
print(9.99>9.98 and 1000!=1000.1)

# 3st program
print(1234%1000//10+5678%1000//10)  # variant 1
print(1234//10%100+5678//10%100)  # variant 2.

# 4st program
print((13.42//1==42.13*100%100) or (13.42*100%100==42.13//1))    # variant 1
print(int(13.42)==int(42.13*100%100) or int(13.42*100%100)==int(42.13))    #variant 2
print(int(13.42)==42.13*100%100 or 13.42*100%100==int(42.13))    # variant 3
# варианты с присвоением переменным значений
a=13.42
b=42.13
print(a//1==b*100%100 or a*100%100==b//1)    # variant 4
print(int(a)==b*100%100 or a*100%100==int(b))    # variant 5