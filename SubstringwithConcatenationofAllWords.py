class Solution(object):

    def __init__(self):
        pass

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if not s or len(words) == 0:
            return []

        strlen = len(s)
        wordlen = len(words[0])
        substrlen = len(words) * wordlen

        timedict = {}
        for word in words:
            if word in timedict:
                timedict[word] += 1
            else:
                timedict[word] = 1

        res = []
        for i in range(min(wordlen, strlen - substrlen + 1)):
            print i
            res += self._findSubstringfromi(i, s, strlen, wordlen, substrlen, timedict)

        return res

    def _findSubstringfromi(self, start, s, strlen, wordlen, substrlen, timedict):

        res = []

        currtimedict = {}
        wordstart = start

        while start + substrlen <= strlen:

            word = s[wordstart: wordstart + wordlen]
            wordstart += wordlen

            if word not in timedict:
                start = wordstart
                currtimedict = {}
            else:
                if word in currtimedict:
                    currtimedict[word] += 1
                else:
                    currtimedict[word] = 1
                while currtimedict[word] > timedict[word]:
                    currtimedict[s[start: start + wordlen]] -= 1
                    start += wordlen
                if start + substrlen == wordstart:
                    res.append(start)
                    # start = wordstart
                    # currtimedict = {}

        return res




if __name__ == '__main__':
    s = Solution()
    print s.findSubstring("barfoofoobarfooman", ["foo", "bar"])