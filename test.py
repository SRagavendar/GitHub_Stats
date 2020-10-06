from dotenv import load_dotenv
import os

load_dotenv()

waka_key = os.getenv('WAKA_API_KEY')
ghtoken = os.getenv('GH_TOKEN')

def printEnvironment():
	print(f'WakaTime API key = {waka_key}.')
	print(f'GH Token = {ghtoken}.')

if __name__ == '__main__':
	printEnvironment()