
def convert(sentence):
    new_sentence = ''
    words = sentence.split(' ')
    for j in range(len(words)):
        for i in range(len(words[j])):
            if words[j][i] in 'aeiouy':
                if (i != 0):
                    new_sentence += words[j][i:] + words[j][:i] + 'ay' + ' '
                else:
                    new_sentence += words[j] + 'yay' + ' '
                break
    return new_sentence
 
input_file = "input.in"
output_file = "output.in"
inputf = open(input_file, "r")
outputf = open(output_file, "w")

line = inputf.readline().strip()
while line:
    outputf.write(convert(line))
    outputf.write('\n')
    line = inputf.readline().strip()

inputf.close()
outputf.close()

'''
str = 'i cant speak pig latin'
print(str + '\n')
print(convert(str))
'''
