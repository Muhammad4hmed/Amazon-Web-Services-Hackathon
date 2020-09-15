import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer=LancasterStemmer()
import pickle
import numpy
import tflearn
import tensorflow
import random
import json
import pyttsx3

def tts(txt):
	engine=pyttsx3.init()
	engine.say(txt)
	engine.runAndWait()


try:
	with open('data.pickle','rb') as f:
		words,labels,training,output=pickle.load(f)
except:
	with open('intents.json') as file:
		data=json.load(file)

	words=[]
	labels=[]
	docs_x=[]
	docs_class=[]
	for intent in data['intents']:
		for pattern in intent['patterns']:
			word_single=nltk.word_tokenize(pattern)
			words.extend(word_single)
			docs_x.append(word_single)
			docs_class.append(intent['tag'])
		if intent['tag'] not in labels:
			labels.append(intent['tag']) 

	words=[stemmer.stem(w.lower()) for w in words if w not in '?']
	words=sorted(list(set(words)))

	labels=sorted(labels)

	training=[]
	output=[]
	out_empty=[0 for _ in range(len(labels))]

	for x,doc in enumerate(docs_x):
		bag=[]

		word_single=[stemmer.stem(w) for w in doc]

		for w in words:

			if w in word_single:
				bag.append(1)
			else:
				bag.append(0)
		output_row=out_empty[:]
		output_row[labels.index(docs_class[x])]=1

		training.append(bag)
		output.append(output_row)
	training=numpy.array(training)
	output=numpy.array(output)

	with open('data.pickle','wb') as f:
		pickle.dump((words,labels,training,output),f)


try:
	tensorflow.reset_default_graph()
	net=tflearn.input_data(shape=[None,len(training[0])])
	net=tflearn.fully_connected(net,8)
	net=tflearn.fully_connected(net,16)
	net=tflearn.fully_connected(net,8)
	net=tflearn.fully_connected(net,len(output[0]),activation='softmax')
	net=tflearn.regression(net)

	model=tflearn.DNN(net,tensorboard_dir='log')
	model.load('my_model.tflearn')

except:
	tensorflow.reset_default_graph()
	net=tflearn.input_data(shape=[None,len(training[0])])
	net=tflearn.fully_connected(net,8)
	net=tflearn.fully_connected(net,16)
	net=tflearn.fully_connected(net,8)
	net=tflearn.fully_connected(net,len(output[0]),activation='softmax')
	net=tflearn.regression(net)

	model=tflearn.DNN(net,tensorboard_dir='log')

	model.fit(training,output,n_epoch=1500,batch_size=8,show_metric=True)
	model.save('my_model.tflearn')

def bag_of_words(s,words):
	bag=[0 for _ in range(len(words))]
	s_words=nltk.word_tokenize(s)
	s_words=[stemmer.stem(word.lower()) for word in s_words]

	for x in s_words:
		for i,w in enumerate(words):
			if w==x:
				bag[i]=1
	return numpy.array(bag)

def chat(inp):
	import random
	#print('Enter a robotics related query!(type quit to stop)')
	while True:
		if inp.lower()=='quit':
			break
		results=model.predict([bag_of_words(inp,words)])[0]
		'''with open('chatbot.pb','wb') as f:
									pickle.dump(model,f)'''
		results_idx=numpy.argmax(results)
		idx=random.randint(0, 1)

		if results[results_idx]>0.3:

			tag=labels[results_idx]
			with open('intents.json') as file:
				data=json.load(file)

				
			for trunc in data['intents']:
				if trunc['tag']==tag:
					responses=trunc['responses']
					prefix=trunc['response_pre_string']
					suffix=trunc['response_post_string']
			txt=random.choices(responses)


			
			return("{}".format(txt[0]))

			
			#print(tag)

			#print(tts(txt))
		else: return('If you still feel that your query was unaddressed feel free to mail us at  support@toll_automator.in')

print(chat("I can't sign in"))