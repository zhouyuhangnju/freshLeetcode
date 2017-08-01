def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    digitletterdict = {"0": "0", "1": "1", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
     "9": "wxyz"}

    # strlist = []
    #
    # for digit in digits:
    #     letters = digitletterdict[digit]
    #
    #     newstrlist = []
    #     for letter in letters:
    #         if strlist:
    #             for str in strlist:
    #                 newstrlist.append(str+letter)
    #         else:
    #             newstrlist.append(letter)
    #     strlist = newstrlist
    #
    # return strlist

    def subLetterCombinations(currdigits):
        if len(currdigits) == 0:
            return ['']
        return [letters + poststr for letters in digitletterdict[currdigits[0]] for poststr in
                subLetterCombinations(currdigits[1:])]

    if len(digits) == 0:
        return []
    return subLetterCombinations(digits)


if __name__ == '__main__':
    print len(letterCombinations("234"))

