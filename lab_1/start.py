"""
Concordance implementation starter
"""

import main
import os

if __name__ == '__main__':
    #  use data.txt file to test your program
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data = main.read_from_file(os.path.join(current_dir, 'data.txt'))
    stop_words = ['was', 'a']

    #  here goes your logic: calling methods from concordance.py

    tokens = main.tokenize(data)
    print("your tokens, dear:", tokens[:10])

    tokens = main.remove_stop_words(tokens, stop_words)
    print("your tokens without stop words, dear:", tokens[:10])

    frequencies = main.calculate_frequencies(tokens[:1000])
    print("let's look at frequencies, dear:", frequencies[tokens[2]])

    top_3_words = main.get_top_n_words(frequencies, 3)
    print("top 3 words:", top_3_words)

    concordance = main.get_concordance(tokens, 'year', 2, 3)
    print("here is your concordance:", concordance[:5])

    adjacent_words = main.get_adjacent_words(tokens, 'year', 2, 3)
    print("take a look at adjacent words for 'book':", adjacent_words[:4])

    sorted_concordance = main.sort_concordance(tokens, 'year', 2, 3, False)
    print("here is a sorted concordance:", sorted_concordance[:3])

    main.write_to_file('report.txt', sorted_concordance)
    print("File was written successfully")

    RESULT = sorted_concordance[:3]
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT == [['less', 'frequently', 'year', '1006', 'ab', 'urbe'],
                      ['the', 'previous', 'year', '1031', 'ayrton', 'shunt'],
                      ['less', 'frequently', 'year', '1093', 'ab', 'urbe']], 'Concordance not working'
