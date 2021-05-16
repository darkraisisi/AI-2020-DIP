python mapper.py < english.txt | sort -k1,1| python reducer.py english

python mapper.py < dutch.txt | sort -k1,1| python reducer.py dutch

python main.py validation.txt