# Written by: Victor Ren
# This program performs sentiment analysis by prompting the user for a tweets file name and a keywords file name,
# and using the imported compute_tweets function to output the average happiness value, number of tweets with
# keywords, and number of tweets for each respective region.

from sentiment_analysis import compute_tweets

# Prompt user for file names
tweetsFile = input("Enter the name of the tweets file: ")
keywordsFile = input("Enter the name of the keywords file: ")

results = compute_tweets(tweetsFile, keywordsFile)

# Verifies that results from compute_tweets is not an empty list from invalid file names
if len(results) != 0:
    print()
    print("Eastern Time Zone:")
    print("Average happiness value:", results[0][0])
    print("Number of tweets with keywords:", results[0][1])
    print("Number of tweets in the region:", results[0][2])
    print()

    print("Central Time Zone:")
    print("Average happiness value:", results[1][0])
    print("Number of tweets with keywords:", results[1][1])
    print("Number of tweets in the region:", results[1][2])
    print()

    print("Mountain Time Zone:")
    print("Average happiness value:", results[2][0])
    print("Number of tweets with keywords:", results[2][1])
    print("Number of tweets in the region:", results[2][2])
    print()

    print("Pacific Time Zone:")
    print("Average happiness value:", results[3][0])
    print("Number of tweets with keywords:", results[3][1])
    print("Number of tweets in the region:", results[3][2])
else:  # Prints error message if results is empty list
    print()
    print("There are no results.", tweetsFile, "and/or", keywordsFile, "does not exist in this directory.")
