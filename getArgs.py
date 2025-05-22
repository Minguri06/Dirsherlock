#파이썬 인자값을 전달하는 모듈/sending python args

import argparse

parser = argparse.ArgumentParser(description='args')
parser.add_argument('-w',type=str,help='Enter the wordlist PATH')
parser.add_argument('-u',type=str,help='Enter the URL')
getpars = parser.parse_args()

url = getpars.u
wordlist = getpars.w

if __name__ == '__main__':
    print("Module is Working!")
