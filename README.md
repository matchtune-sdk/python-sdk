# Muzeek SDK for Python

This repository contains the open source Muzeek SDK that allows you to access the Muzeek API from your Python app.

## Installation

The Muzeek Python SDK can be installed with [Pip](https://pip.pypa.io/en/stable/installing/). Run this command:

```sh
pip install muzeek-sdk
```

## Usage

Simple Muzeek Query Example

```Python
import random

from muzeek_sdk import Muzeek

api = Muzeek({"app_token" : app_token})

haserror = True
## -- Load genre & subgenre list
genres = api.genres()
if genres != None:

  ## -- pick a random genre
  genre = random.sample(genres.keys(), 1)

  ## -- create a search query
  query = api.makeQuery(genre, subgenre = None, title = None, tags = None)

  ## -- request a standard generated music
  idcard = api.generate(query)
  if idcard != None:
    haserror = False

    ## -- use the data
    printIDCard(idcard)
  }
}
```

## License

Please see the [license file](https://github.com/muzeek/python-sdk/blob/master/LICENSE) for more information.

## Security Vulnerabilities

If you have found a security issue, please contact the support team directly at [support@muzeek.co](mailto:support@muzeek.co).
