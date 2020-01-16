import browserhistory as bh
import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud,STOPWORDS

#print(bh.get_browserhistory())
#bh.write_browserhistory_csv()


history = pd.read_csv("firefox_history.csv")
history = history[~history["browserhistory · PyPI"].str.contains("New Tab", na=False)]

plt.figure(figsize=(15,10))
history = history.dropna()

history.isna().sum()

text = "".join(hist for hist in history["browserhistory · PyPI"])
print(len(text))

#remove the words which you think are not relevant
stopwords = ["Google", "YouTube","Graphic","Hill University","Hill","University"]

STOPWORDS.update(stopwords)

wordcloud = WordCloud(stopwords=STOPWORDS,background_color="white").generate(text)
wordcloud.to_file("third.png")


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
