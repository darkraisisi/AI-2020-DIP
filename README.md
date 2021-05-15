# AI-2020-DIP
2020 Hogeschool Utrecht 2020 Course on Distributed Processing.



# Initialisation :
`python mapper.py < english.txt | sort -k1,1| python reducer.py english`

`python mapper.py < dutch.txt | sort -k1,1| python reducer.py dutch`

# Mapper:
Here you can alter what char's will be converted to a standerd _

# Reducer:
The reducer will return and save a matrix of counted letter combinations.
Also normalizes the matrix, default can be changed.

# Comparer/ validation:
`python iterRow.py validation.txt`

# iterRow:
This python files ties everything together, just in a way to show it can be done without unreadable commands.
This file will print a  prediction per result and a final score per language.