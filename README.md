# Tweet Api

An API to extract data from twitter API and applying filters on provided data and to download the data in CSV format.

## Getting Started

### Prerequisites
Install these packages
* Dajngo==1.11.4
* djangorestframework==3.8.2
* djangorestframework-csv==2.1.0
* tweepy==3.6.0

You can install the individually by using ``` $ pip install PACKAGE-NAME``` or

You can install them at once by running the command
```
 $ pip install -r requirements.txt
```

### Setup

First make a virtaul environment by using the command
```
 $ virtualenv -p /usr/bin/python3 venv
```

Then start the virtual environment by 
```
 $ source venv/bin/activate
```

Install the dependencies given in prerequisites

Change directory to where ```manage.py``` is located
```
 $ cd twitterapi
```

Run the following commands to setup the database
```
 $ python manage.py makemigrations
 $ pyhton manage.py migrate
```

Enter your twitter API in twitterapi/settings.py
```
consumer_key="Your Consumer Key"
consumer_secret="Your Consumer Secreat"
key="Your Access Token"
secret="Your Access Secreat Token"
```
Run the deveploment server by
```
python manage.py runserver
```
This will start the development server at ```http://127.0.0.1:8000/```
## Usage
### Endpoints
##### API 1 to trigger a twitter search/stream for recent high traffic events. 

Endpoint for streaming data
```
http://127.0.0.1:8000/api/stream
```

##### API 2 to return stored tweets and their metadata based on applied filters/search. 

Endpint for getting data
```
http://127.0.0.1:8000/api/list
```

##### API 3 (For Bonus Points) ​to export filtered data as CSV 
 
Endpoint for getting data as a CSV file
```
http://127.0.0.1:8000/api/list/csv
```

### Pagination
The API is paginaed with page size equal to 20 to move to next page you can apply page filter
```
api/list?page=2
```

### Filtering
Your can filter the data your a receiving from this API by applying filters
Eg- ```/api/list?text__startswith=The%20person```

| Fields | Filters | Discription | Example |
| -------|---------|-------------|---------|
| text, user_name, user_screen_name | startswith | Filters the field on the basis if it start with the given value | ```http://127.0.0.1:8000/api/list?user_name__startswith=Rohan``` |
|  | endswith | Filters the field on the basis if it ends with the given value | ```http://127.0.0.1:8000/api/list?text__endswith=in%20india``` |
|  | contains | Filters the field on the basis if it contains the given value | ```http://127.0.0.1:8000/api/list?text__contains=python``` |
|  | exact | Filters the field on the basis if it is exactly the given value | ```http://127.0.0.1:8000/api/list?text__exact=abcd``` |
| favorite_count, user_followers_count, retweet_count | lt | Filters the field on the basis if it is less then the given number | ```http://127.0.0.1:8000/api/list?favorite_count__lt=30``` |
|  | gt | Filters the field on the basis if it is greater then the given number | ```http://127.0.0.1:8000/api/list?favorite_count__gt=30``` |
|  | exact | Filters the field on the basis if it is exatly the given number | ```http://127.0.0.1:8000/api/list?favorite_count__exact=30``` |
| tweet_time | before| Filters the field on the basis if it is before the given value | ```http://127.0.0.1:8000/api/list?tweet_time_before=2018-10-07%2014:00``` |
|  | after| Filters the field on the basis if it is after the given value | ```http://127.0.0.1:8000/api/list?tweet_time_after=2018-10-07%2014:00``` |

  - Multiple filters can be applied by chaining ```/api/list?page=2&text__startswith=python&user_name=Rohan```
  - Filter by a range of date can be done by ```api/list?tweet_time_before=2018-10-07%2014:00&/api/list?tweet_time_after=2018-10-05%2014:00```
  - Filtering can be applied for genrating csv file by changing the url like ```/api/list/csv?retweet_count__lt=10```


#### Field Refrences

| Field | Description |
|-------|-------------|
| text | Main tweet text |
| tweet_time | Time at which the tweet was posted |
| user_name | Name of the person who posted the tweet |
| favorite_count | Number of favorites/like on the tweet |
| retweet_count | Number of retweets |
| lang | Language in which tweet is posted |
| user_followers_count | Number of followers of the user |
| user_screen_name | Screen Name(username) of the user |

### Searching
Searching is done on the basis of ```user_name``` and ```text```
For searching just apply the filter ```/api/list?search=abcd```. This will search for abcd in both user_name and text and display the result

### Sorting
Sorting can be done on the basis of ```tweet_time``` and ```text```
For sorting just apply the filter ```/api/list?ordering=tweet_time```. This will sort data according to tweet_time
Use ```ordering=tweet_time``` for ascending and ```ordering=-tweet_time``` for descending, same for ```text```.

  - Searching and Sorting can be chained with filtering for combined result.
### Response
Here is a example of response for ```http://127.0.0.1:8000/api/list/```

```
{
    "count": 42,
    "next": "http://127.0.0.1:8000/api/list/?page=2",
    "previous": null,
    "results": [
        {
            "text": "RT @SirPunyaPrasun: मोदी सरकार ने साढ़े चार सालों में विज्ञापन पर ख़र्च किए 5,000 करोड़ रुपये https://t.co/cYxp8HAWLv #ModiGovernment #Adve…",
            "tweet_time": "2018-10-09T17:40:05.310000Z",
            "user_name": "The Viper",
            "favorite_count": 0,
            "retweet_count": 0,
            "lang": "hi",
            "user_followers_count": 33,
            "user_screen_name": "theviper753"
        },
        {
            "text": "@jnukaraja @gauravcsawant @ShivAroor @sanjayuvacha Every member of that so called freedom fighters wants to prove h… https://t.co/3MSSlf13Jg",
            "tweet_time": "2018-10-09T17:40:05.390000Z",
            "user_name": "MAHENDRA RATHORE",
            "favorite_count": 0,
            "retweet_count": 0,
            "lang": "en",
            "user_followers_count": 14,
            "user_screen_name": "singhbattleford"
        },
        ....
        ...
        ..
        .
}
```
  - Here count is the total number of results
  - next is the nest page in pagination
  - previous is the previous page in pagination 


