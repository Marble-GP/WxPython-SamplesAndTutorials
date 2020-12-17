import json

with open("sampledata.json", "r") as jf:
    dat = json.load(jf)

print("{}(age:{}), his/her favorite is {}, his/her heigh is {}cm, his/her weight is {}kg.".format(dat["name"],dat["status"][2],dat["favorite"], dat["status"][0],dat["status"][1]))

input()
