#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  A = ingredients
  B = recipe
  Alist = []
  Blist = []

  for v in A:
    Alist.append(v)

  for v in B:
    Blist.append(v)

  Aset = set(Alist)
  Bset = set(Blist)

  if Bset.issubset(Aset):
    batches = []
    for i in Alist:
      batches.append(A[i] // B[i])

    batches = set(batches)

    return min(batches)
  else:
    return 0 



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))