## Copyright 2021 MatchTune Inc.
##
## You are hereby granted a non-exclusive, worldwide, royalty-free license to
## use, copy, modify, and distribute this software in source code or binary
## form for use in connection with the web services and APIs provided by
## MatchTune.
##
## As with any software that integrates with the MatchTune platform, your use
## of this software is subject to the MatchTune terms of services and
## Policies [https://www.matchtune.com/privacy-policy]. This copyright notice
## shall be included in all copies or substantial portions of the software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
## THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.

from helpers        import *
from credentials    import *
from matchtune_sdk  import MatchTune

import random

client_id = MATCHTUNE_CLIENT_ID
app_token = retreivetoken(client_id)
api = MatchTune({  "app_token"   : app_token,
                   "app_id"      : MATCHTUNE_APP_ID,
                   "app_secret"  : MATCHTUNE_APP_SECRET})
version = api.apiVersion()
print("API Version : " + version)

haserror = True
## -- login if needed
if app_token != None or api.apiLogin(client_id, MATCHTUNE_TOS):

  ## -- save the token
  savetoken(client_id, api.getCurrentToken())

  ## -- get all genre & subgenre
  genres = api.genres()
  if genres != None:

    ## -- pick a random genre
    genre = random.sample(genres, 1)

    ## -- create a search query
    query = api.makeQuery(genre, title = None, tags = None)

    ## -- request a standard generated music
    idcard = api.generate(query)
    if idcard != None:
        print("Original :")
        printIDCard(idcard)

        ## -- request a climax @ 10s with riser and drop if available
        features = [api.makeClimaxFeature(10000, True, True)]

        ## -- request a modification on the music
        print("Modified :")
        idcard = api.modify(idcard["finalHash"], 30000, features)
        if idcard != None:
            haserror = False

            ## -- use the data
            printIDCard(idcard)

if haserror:
    print("Error :")
    print(api.getLastError())
