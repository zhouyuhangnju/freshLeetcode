def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    anagrams_dict = {}
    for s in strs:
        key = str(sorted(s))
        if key in anagrams_dict:
            anagrams_dict[key].append(s)
        else:
            anagrams_dict[key] = [s]

    anagrams_list = []
    for key in anagrams_dict:
        anagrams_list.append(anagrams_dict[key])

    return anagrams_list


if __name__ == '__main__':
    print groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])