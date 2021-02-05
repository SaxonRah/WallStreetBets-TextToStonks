import spacy
from pprint import pprint

"""
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg
"""


class BasedException(Exception):
	pass


def spacy_gpu_nlp(text: str = ''):
	# GPU Computation
	spacy.prefer_gpu()

	# Load English tokenizer, tagger, parser, NER and word vectors
	# nlp = spacy.load("en_core_web_sm")   # Efficient - Good
	# nlp = spacy.load("en_core_web_md")  # Blend - Will fail, need to fix test 2_EntityPhraseConcept
	nlp = spacy.load("en_core_web_lg")  # Accurate - Good

	# Process whole document
	doc = nlp(text)

	# Analyze syntax of parts
	noun_phrases = [chunk.text for chunk in doc.noun_chunks]
	verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]

	ne_p_and_c = {'0_Verbs': [],
				  '1_NounPhrases': [],
				  '2_EntityPhraseConcept': []}

	# Find named entities, phrases and concepts
	for entity in doc.ents:
		ne_p_and_c['2_EntityPhraseConcept'].append(entity.text)

	ne_p_and_c['1_NounPhrases'] = noun_phrases
	ne_p_and_c['0_Verbs'] = verbs

	# print('Returning from spacy_gpu_nlp')
	# pprint(ne_p_and_c)
	# print('Returning from spacy_gpu_nlp')

	return ne_p_and_c


def self_test():
	text = ("When Sebastian Thrun started working on self-driving cars at "
			"Google in 2007, few people outside of the company took him "
			"seriously. “I can tell you very senior CEOs of major American "
			"car companies would shake my hand and turn away because I wasn’t "
			"worth talking to,” said Thrun, in an interview with Recode earlier "
			"this week.")

	assert_ne_p_and_c = ['Sebastian Thrun', 'Google', '2007', 'American', 'Thrun', 'Recode', 'earlier this week']
	assert_noun_phrases = ['Sebastian Thrun', 'self-driving cars', 'Google', 'few people', 'the company', 'him', 'I',
						   'you', 'very senior CEOs', 'major American car companies', 'my hand', 'I', 'Thrun',
						   'an interview', 'Recode']
	assert_verbs = ['start', 'work', 'drive', 'take', 'can', 'tell', 'would', 'shake', 'turn', 'talk', 'say']

	ne_p_and_c = spacy_gpu_nlp(text)
	try:
		try:
			assert ne_p_and_c['0_Verbs'] == assert_verbs
		except AssertionError:
			raise BasedException('0_Verbs Failed')
		try:
			assert ne_p_and_c['1_NounPhrases'] == assert_noun_phrases
		except AssertionError:
			raise BasedException('1_NounPhrases Failed')
		try:
			assert ne_p_and_c['2_EntityPhraseConcept'] == assert_ne_p_and_c
		except AssertionError:
			raise BasedException('2_EntityPhraseConcept Failed')

	except BasedException as be:
		print('BasedException:', be)
		print('FAILURE: spacy_gpu_nlp self_test failed.')
	else:
		print('SUCCESS: spacy_gpu_nlp self_test completed.')


self_test()
