def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    digitletterdict = {"0": "0", "1": "1", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
     "9": "wxyz"}

    strlist = []

    for digit in digits:
        letters = digitletterdict[digit]

        newstrlist = []
        for letter in letters:
            if strlist:
                for str in strlist:
                    newstrlist.append(str+letter)
            else:
                newstrlist.append(letter)
        strlist = newstrlist

    return strlist


if __name__ == '__main__':
    print letterCombinations("")

