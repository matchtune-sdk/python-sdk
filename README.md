# MatchTune SDK for Python

This repository contains the open source MatchTune SDK that allows you to access the MatchTune API from your Python app.

## Installation

The MatchTune Python SDK can be installed with [Pip](https://pip.pypa.io/en/stable/installing/). Run this command:

```sh
pip install matchtune-sdk
```

## Usage

Simple MatchTune Query Example

```Python
import random

from matchtune_sdk import MatchTune

api = MatchTune({"app_token" : app_token})

haserror = True
## -- Load genre & subgenre list
genres = api.genres()
if genres != None:

  ## -- pick a random genre
  genre = random.sample(genres, 1)

  ## -- create a search query
  query = api.makeQuery(genre, title = None, tags = None)

  ## -- request a standard generated music
  idcard = api.generate(query)
  if idcard != None:
    haserror = False

    ## -- use the data
    printIDCard(idcard)
  }
}
```

## Api documentation

All mechanisms developed here are documented on our [REST API documentation](https://api-doc.matchtune.com/).

## License

Please see the [license file](https://github.com/matchtune-sdk/python-sdk/blob/master/LICENSE) for more information.

## Security Vulnerabilities

If you have found a security issue, please contact the support team directly at [support@matchtune.com](mailto:support@matchtune.com).
