# import pandas as pd

# df = pd.DataFrame({
#   'course': ['Mathematik', 'Englisch', 'Deutsch', 'BWL', 'Biologie', 'Physik'],
#   'score': [10, 5, 8, 12, 9, 13]
# })

# cutoff=[0, 1, 3, 6, 9, 12, 15]
# grades = ['Ungenügend', 'Mangelhaft', 'Ausreichend', 'Befriedigend', 'Gut', 'Sehr gut']

# # df['grades'] = pd.cut(df['score'], labels=grades, bins=cutoff)
# df['grades'] = pd.cut(df['score'], bins=cutoff, right=None, labels=grades, retbins=False, precision=13, include_lowest=False, ordered=False)


# print(df)


import pandas as pd

df = pd.DataFrame({
  'name': ["Max", "Julia", "Lena", "Paul", "Sophie", "Tim", "Mia", "Jonas", "Emma", "Felix"],
  'age': [69, 45, 3, 14, 63, 47, 41, 7, 51, 66]
})

cutoff=[0, 12, 17, 64, 100]
employability = ['False', 'halfway', 'True', 'False']

df['employability'] = pd.cut(df['age'], labels=employability, bins=cutoff, ordered=False)

print(df)