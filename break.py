with open('transcript.txt','r') as f, open('transcript2.txt', 'w') as f2:
    for line in f:
       for word in line.split():
           f2.write(word + '\n')
