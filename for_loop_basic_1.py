
# 1
for basic in range(1, 151):
    print(basic)


# 2
for mult_of_five in range(5, 1001, 5):
    print(mult_of_five)

    print([5]+list(range(5,1001,5))) 

# 3
for counting_dojo_way in range(1, 101):
    if counting_dojo_way %5== 0:
        print("Dojo")
    else:
        print(counting_dojo_way)

# 4
for huge_sucker in range(0, 5000001):
    if huge_sucker %2!= 0:        
        print(huge_sucker)

# 5
for down_by_fours in range(2018, -1, -4):
    print(down_by_fours)

#6
low_num = 2
high_num = 9
mult = 3
print(mult)
print(low_num * mult)
print(high_num)

print(mult, low_num * mult, high_num)