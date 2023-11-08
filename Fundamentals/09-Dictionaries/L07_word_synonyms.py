# Write a program, which keeps a dictionary with synonyms. The key of the dictionary will be the word. The value
# will be a list of all the synonyms of that word. You will be given a number n – the count of the words. After each
# term, you will be given a synonym, so the count of lines you should read from the console is 2 * n. You will be
# receiving a word and a synonym each on a separate line like this:
# •	{word}
# •	{synonym}
# If you get the same word twice, just add the new synonym to the list.
# Print the words in the following format:
# {word} - {synonym1, synonym2 … synonymN}

count_words = int(input())

word_synonyms = {}

for _ in range(count_words):
    word = input()
    synonym = input()

    if word not in word_synonyms:
        word_synonyms[word] = [synonym]
    else:
        word_synonyms[word].append(synonym)

for (key, values) in word_synonyms.items():
    print(f"{key} - {', '.join(values)}")

