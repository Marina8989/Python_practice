def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than n, make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    n = n - 3

    if n > len(phrase):
        return phrase
    elif n < 3:
        return f'Truncation must be at least 3 characters.'
    else:
        x = phrase[0:n:] + '...'
        return x


print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
print(truncate("Yo", 100))
print(truncate('Cool', 1))