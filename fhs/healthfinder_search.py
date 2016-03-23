import keys

import json
import urllib, urllib2
import string
HEALHFINDER_API = keys.HEALHFINDER_API

#http://healthfinder.gov/developer/
# Search.xml?api_key=demo_api_key&keyword=*&lang=es
#http://healthfinder.gov/developer/Search.xml?api_key=demo_api_key&keyword=%22type%202%20diabetes%22
def run_query(search_terms, age, gender):
    results = []
    keywords = "%22" + search_terms.replace(" ", "%20") + "%22"

    root_url = "http://healthfinder.gov/developer/Search.json?api_key="
    search_url = "{}{}&keyword={}&age={}&gender={}".format (
        root_url,
        HEALHFINDER_API,
        keywords,
        age,
        gender
    )

    try:
        response = urllib2.urlopen(search_url).read()
        json_response = json.loads(response)

        if json_response['Result'].has_key('Topics'):
            #the if/else statements are because when there is only one result per topics/tools
            #only a single dictionary is returned; while if there are more than one results per topics/tools
            #a list of results is returned
            if type(json_response['Result']['Topics']) == dict:

                topic=json_response['Result']['Topics']
                results.append({"title": topic["Title"], "url": topic["AccessibleVersion"], "source": "healthgov", "summary": "There is no description provided" })
            else:
                for topic in json_response['Result']['Topics']:
                    results.append({"title": topic["Title"], "url": topic["AccessibleVersion"], "source": "healthgov", "summary": "There is no description provided" })
            if type(json_response['Result']['Tools']) == dict:
                topic = json_response['Result']['Tools']
                results.append({"title": topic['Title'], "url": topic["AccessibleVersion"], "source": "healthgov", "summary": "There is no description provided" })
            else:
                for topic in json_response['Result']['Tools']:
                    results.append({"title": topic['Title'], "url": topic["AccessibleVersion"], "source": "healthgov", "summary": "There is no description provided" })


    except urllib2.URLError as e:
        print "Error when querying the healthfinder API: ", e

    return results


def main():
    # Query, get the results and create a variable to store rank.
    query = raw_input("Please enter a query: ")
    results = run_query(query)
    rank = 1
   # Loop through our results.
    for result in results:

       # Increment our rank counter by 1.
        rank += 1

if __name__ == '__main__':
    main()
