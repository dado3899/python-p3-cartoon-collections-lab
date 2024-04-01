def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        print(f"{num}. {dwarf}")
        num += 1

def summon_captain_planet(calls):
    # new_list = []
    # for call in calls:
    #     new_list.append(call.capitalize()+"!")
    # return new_list
    return [call.capitalize()+"!" for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(food):
    cheese_list = ("cheddar", "gouda", "camembert")
    for ingredient in food:
        if ingredient in cheese_list:
            return ingredient
    return None

# solution = summon_captain_planet(["earth", "wind", "fire", "water", "heart"])
# print(solution)
# solution = long_planeteer_calls(["two", "go", "ind", "bop"])
# print(solution)
# roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])
# solution = find_the_cheese(["crackers", "gouda", "thyme"])
# print(solution)
# ingredients = ["crackers", "gouda", "thyme"]
# ingredients.map(i => i+"!")
# new_list = [i+"!" for i in ingredients]
# print(new_list)