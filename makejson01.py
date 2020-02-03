#!/usr/bin/python3

import json

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, \
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    with open("galaxyguide.json", "w") as zfile:
        ## use the JSON library
        ## USAGE: json.dump(input data, file like object) ##
        json.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()
