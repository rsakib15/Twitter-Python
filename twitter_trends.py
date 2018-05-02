import yweather
import operator
import csv

def get_trends(api):
    trend_dict = {}
    client = yweather.Client()
    results = api.trends_place(23424977)
    for location in results:
        for trend in location["trends"]:
            try:
                if trend["tweet_volume"] > 0:
                    trend['name'].decode('ISO-8859-1')
                    trend_dict[trend['name']] = trend['tweet_volume']
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

