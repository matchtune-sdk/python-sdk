## Copyright 2019 Muzeek Inc.
##
## You are hereby granted a non-exclusive, worldwide, royalty-free license to
## use, copy, modify, and distribute this software in source code or binary
## form for use in connection with the web services and APIs provided by
## Muzeek.
##
## As with any software that integrates with the Muzeek platform, your use
## of this software is subject to the Muzeek terms of services and
## Policies [https://app.muzeek.co/terms-of-service]. This copyright notice
## shall be included in all copies or substantial portions of the software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
## THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.

import json
import time
import os

## format and print an id card
##
## @return null
##
def printIDCard(idcard):
  metadata     = idcard["metadata"];
  coverurl     = metadata["cover"]["medium"];
  musicurl     = idcard["urls"]["LOW"]; # Warning this url expires in 3 minutes
  prettyname   = ("%s %d (%s, %s)" % (metadata["title"], metadata["recordId"], metadata["genre"], metadata["subgenre"]));
  descriptor   = ("Duration:%ds, Tempo:%dBPM, Pitch:%s, Signature:%d/%d" % (round(metadata["duration"] / 1000), int(metadata["tempo"]), metadata["pitch"], int(metadata["numerator"]), int(metadata["denominator"])));

  print("Display name : " + prettyname);
  print("Description  : " + descriptor);
  print("Cover URL    : " + coverurl);
  print("Music URL    : " + musicurl);
  print()

  return None;

## save token to file (note this should be a database, this token should be encrypted)
##
## @return null
##
def savetoken(clientid, token):
  with open(".muzeektoken_" + clientid, 'w') as outfile:
    json.dump(token, outfile)

  return None;

## retreive token from file (note this should be a database
##
## @return token
##
def retreivetoken(clientid):
    if os.path.isfile(".muzeektoken_" + clientid):
        with open(".muzeektoken_" + clientid) as infile:
            token = json.load(infile)
        if float(time.time()) < float(token["expiration"]):
            return token;

    return None;
