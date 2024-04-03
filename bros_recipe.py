'''
❓ PROMPT
You found a note from your brother when you got home from school:

"Doofus, go to the store to pick up some ingredients for my recipe. Don't buy anything we already have at home like last time. I didn't make the grocery list so you'll have to do it yourself and then go to the store to buy the missing ingredients, you lazy bum. Use your own money to pay for it; you owe me for only pranking you 5 times this week anyway. Get it done before dinnertime, loser."

Your brother's a jerk and gave you the recipe in the hardest possible way to decipher: one long line of all the quantities followed by all the ingredients. Meanwhile, the ingredients at home are in tabular format, ugh!

Example(s)
Recipe: "12 3 3 1 egGs baCon sAusaGe souRdoughBread"
At home: {"SauSage": 6, "EGgs": 4, "BACoN": 3, "banAnA"; 1}
Grocery list: {"eggs": 8, "sourdoughbread": 1}

You need 12 eggs but you only have 4 at home, so you need 8 more, dweeb.
You need 3 bacon and you have 3 at home, so you don't need anymore, dweeb.
You need 3 sausage and you have 6 at home, so you don't need anymore, dweeb.
You need 1 sourdoughbread but you have none at home, so you need 1 more, dweeb.
The banana isn't a part of the recipe, so it doesn't matter, dweeb.

Your brother swears he could do this so much faster than you, but he's got more important things to do like go grind the half-pipe with some gnarly shredz.
'''
def build_dict_from_string(recipe):
    lower_arr = recipe.lower().split()
    result = {}
    counts = []
    idx = 0
    for v in lower_arr:
        if v.isnumeric():
            counts.append(int(v))
        else:
            result[v] = counts[idx]
            idx += 1
    return result


def generate_list(recipe, at_home):
    recipe_dict = build_dict_from_string((recipe))
    print('recipe_dict:', recipe_dict)
    for key in at_home:
        lower_key = key.lower()
        at_home_count = at_home[key]
        if lower_key in recipe_dict:
            if recipe_dict[lower_key] > at_home_count:
                recipe_dict[lower_key] -= at_home_count
            else:
                del recipe_dict[lower_key]
    return recipe_dict


recipe = "12 3 3 1 egGs baCon sAusaGe souRdoughBread"
at_home = {"SauSage": 6, "EGgs": 4, "BACoN": 3, "banAnA": 1}
grocery_list = {"eggs": 8, "sourdoughbread": 1}
print(generate_list(recipe, at_home))