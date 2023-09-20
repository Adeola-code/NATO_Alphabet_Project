import pandas

# Create dictionary fo the csv file
alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {row.letter: row.code for (index, row) in alphabets.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.



word = input("Enter a word: ").upper()


output_list = [nato[letter] for letter in word]
print(output_list)
