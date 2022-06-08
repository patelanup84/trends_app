import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.set_page_config(
layout='wide')

st.title("Topic Finder")

pytrend_word = st.sidebar.text_input("Google Trend Search Term",google_topic)
redtrend_word = st.sidebar.text_input("Reddit Trend Search Term",reddit_topic)
twtrend_word = st.sidebar.text_input("Twitter Trend Search Term",twitter_topic)
nwtrend_word = st.sidebar.text_input("News Search Term",news_topic)


if st.button('Click Here To Get Hot Topics For Search Term'):
    with st.spinner('Wait for it...'):        #to display progressing message
        time.sleep(5)

    data = gtrends(pytrend_word)
    gtrends_list = list(data['query'][0:10])  # gtrends Top 10
    redtrends(redtrend_word) #returns reddit trend search
    twtrends(twtrend_word) #twitter top list
    tweets_df = pd.DataFrame(list(zip(tweet_text, score)), columns=['Tweets', 'Score'])
    tweets_df = tweets_df.sort_values(by=['Score'], ascending=False)
    tweets_list = list(tweets_df['Tweets'].head(10))
    newtrends(nwtrend_word)
    st.success('Done!')
    st.balloons()

    df1 = pd.DataFrame(data=gtrends_list,columns=['Trending in Google'])



    df2 = pd.DataFrame(reddit_list,columns=['Trending in Reddit'])
    df3 = pd.DataFrame(tweets_list,columns=['Trending in Twitter'])
    df4 = pd.DataFrame(news_list,columns=['Trending in News'])
    df1=df1.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    df2=df2.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    df3=df3.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    df4=df4.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    st.title("Content Idea Search")
    col1,col2,col3,col4 = st.beta_columns(4)

    col1.table(df1)
    col2.table(df2)
    col3.table(df3)
    col4.table(df4)

    wc = gtrends_list + reddit_list + news_list + tweets_list


    from wordcloud import WordCloud, STOPWORDS
    import matplotlib.pyplot as plt
    comment_words = ''
    stopwords = set(STOPWORDS)

    for val in wc:

        # typecaste each val to string
        val = str(val)

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens) + " "

    # Create some sample text
    #text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

    # Create and generate a word cloud image:
    wordcloud = WordCloud().generate(comment_words)
    fig, ax = plt.subplots()
    # Display the generated image:
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    #ax.show()
    st.pyplot(fig)





