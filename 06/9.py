m = int(input())
ingredients = set()
recipe_ingredients = set()
for i in range(m):
    ingredients.add(input())
n = int(input())
for i in range(n):
    recipe = input()
    number_ingredients = int(input())
    for j in range(number_ingredients):
        recipe_ingredient = input()
        recipe_ingredients.add(recipe_ingredient)
    if recipe_ingredients <= ingredients:
        print(recipe)
