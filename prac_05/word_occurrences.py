def main():
    counted_word = {}
    sentence = input("Please enter a sentence to be checked: ")
    sentence_parts = sentence.split()

    for each_word in sentence_parts:
        unique_word_count = counted_word.get(each_word, 0)  # Stolen from solution - was using count not get
        counted_word[each_word] = unique_word_count + 1

    print_spacing = max(len(each_word) for each_word in sentence_parts)  # Again shamelessly stolen, i had loop

    for unique_key in sorted(counted_word.keys()):
        print("{:{}} - {}".format(unique_key, print_spacing, counted_word[unique_key]))


main()
