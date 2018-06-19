import math

#computes the cosine of two vectors
def cosine_formula(vec1, vec2):
    prod,one,two = 0,0,0
    if len(vec1)>=len(vec2):
    	first = vec2
    	second = vec1
    else:
    	first = vec1
    	second = vec2

    for word in first:
    	if word in second:
    		prod += first[word]+second[word]
    	one = prod*prod
    for word in second:
    	two += second[word]*second[word]
    return prod/math.sqrt(one*two)

# takes a text and returns list of strings
def get_list_sentence(text):
	stop = {".":1,"?":1,"!":1}
	dont = {" ":1,",":1, "-":1,"--":1, ":":1, ";":1, "!":1, "?":1, ".":1,"'":1,'"':1}
	text = text.replace(",","").replace(".","?").replace(";","").split("?")
	result = []
	tempList = []
	for sent in text:
		remove_spaces = sent.strip().lower()
		tempList = remove_spaces.split()
		if tempList:
			result.append(tempList)
	return result

# takes a file and returns list of strings
def get_sentence_from_files(filenames):
	result = []
	for file in filenames:
		with open(file) as f:
			for line in f:
				if line:
					text = "".join(line)
					temp = get_list_sentence(text)
				result += temp
	return result


# takes sentences and builds descriptor(dict of dicts)
def build_semantic_descriptors(sentences):
	final_dict = dict()
	for sentence in sentences:
		final_list = []
		for word in sentence:
			if word not in final_list:
				if word not in final_dict:
					final_dict[word] = {}
				temp_list = []
				for s in sentence:
					if s not in temp_list:
						if s != word:
							if s not in final_dict[word]:
								final_dict[word][s] = 1
							final_dict[word][s] += 1
							temp_list.append(s)
				final_list.append(word)
	return final_dict

# returns the correct answer for given word and choices
def similar_word(word,choices,semantic_descriptor):
	result_words = []
	if word not in semantic_descriptor:
		return "Sorry... Currently I can't find meaning of this word"
	else:
		word_predictor = semantic_descriptor[word]
	
	for word in word_predictor:
		result_words.append(word)

	for c in choices:
		if c in semantic_descriptor:
			for w in semantic_descriptor[c]:
				if w not in result_words:
					result_words.append(w)
	answer = ""
	max_points = -1

	for c in choices:
		if c not in semantic_descriptor:
			return "Sorry... Currently I can't find meaning of this word"
		option_desc = semantic_descriptor[c]
		point = cosine_formula(word_predictor,option_desc)
		if point>max_points:
			max_points = point
			answer = c
	return answer
		

files = ["pg7178.txt","2600-0.txt"]
sentences_list = get_sentence_from_files(files)
descriptor = build_semantic_descriptors(sentences_list)
word = raw_input("Enter a word ")
options = []
print "Please Enter options"
for option in range(1,5):
	print "option "+str(option)+"st"
	options.append(raw_input())

answer = similar_word(word,options,descriptor)
print "The answer is "+answer