import fileinput
import requests

def main():
  for line in fileinput.input():
    query = line.rstrip()
    url = 'http://127.0.0.1:8080/query'
    myobj = {'query': query}
    x = requests.post(url, json = myobj)

if __name__ == "__main__":
    main()
