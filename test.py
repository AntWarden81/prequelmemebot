from markovGen import markovBot

# Instantiate the bot with the source files
bot = markovBot("./backstroke")

# out contains an array of sentences equal to the argument of generate_text
out = bot.generate_text(2)

for sentence in out:
    print(sentence)
