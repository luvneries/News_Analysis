import pandas as pd

#Read file
news = pd.read_csv("./news_data.csv")

# remove duplicate description columns
news = news.drop_duplicates('description')

# remove rows with empty descriptions
news = news[~news['description'].isnull()]

news['len'] = news['description'].map(len)

news = news[news.len > 140]

news.reset_index(inplace=True)

news.drop('index', inplace=True, axis=1)

#Tokenization using NLTK
import nltk
from nltk.tokenize import RegexTokenizer
#from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
#ps = PorterStemmer()
tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = nltk.WordNetLemmatizer()
def preprocessing(text):
    try:
        tokens = tokenizer.tokenize(str(text))
#        tokens = ps.stem(tokens)
#        tokens = list(filter(lambda t: t.lower() not in stop, tokens))
#        tokens = [ps.stem(word) for word in tokens if not word.lower() in set(stopwords.words('english'))]
        tokens = [lemmatizer.lemmatize(word) for word in tokens if not word.lower() in set(stopwords.words('english'))]
        tokens = list(filter(lambda x : re.search('[a-zA-Z]',x), tokens))
        return tokens
    except Exception as e:
        print(e)

data['tokens'] = data['description'].map(preprocessing)

for descripition, tokens in zip(data['description'].head(5), data['tokens'].head(5)):
    print('description:', descripition)
    print('tokens:', tokens)
    print()

def keywords(category):
    tmp_df = data.groupby('category').get_group(category)
#    tmp_df = l[ist(''.join(tmp_df.tokens))]
    tmp_df =  [word for sent in tmp_df.tokens for word in sent ]
    counter = Counter(tmp_df)
    return counter.most_common(10)

for category in set(data.category):
    print('category :', category)
    print('top 10 keywords:', keywords(category))
    print('---')
