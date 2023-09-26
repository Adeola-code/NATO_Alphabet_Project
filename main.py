import pandas

# Create dictionary fo the csv file
alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {row.letter: row.code for (index, row) in alphabets.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet letters")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()