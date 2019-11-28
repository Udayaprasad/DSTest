#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:42:52 2019

@author: Uday Vakalapudi
"""

from flask import Flask
import requests

app = Flask(__name__)


@app.route('/quotes/movie/<string:movieId>/character/<string:characterId>', methods=['GET'])
def quotes_by_movie_and_character(movieId, characterId):
    ''' This WebService is responsible for returning filtered quotes by movie and character fields
        @param movieId   - movie id
        @param characterId  - character id from the same movie id

        @return  return_response - Positive Response:- {
                                      "character_name": "<<CHARACTER_NAME>>"
                                      ,"movie_name" : "<<MOVIE_NAME>>"
                                      ,"quotes" : [
                                        "quote 1"
                                        ,"quote 2"
                                        ,"quote 3"
                                      ]
                                    }

                                   Negative Response:- {
                                   "request_type": "Bad Request",
                                   "response_codes":{"quotes_url":status_code,
                                                      "characters_url":status_code,
                                                      "movies_url":status_code}
                                   }
    '''

    # List of Endpoint URL used to format the desired output (character_name, movie_name, quotes)
    quotes_url = "https://the-one-api.herokuapp.com/v1/movie/{}/quote".format(
        movieId)
    characters_url = "https://the-one-api.herokuapp.com/v1/character/{}".format(
        characterId)
    movies_url = "https://the-one-api.herokuapp.com/v1/movie/{}".format(
        movieId)

    # Generate your own Authorization secret key and paste it in Authorization value
    common_header = {
        'Authorization': "Bearer ********",
    }

    # Get response objects for all Endpoint URLs
    quotes_response = requests.request(
        "GET", quotes_url, headers=common_header)
    characters_response = requests.request(
        "GET", characters_url, headers=common_header)
    movies_response = requests.request(
        "GET", movies_url, headers=common_header)

    # if the response status for all URLs are 200 then only send the desired output, else send the Bad Request a Response
    if(quotes_response.status_code == characters_response.status_code == movies_response.status_code == 200):
        return_response = {
            "character_name": characters_response.json()["name"].rstrip(),
            "movie_name": movies_response.json()["name"].rstrip(),
            "quotes": [item["dialog"].rstrip() for item in quotes_response.json()["docs"] if item["character"] == characterId]
        }
    else:
        return_response = {
            "request_type": "Bad Request",
            "response_codes": {"quotes_url": quotes_response.status_code,
                               "characters_url": characters_response.status_code,
                               "movies_url": movies_response.status_code}
        }

    return return_response


if __name__ == '__main__':
    app.run()
