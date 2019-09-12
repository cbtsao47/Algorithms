#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # initialize batches made
  batches =0
  # check if we have enough ingredients
  enough_ingredients=True
  # make a batch as long as there are enough ingredients
  while enough_ingredients:
    # subtract recipe required amount from available ingredient amounts
    for key in recipe:
      if ingredients.get(key) == None or ingredients[key]-recipe[key]<0:
        enough_ingredients=False
      else:
        ingredients[key]=ingredients[key]-recipe[key]
    # increase batches
    if enough_ingredients:
      batches+=1
    
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))