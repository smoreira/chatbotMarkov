import markovify

#ler o arquivo texto
with open('reflexoes.txt') as f:
	texto = f.read()

#criar modelo markov
model = markovify.Text(texto)

#loop do chat
while True:
	i = raw_input("> ")

	o = model.make_short_sentence(60)

	print 'Voce: ' + i
	print 'Bot: ' + str(o) 