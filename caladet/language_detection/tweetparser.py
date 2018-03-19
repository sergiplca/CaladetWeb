# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
import re
import string

class Emoticons:

    EMOTICONS = ["*O", "*-*", "*O*", "*o*", "* *",
                 ":P", ":D", ":d", ":p",
                 ";P", ";D", ";d", ";p",
                 ":-)", ";-)", ":=)", ";=)",
                 ":<)", ":>)", ";>)", ";=)",
                 "=}", ":)", "(:;)",
                 "(;", ":}", "{:", ";}",
                 "{;:]",
                 "[;", ":')", ";')", ":-3",
                 "{;", ":]",
                 ";-3", ":-x", ";-x", ":-X",
                 ";-X", ":-}", ";-=}", ":-]",
                 ";-]", ":-.)",
                 "^_^", "^-^", ":(", ";(", ":'(",
                 "=(", "={", "):", ");",
                 ")':", ")';", ")=", "}=",
                 ";-{{", ";-{", ":-{{", ":-{",
                 ":-(", ";-(",
                 ":,)", ":'{",
                 "[:", ";]"
                 ]

class Ticks:

    TICKS = {
             u"á":u"&a;", u"é":u"&e;", u"í":u"&i;", u"ó":u"&o;", u"ú":u"&u;",
             u"Á":u"&A;", u"É":u"&E;", u"Í":u"&I;", u"Ó":u"&O;", u"Ú":u"&U;",
             u"à":u"&a;", u"è":u"&e;", u"ì":u"&i;", u"ò":u"&o;", u"ù":u"&u;",
             u"À":u"&A;", u"È":u"&E;", u"Ì":u"&I;", u"Ò":u"&O;", u"Ù":u"&U;",
             u"ñ":u"&n;", u"Ñ":u"&Ne;"
             }

class Tweet:

    @staticmethod
    def parsetweet(tweet, emojis):

        # Remove hashtags
        tweet = Tweet.__remove_hashtags(tweet)

        # Remove mentions
        tweet = Tweet.__remove_mentions(tweet)

        # Remove URLs
        tweet = Tweet.__remove_urls(tweet)

        # Remove emoticons
        tweet = Tweet.__remove_emoticons(tweet)

        # Remove RT if its a retweet
        tweet = Tweet.__remove_rt(tweet)

        # Parse to lower case
        tweet = tweet.lower()

        # Clear numbers
        tweet = ''.join(n for n in tweet if not n.isdigit())

        # Remove punctuation signs
        tweet = ''.join(l for l in tweet if (l not in string.punctuation or l == "'"))

        #Remove emojis
        tweet = Tweet.__remove_emojis(tweet, emojis)

        # Remove redundant spaces generated
        tweet = ' '.join(tweet.split())

        return tweet

    @staticmethod
    def __remove_hashtags(tweet):
        return re.sub(r"#\S+", "", tweet)

    @staticmethod
    def __remove_mentions(tweet):
        return re.sub(r"@\S+", "", tweet)

    @staticmethod
    def __remove_urls(tweet):
        return re.sub(r"http\S+", "", tweet)

    @staticmethod
    def __remove_emoticons(tweet):
        for emoticon in Emoticons.EMOTICONS:
            tweet = re.sub(".%s" % re.escape(emoticon), "", tweet)

        return tweet

    @staticmethod
    def __remove_emojis(tweet, emojis):
        for emoji in emojis.EMOJIS:
            tweet = re.sub(emoji, '', tweet)

        return tweet

    @staticmethod
    def __remove_ticks(tweet):
        for valueSearch, valueReplace in Ticks.TICKS.iteritems():
            tweet = tweet.replace(valueSearch, valueReplace)
        
        return tweet

    @staticmethod
    def __remove_rt(tweet):
        return re.sub("^RT", "", tweet)
