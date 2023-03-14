#this code won't die due to radiation posoning
import openai
import csv
from key import *
#I don't even bother with this
import logging
import threading
import time
import os
import os.path
#import moonlander from moonhole

#Flagged account ? api_key ?
#Flagged HWID ?
#Flagged ip ?

def main():
    openai.api_key = API_KEY
    model_engine = "text-davinci-003"
    #model_engine="curie"
    max_tokens = 1024
    while True:
        prompt = "Prompt: " + input("Enter your text: ")
        printtofile(prompt)
        completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.2,
        #top_p=0.5,
        #frequency_penalty=0,
        #presence_penalty=0
        )
        answer=completion.choices[0].text
        printtofile(answer)
        print(answer)

def printtofile(stuff):
    if os.path.exists("output.csv"):
        with open('output.csv', 'a') as f:
            # create the csv writer
            writer = csv.writer(f)
            # write a row to the csv file
            writer.writerow(stuff)
            #for item in stuff:
            #    writer.writerow([item])
            f.close()
    else :
        asd=open('output.csv', 'w')
        printtofile(stuff)
        asd.close()

main()