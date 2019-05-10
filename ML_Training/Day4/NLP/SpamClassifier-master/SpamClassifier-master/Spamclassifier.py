# importing the Dataset

import pandas as pd

messages = pd.read_csv(r'C:\PSTL\Purdue_PSTL\ML_Training\Day4\NLP\SpamClassifier-master\SpamClassifier-master\smsspamcollection\SMSSpamCollection', sep='\t',
                           names=["label", "message"])

#Data cleaning and preprocessing
import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wd=WordNetLemmatizer()

corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    review = review.lower()
    review = review.split()
    
    #review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    
    review = [wd.lemmatize(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    
    
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000)
X = cv.fit_transform(corpus).toarray()


# Creating  TF-IDF model 
from sklearn.feature_extraction.text import TfidfVectorizer
tf=TfidfVectorizer(max_features=5000)
X = tf.fit_transform(corpus).toarray()

# OneHotEncoding
y=pd.get_dummies(messages['label'])
y=y.iloc[:,1].values


# Train Test Split

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Training model using Naive bayes classifier
from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(X_train, y_train)

y_pred=spam_detect_model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
accuracy


# Training model using Decision Tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
dtree = DecisionTreeClassifier(criterion = 'entropy')
print(cross_val_score(dtree, X, y, cv=10, scoring ='accuracy').mean())


# for creating deployable artifacts
# way1
import pickle
name="NLP.pkl"
pckl=open(name,'wb')
pickle.dump(spam_detect_model,pckl)


# way2
from sklearn.externals import joblib
#Save the model as a pickele in a files
#knn is here model name
joblib.dump(spam_detect_model,'filename.pkl')



#Load the model from the pickle file
nlp_from=joblib.load('filename.pkl')
nlp_from.predict(X)



























