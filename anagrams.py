from flask import Flask, request, render_template
app = Flask(__name__)

def setup_dictionary(list_of_words):
    '''
    For an input list of words, generates a dictionary with
    lexigraphically-sorted items as keys, values as a list of all items 
    that generate a given lexigraphic-sort:

    EXAMPLE:
    >>> setup_dictionary(['step','banana','pest'])
    {'aaabnn': ['banana'], 'epst': ['step', 'pest']}
    '''

	# adding more comments is fun and stuff
    # hold the lexigraphically-sorted dictionary
    lex_dict = {}
    for item in list_of_words:
        lex_sorted_item = "".join(sorted(item))
        if lex_sorted_item not in lex_dict:
            lex_dict[lex_sorted_item] = [item]
        else:
            lex_dict[lex_sorted_item] += [item]
    return lex_dict

def find_anagrams(word, lex_dict):
    '''
    Finds all anagrams for a given input word.

    Input:
    word     = any sequence of characters
    lex_dict = lexigraphically sorted dictionary (use setup_dictionary())
	'''
	

    lex_word = "".join(sorted(word))
    dict_result = []
    if lex_word in lex_dict:
        dict_result = [item for item in lex_dict[lex_word] if item != word]
    if dict_result == [] or (len(dict_result) == 1 and dict_result[0] == word):
        return None
    else:
        return "%s" % (dict_result)

# get all words from dictionary in web2
unix_dict = open("web2",'r')
list_of_words = [item.strip() for item in unix_dict.readlines()]

# pre-sort the words into a dictionary
sorted_dictionary = setup_dictionary(list_of_words)

@app.route('/anagrams')
def hello_world():
    request_word = request.args.getlist('word')
    if request_word != []:
        listOfAnagrams = find_anagrams(request_word[0].lower(), sorted_dictionary)
        return render_template('anagrams.html', anagrams=listOfAnagrams, word=request_word[0])
    else:
        return render_template('anagrams.html', anagrams=None, word=None)

if __name__ == '__main__':
    app.run(debug=True, host="192.249.58.45",port=5500)