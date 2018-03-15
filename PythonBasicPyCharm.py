import pandas as pd
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt;
import pylab;
from collections import Counter;
import datetime;
import string;
import urllib2;
import json;

df = pd.read_csv('C:/Users/hgsgautam/Desktop/Python/lending-club-loan-data/loan.csv');
df

from wordcloud import WordCloud
wordcloud = WordCloud(width = 2000, height = 1000).generate(' '.join(str(i) for i in df['title']))

plt.figure(figsize=(30,16))
plt.imshow(wordcloud)
