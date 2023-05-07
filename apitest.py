def leet():
    import requests
    import json

    def get_stats(username):
        url = "https://leetcode.com/graphql/"
        headers = {
            "referer": f"https://leetcode.com/{username}/",
            "Content-Type": "application/json"
        }
        query = """
            query getUserProfile($username: String!) {
                allQuestionsCount {
                    difficulty
                    count
                }
                matchedUser(username: $username) {
                    contributions {
                        points
                    }
                    profile {
                        reputation
                        ranking
                    }
                    submissionCalendar
                    submitStats {
                        acSubmissionNum {
                            difficulty
                            count
                            submissions
                        }
                        totalSubmissionNum {
                            difficulty
                            count
                            submissions
                        }
                    }
                }
            }
        """
        variables = {
            "username": username
        }
        data = {
            "query": query,
            "variables": variables
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_json = response.json()
        return response_json["data"]["matchedUser"]["submitStats"]["acSubmissionNum"][0]["count"]

    return get_stats("sds96")

def gfg():
    import requests
    from bs4 import BeautifulSoup
    url="https://auth.geeksforgeeks.org/user/shaurydeepsaxena"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all('span', {'class': 'score_card_value'})
    text = elements[1].text.strip()
    return text

def hrank():
    headers = {

        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'if-none-match': 'W/"f2b533d79ca695dc61fe8f94210d3f3c"',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-csrf-token': 'TCj3huLeF0Tpt8lR1jCFUkfuAt3rvgxWAkxkWeVnH2zlGFFSOhLr4gfMg8l6RCUfJQ+0Nd5xFQ2J/4IkSeT5/Q=='
    }
    import requests
    url = "https://www.hackerrank.com/rest/hackers/shaurydeepsaxena/badges"
    response = requests.get(url, headers=headers)
    res=response.json()
    return res['models'][0]['stars']

def codechef():
    import requests
    url = "https://www.codechef.com/users/sds96"
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find('div', {'class': 'rating-number'})
    return element.text.strip()