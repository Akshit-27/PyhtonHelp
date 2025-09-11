import ast
input_str = input("Enter Day & Vacation : ")

input_list = ast.literal_eval(input_str)
day_of_week = input_list[0]
is_on_vacation = input_list[1]

weekend = [6,7]
def clock (day,vaction):
    if is_on_vacation :
        if day_of_week not in weekend :
            return "10:00"
        else :
            return "OFF"
    else:
        if day_of_week in weekend:
            return "10:00"
        else :
            return "7:00"


print (clock(day_of_week,is_on_vacation))

# Enter Day & Vacation : 4 , True
# 10:00

# Enter Day & Vacation : 7, False
# 10:00

# Enter Day & Vacation : 7,True
# OFF

# Enter Day & Vacation : 1,False
# 7:00
