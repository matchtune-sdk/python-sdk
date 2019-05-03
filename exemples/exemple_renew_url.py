## Copyright 2019 Muzeek Inc.
##
## You are hereby granted a non-exclusive, worldwide, royalty-free license to
## use, copy, modify, and distribute this software in source code or binary
## form for use in connection with the web services and APIs provided by
## Muzeek.
##
## As with any software that integrates with the Muzeek platform, your use
## of this software is subject to the Muzeek terms of services and
## Policies [https:##app.muzeek.co/terms-of-service]. This copyright notice
## shall be included in all copies or substantial portions of the software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
## THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.

from helpers     import *
from credentials import *
from muzeek_sdk  import Muzeek

import random

client_id = MUZEEK_CLIENT_ID
app_token = retreivetoken(client_id)
api = Muzeek({  "app_token"   : app_token,
                "app_id"      : MUZEEK_APP_ID,
                "app_secret"  : MUZEEK_APP_SECRET})
version = api.apiVersion()
print("API Version : " + version)

haserror = True
## -- login if needed
if app_token != None or api.apiLogin(client_id, MUZEEK_TOS):

    ## -- save the token
    savetoken(client_id, api.getCurrentToken())

    ## -- get all genre & subgenre
    genres = api.genres()
    if genres != None:

        ## -- pick a random genre
        genre = random.sample(genres.keys(), 1)

        ## -- create a search query
        query = api.makeQuery(genre, subgenre = None, title = None, tags = None)

        ## -- request a standard generated music
        idcard = api.generate(query)
        if idcard != None:
            printIDCard(idcard)
        ## -- if you already have a license for this title, you may don't have to request a new one
        ## -- please check the terms of the license  (https:##app.muzeek.co/#/conditions-premium)
        ## -- Get a license on the title (mandatory to get unwatermarked files and full quality
        license = None
        if idcard["license"] == "None":
            license = api.license(idcard["finalHash"])

        if idcard["license"] != "None" or (license != None and license["status"] == "approved"):
            ## -- Get a new URL only available once the song licensed
            url = api.getMusicURL(idcard["finalHash"], "HIGH")
            if url != None:
                haserror = False

                ## -- use the data
                printIDCard(idcard)

                ## -- use the data
                print("Fresh url :")
                print(url)
                print()

if haserror:
    print("Error : ")
    print(api.getLastError())
