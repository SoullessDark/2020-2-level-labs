"""
Lab 1
A concordance extraction
"""


def tokenize(text: str) -> list:
    """
    Splits sentences into tokens, converts the tokens into lowercase, removes punctuation
    :param text: the initial text
    :return: a list of lowercased tokens without punctuation
    e.g. text = 'The weather is sunny, the man is happy.'
    --> ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy']
    """
    trash = set("!.,?;:!#$%&()*+/<=>@^_{|}~-[]{}")
    c = ''
    tokens = []
    if type(text) is str:
        text = text.lower()
        for i in text:
            if i in trash:
                text = text.replace(i, c)
        text = text.split()
        tokens.extend(text)
    return tokens
    pass


def remove_stop_words(tokens: list, stop_words: list) -> list:
    """
    Removes stop words
    :param tokens: a list of tokens
    :param stop_words: a list of stop words
    :return: a list of tokens without stop words
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy']
    stop_words = ['the', 'is']
    --> ['weather', 'sunny', 'man', 'happy']
    """
    without_st_wrds = []
    if type(tokens) is list:
        for i in tokens:
            if i not in stop_words:
                without_st_wrds.append(i)

    return without_st_wrds
    pass


def calculate_frequencies(tokens: list) -> dict:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens without stop words
    :return: a dictionary with frequencies
    e.g. tokens = ['weather', 'sunny', 'man', 'happy']
    --> {'weather': 1, 'sunny': 1, 'man': 1, 'happy': 1}
    """
    freq = {}
    if type(tokens) is list and all(tokens):
        for i in tokens:
            frequencies = {i: tokens.count(i)}
            freq.update(frequencies)

    return freq
    pass


calculate_frequencies(['weather', 'sunny', 'man', 'happy'])


def get_top_n_words(freq_dict: dict, top_n: int) -> list:
    """
    Returns the most common words
    :param freq_dict: a dictionary with frequencies
    :param top_n: a number of the most common words to return
    :return: a list of the most common words
    e.g. tokens = ['weather', 'sunny', 'man', 'happy', 'and', 'dog', 'happy']
    top_n = 1
    --> ['happy']
    """
    top_n_words = []

    if type(freq_dict) is dict and type(top_n) is int:
        listed_dict = list(freq_dict.items())
        listed_dict.sort(key=lambda x: -x[1])
        sorted_dict = dict(listed_dict)
        for i, wrd in enumerate(sorted_dict):
            top_n_words.append(wrd)

    return top_n_words[:top_n]
    pass


def get_concordance(tokens: list, word: str, left_context_size: int, right_context_size: int) -> list:
    """
    Gets a concordance of a word
    A concordance is a listing of each occurrence of a word in a text,
    presented with the words surrounding it
    :param tokens: a list of tokens
    :param word: a word-base for a concordance
    :param left_context_size: the number of words in the left context
    :param right_context_size: the number of words in the right context
    :return: a concordance
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_context_size = 2
    right_context_size = 3
    --> [['man', 'is', 'happy', 'the', 'dog', 'is'], ['dog', 'is', 'happy', 'but', 'the', 'cat']]
    """
    conditions = [
        type(tokens) is list,
        type(word) is str,
        type(left_context_size) is int,
        type(right_context_size) is int
    ]

    if all(conditions):
        context = []
        word_numb = []
        for index, element in enumerate(tokens):
            if element == word:
                word_numb.append(index)

        for i in word_numb:
            if left_context_size > 0 and right_context_size > 0:
                context.append(tokens[i - left_context_size:i + right_context_size + 1])
            elif right_context_size > 0:
                context.append(tokens[i:i + right_context_size + 1])
            elif left_context_size > 0:
                context.append(tokens[i - left_context_size:i + 1])
            else:
                return []
        return context
    return []
    pass


def get_adjacent_words(tokens: list, word: str, left_n: int, right_n: int) -> list:
    """
    Gets adjacent words from the left and right context
    :param tokens: a list of tokens
    :param word: a word-base for the search
    :param left_n: the distance between a word and an adjacent one in the left context
    :param right_n: the distance between a word and an adjacent one in the right context
    :return: a list of adjacent words
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_n = 2
    right_n = 3
    --> [['man', 'is'], ['dog, 'cat']]
    """
    conditions = [
        type(tokens) is list,
        type(word) is str,
        type(left_n) is int,
        type(right_n) is int
    ]

    if all(conditions):
        concordance = get_concordance(tokens, word, left_n, right_n)
        adj_words = []

        if left_n > 0 and right_n > 0:
            for i in concordance:
                wrds = [[i[0], i[-1]]]
                adj_words.extend(wrds)
            return adj_words
        elif right_n > 0:
            for i in concordance:
                wrds = [[i[-1]]]
                adj_words.extend(wrds)
            return adj_words
        elif left_n > 0:
            for i in concordance:
                wrds = [[i[0]]]
                adj_words.extend(wrds)
            return adj_words
        return adj_words
    return []
    pass


def read_from_file(path_to_file: str) -> str:
    """
    Opens the file and reads its content
    :return: the initial text in string format
    """
    if type(path_to_file) is str:
        with open(path_to_file, 'r', encoding='utf-8') as fs:
            data = fs.read()

        return data


def write_to_file(path_to_file: str, content: list):
    """
    Writes the result in a file
    """
    if type(path_to_file) is str and type(content) is list:
        with open(path_to_file, 'w', encoding='utf-8') as file:
            for i in content:
                file.write(" ".join(i))
                file.write("\n")
    pass

def sort_concordance(tokens: list, word: str, left_context_size: int, right_context_size: int, left_sort: bool) -> list:
    """
    Gets a concordance of a word and sorts it by either left or right context
    :param tokens: a list of tokens
    :param word: a word-base for a concordance
    :param left_context_size: the number of words in the left context
    :param right_context_size: the number of words in the right context
    :param left_sort: if True, sort by the left context, False – by the right context
    :return: a concordance
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_context_size = 2
    right_context_size = 3
    left_sort = True
    --> [['dog', 'is', 'happy', 'but', 'the', 'cat'], ['man', 'is', 'happy', 'the', 'dog', 'is']]
    """
    conditions = [
        type(tokens) is list,
        type(word) is str,
        type(left_context_size) is int,
        type(right_context_size) is int,
        type(left_sort) is bool
    ]
    concordance = get_concordance(tokens, word, left_context_size, right_context_size)

    if all(conditions):
        if left_sort and left_context_size > 0:
            return sorted(concordance)
        if not left_sort and right_context_size > 0:
            return sorted(concordance, key=lambda x: x[left_context_size + 1])

    return []
    pass
