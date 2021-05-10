import sys

punctuation = [
    ' ', '.', ',', '?', '!', ':', ';', '-', '\'', '\"',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
]

for line in sys.stdin:
    filterd = line.strip().lower()
    for p in punctuation:
        filterd = filterd.replace(p, '_')

    words = [filterd[i:i+2] for i in range(0, len(filterd), 1)]
    for word in words:
        print(f'{word}\t{1}')