# This module consists of the compute_tweets function.
# The function takes two parameters, processes the tweets, and then outputs the results.

import string

def compute_tweets(tweetsFile, keywordsFile):
    try:
        # Opens keywords file, avoid encoding errors
        infile = open(keywordsFile, "r", encoding="utf-8")

        keywordsList = []
        valuesList = []

        # Processes keywords file, splitting the happiness values from the keywords,
        # appending them into their respective lists
        for line in infile:
            keywordsLine = line.rstrip().split(",")
            keywordsList.append(keywordsLine[0])
            valuesList.append(keywordsLine[1])

        infile.close()
    except IOError:
        return[]  # Returns empty list if file is not found
        quit()

    try:
        # Opens tweets file, avoiding encoding errors
        infile = open(tweetsFile, "r", encoding="utf-8")

        # Initialize variables
        easternTweetCount = 0
        centralTweetCount = 0
        mountainTweetCount = 0
        pacificTweetCount = 0

        easternKeywordTweetCount = 0
        centralKeywordTweetCount = 0
        mountainKeywordTweetCount = 0
        pacificKeywordTweetCount = 0

        easternScore = 0
        centralScore = 0
        mountainScore = 0
        pacificScore = 0

        # Initialize results list, which tuples of values will be placed into
        results = []

        # Processes tweet line, extracting latitude and longitude values as well as the text
        for line in infile:
            tweetLine = line.lower().rstrip().split()
            latitude = float(tweetLine[0].rstrip(",").lstrip("["))
            longitude = float(tweetLine[1].rstrip("]"))
            keywordFound = False  # Set boolean variable to avoid counting lines with two keywords as two tweets
            wordCount = 0
            scoreCount = 0

            # Determine which region the tweet is from, removes punctuation, sets counters and scores.
            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -67.4446574 and longitude >= -87.518395):
                easternTweetCount += 1
                for word in tweetLine:
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    if word in keywordsList:
                        if not keywordFound:
                            easternKeywordTweetCount += 1
                            keywordFound = True
                        wordCount += 1
                        keywordScorePosition = keywordsList.index(word)
                        scoreCount += float(valuesList[keywordScorePosition])
                if scoreCount > 0 and wordCount > 0:
                    easternScore += (scoreCount/wordCount)

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -87.518395 and longitude >= -101.998892):
                centralTweetCount += 1
                for word in tweetLine:
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    if word in keywordsList:
                        if not keywordFound:
                            centralKeywordTweetCount += 1
                            keywordFound = True
                        wordCount +=1
                        keywordScorePosition = keywordsList.index(word)
                        scoreCount += float(valuesList[keywordScorePosition])
                if scoreCount > 0 and wordCount > 0:
                    centralScore += (scoreCount/wordCount)

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -101.998892 and longitude >= -115.236428):
                mountainTweetCount += 1
                for word in tweetLine:
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    if word in keywordsList:
                        if not keywordFound:
                            mountainKeywordTweetCount += 1
                            keywordFound = True
                        wordCount +=1
                        keywordScorePosition = keywordsList.index(word)
                        scoreCount += float(valuesList[keywordScorePosition])
                if scoreCount > 0 and wordCount > 0:
                    mountainScore += (scoreCount/wordCount)

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -115.236428 and longitude >= -125.242264):
                pacificTweetCount += 1
                for word in tweetLine:
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    if word in keywordsList:
                        if not keywordFound:
                            pacificKeywordTweetCount += 1
                            keywordFound = True
                        wordCount +=1
                        keywordScorePosition = keywordsList.index(word)
                        scoreCount += float(valuesList[keywordScorePosition])
                if scoreCount > 0 and wordCount > 0:
                    pacificScore += (scoreCount/wordCount)

        # Compute average happiness scores for each region, avoiding division by zero
        if easternKeywordTweetCount != 0:
            easternAverage = easternScore / easternKeywordTweetCount
        else:
            easternAverage = 0

        if centralKeywordTweetCount != 0:
            centralAverage = centralScore / centralKeywordTweetCount
        else:
            centralAverage = 0

        if mountainKeywordTweetCount != 0:
            mountainAverage = mountainScore / mountainKeywordTweetCount
        else:
            mountainAverage = 0

        if pacificKeywordTweetCount != 0:
            pacificAverage = pacificScore / pacificKeywordTweetCount
        else:
            pacificAverage = 0

        # Appends tuples of values to results list
        results.append((easternAverage, easternKeywordTweetCount, easternTweetCount))
        results.append((centralAverage, centralKeywordTweetCount, centralTweetCount))
        results.append((mountainAverage, mountainKeywordTweetCount, mountainTweetCount))
        results.append((pacificAverage, pacificKeywordTweetCount, pacificTweetCount))

        return results

        infile.close()
    except IOError:
        return[]
        quit()
