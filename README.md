# AI-2020-DIP
2020 Hogeschool Utrecht 2020 Course on Distributed Processing.

`python mapper.py < english.txt | sort -k1,1| python reducer.py english`

Validation:
`python iterRow.py validation.txt | sort -k1,1| python reducer.py testfolder/a`
