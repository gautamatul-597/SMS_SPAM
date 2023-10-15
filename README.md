# <-----------SMS_SPAM_Classifier----------->

I worked on project to build SMS SPAM CLASSIFIER
Here My goal was to develop a machine learning model that can accurately classify wheather a message is spam or not spam(ham) effectively.
I used well known UCI machine learning dataset (spam collection) 
which contains a labeled collection of sms message as spam or ham.
I selected a Multinomial Naive Bays algorithm because It is well suited for text classification tasks 
when we assume that the features are normaly distributed. 


There are Some Phases That I worked which are mentioned below.
1. DATA CLEANING.
     In the project first phase first load the dataset, I perfomed data cleaning to ensure dataset quality and reliability.
     handled missing values, remove duplicates, delete columns which was not necessary in prediction and achieved (ensured)
     data consistency.
   
2. EDA(EXPLORATORY DATA ANALYSIS).
     In this step, I know about what our dataset contains and how to relate each other.
     Analysing the data using some python libraries(pandas) method. like info(), shape[0] (0 for rows ,1 for columns)
     described(),profile_report(df). --> They are used for statistical summary.
     corr() to analysis correlation between columns
     For visualization we use matplotlib, seaborn (heatmap) etc.

     I use nltk library to check how many words , character,sentences a message contains, what is the average length of message ,
     In mycase generally spam have more words or sentences than  ham messages.
   
3. TEXT PREPROCESSING.
     There are some steps which I perfomed.
     Lower Case.
         Convirt all message into lower case character
     Tokenization.
         Convirt all message into tokens or in form of words ['hi', 'how', 'are', 'you'].
     Remove special characters.
         Remove some special character which are not neccessary in model building like %,$,#,@,& ect.
     Remove stop words and punctuation.
         I remove stop words( he ,she ,it , you, can, etc) and punctuation ( !,?,.,^, etc)
         because there no special meaning to form a sentence they are just used to decorate the sentence
         I use nltk.corpus to import stop words and string for punctuation.
     Stemming.
         In last step we performed stemming. It is process of convirting words into a root form.
         example.   dancing-->dance, loving--> love, reading-->read.
4.  MODEL BUILDING.
     Here , first we convirt text message into numerical form(vector) on the basis of frequencies of each word
     That occured the entire text. For this convirsion I use Countvectorizer,TF-IDF(Term frequency-Inverse document frequency).
     After that I split the dataset into training and testing set. I use 20% to test data(unseen),80% for training data of
     the whole data, used random state .2.
     The model was trained on Naive Bays theorem, Gaussian naive, Multinomial naive, Bernouli naive.
     also perfomed some machine learning learning algorithm like bagging(Random Forest classifier), boosting ,Voting(combination of different algorithm),stacking etc.
     Multinomial naive_bays gives the best result.
5. EVALUATION.
     The evaluationg model concerning with accuracy 97.8% and precesion 100%.
6. WEBSITE.
     As a user freindly solution , I developed a website using streamlit python library where use can interact
     with  SMS SPAM CLASSIFIER . This website allows user to give input a text messages and receive instant predictions
     enhancing its practical ability.
     
     
     
