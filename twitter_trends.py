
import operator
import csv

def get_trends(api):
    trend_dict = {}
    woeid = {
        "AUSTRALIA" : 23424748,
        "AUSTRIA" : 23424750,
        "BELGIUM" : 23424757,
        "CANADA" : 23424775,
        "CHILE" : 23424782,
        "COLOMBIA" : 23424787,
        "DENMARK" : 23424796,
        "EGYPT" : 23424802,
        "FRANCE" : 23424819,
        "GERMANY" : 23424829,
        "INDIA" : 23424848,
        "IRELAND" : 23424803,
        "ITALY" : 23424853,
        "MEXICO" : 23424900,
        "NETHERLANDS" : 23424909,
        "NORWAY" : 23424910,
        "SOUDI" : 23424938,
        "SINGAPORE" : 23424948,
        "RSA" : 23424942,
        "SWEDEN" : 23424954,
        "SWITZERLAND" : 23424957,
        "THAILAND" : 23424960,
        "USA" : 23424977
    }

    for key, value in woeid.iteritems():
        print value
        results = api.trends_place(value)
        for location in results:
            for trend in location["trends"]:
                try:
                    if trend["tweet_volume"] > 0:
                        trend['name'].decode('ISO-8859-1')
                        trend_dict[trend['name']] = trend['tweet_volume']  # keep the value in key value pair
                except:
                    continue

    rev_sorted_trend = sorted(trend_dict.items(), key=operator.itemgetter(1), reverse=True)
    return rev_sorted_trend


def put_trend_csv(trend):
    trendlistexport = [["Trending Topic", "Tweet Volume"]]  # Makes trendlist to write into csv

    for item in trend:
        trendelement = []
        trendelement.append(item[0])
        trendelement.append(item[1])
        print(trendelement)
        trendlistexport.append(trendelement)
        with open('trendtweets.csv', 'w') as trendfile:  # puts trend list items in CSV
            writeto = csv.writer(trendfile, delimiter=',')
            writeto.writerows(trendlistexport)

