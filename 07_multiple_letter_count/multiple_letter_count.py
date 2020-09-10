def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    dict = {}

    for n in phrase:
       key = dict.keys()
       if n in key:
           dict[n] += 1
       else:
           dict[n] = 1
    return dict

    # counter = {}
    #
    # for ltr in phrase:
    #     counter[ltr] = counter.get(ltr, 0) + 1
    #
    # return counter


print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))