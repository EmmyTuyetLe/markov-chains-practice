"""Generate Markov text from text files."""
import sys
from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path)
    contents = file.read()
    return contents
    
# print(open_and_read_file(sys.argv[1]))


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    words.append(None)
    for i in range(len(words)-2):
        key = (words[i], words[i+1])
        value = words[i+2]
        if key not in chains:
            chains[key] = []
        chains[key].append(value)

    return chains

# print(make_chains(open_and_read_file(sys.argv[1])))



def make_text(chains):
    """Return text from chains."""

    sentence = []
    keys_list = []
    values_list = []
    for key, value in chains.items():
        keys_list.append(key)
        values_list.append(value)

    first_item = keys_list[0][1]
    first_value = values_list[0]
    random_second_item = choice(first_value)
    
    new_key = (first_item, random_second_item)
    for item in new_key:
        sentence.append(item)

    while new_key in chains:
        for key, value in chains.items():
            if key == new_key:
                chosen_word = choice(value)
                sentence.append(chosen_word)
                new_key = (key[1], chosen_word)

    return " ".join(sentence[:-1])

# print(make_text(make_chains(open_and_read_file(sys.argv[1]))))

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
