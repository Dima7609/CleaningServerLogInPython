import os
import re
import datetime
from datetime import timezone
import math

def needsortdata():
    itert = 'D:/'
    listdata = ['24','25','26','27','28','29','30']
    file = open("selectdata.txt", "w")
    te = open(os.path.join(itert, "wm2020projekt.log"), "r")
    for et in te:
        dtime = re.search(r'\d\d/\w\w\w/\d\d\d\d\S\d\d\S\d\d\S\d\d', et)
        mydate = re.search(r'^(\d\d)', dtime.group(0))
        mymonth = re.search(r'\d\d/(\w\w\w)', dtime.group(0))
        myyear = re.search(r'(\d\d\d\d)', dtime.group(0))
        if (str(mydate.group(0)) in listdata):
            if (mymonth.group(1) == 'Dec'):
                if(str(myyear.group(0)) == '2017'):
                    file.write(et)
    file.close()

def prvauloha():
    ipadress = []
    cisteniedat = open("prvauloha.txt", "w")
    filerobots = open("robotstxt.txt", "w")
    filerobotsuseragent = open("robotuseragent.txt", "w")
    with open('selectdata.txt', 'r') as f:
        data = f.readlines()
        for t in data:
            find_ip = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', t)
            find_dtime = re.search(r'\d\d/\w\w\w/\d\d\d\d\S\d\d\S\d\d\S\d\d', t)
            find_statuscode = re.search(r'(\s+((2|3)\d\d)\s)', t)
            find_bytes = re.search(r'(\s+((2|3)\d\d)\s)+([0-9]+)', t)
            find_agent = re.search(r'\"\s\"(.*?)\"', t)
            find_urls = re.search(r'\"(\w\w\w\s([^\]]+?))\"', t)
            find_referrer = re.search(r'(\s+((2|3)\d\d)\s)+([0-9]+)\s(\"([^\]]+?)\")', t)
            if (t.find('.bmp') != -1):
                print("This line is not added")
            elif (t.find('.jpg') != -1):
                print("This line is not added")
            elif (t.find('.jpeg') != -1):
                print("This line is not added")
            elif (t.find('.png') != -1):
                print("This line is not added")
            elif (t.find('.gif') != -1):
                print("This line is not added")
            elif (t.find('.JPG') != -1):
                print("This line is not added")
            elif (t.find('.css') != -1):
                print("This line is not added")
            elif (t.find('.flv') != -1):
                print("This line is not added")
            elif (t.find('.ico') != -1):
                print("This line is not added")
            elif (t.find('.swf') != -1):
                print("This line is not added")
            elif (t.find('.rss') != -1):
                print("This line is not added")
            elif (t.find('.xml') != -1):
                print("This line is not added")
            elif (t.find('.cur') != -1):
                print("This line is not added")
            elif (t.find('.js') != -1):
                print("This line is not added")
            elif (t.find('.json') != -1):
                print("This line is not added")
            elif (t.find('.svg') != -1):
                print("This line is not added")
            elif (t.find('.woff') != -1):
                print("This line is not added")
            elif (t.find('.eot') != -1):
                print("This line is not added")
            elif (re.findall(r'\"\s((1|4|5)\d\d)\s', t)):
                print("This line is not added")
            elif (t.find('POST') != -1):
                print("This line is not added")
            elif (t.find('HEAD') != -1):
                print("This line is not added")
            elif (t.find('.otf') != -1):
                print("This line is not added")
            elif (t.find('.ttf') != -1):
                print("This line is not added")
            elif (t.find('format=json') != -1):
                print("This line is not added")
            elif (t.find('OPTIONS') != -1):
                print("This line is not added")
            elif (t.find('robots.txt') != -1):
                filerobots.write(t)
            elif (re.findall(r'[c,C]rawl', find_agent.group(1))):
                filerobotsuseragent.write(t)
            elif (re.findall(r'[s,S]pider', find_agent.group(1))):
                filerobotsuseragent.write(t)
            elif (re.findall(r'[b,B]ot', find_agent.group(1))):
                filerobotsuseragent.write(t)
            else:
                find_date = re.search(r'^(\d\d)', find_dtime.group(0))
                find_year = re.search(r'(\d\d\d\d)', find_dtime.group(0))
                find_hour = re.search(r':(\d\d):', find_dtime.group(0))
                find_minute = re.search(r':\d\d:(\d\d):\d\d', find_dtime.group(0))
                find_second = re.search(r'(\d\d)$', find_dtime.group(0))
                get_unixtime = datetime.datetime(int(find_year.group(0)), 12, int(find_date.group(0)), int(find_hour.group(1)), int(find_minute.group(1)), int(find_second.group(0)))
                get_timestamp = get_unixtime.replace(tzinfo=timezone.utc).timestamp()
                cisteniedat.write(find_ip.group(1))
                cisteniedat.write(" ")
                if find_ip.group(1) not in ipadress:
                    ipadress.append(find_ip.group(1))
                    cisteniedat.write(str(ipadress.index(find_ip.group(1))))
                else:
                    cisteniedat.write(str(ipadress.index(find_ip.group(0))))
                cisteniedat.write(" ")
                cisteniedat.write(str(get_timestamp))
                cisteniedat.write(" ")
                cisteniedat.write(find_dtime.group(0))
                cisteniedat.write(" ")
                cisteniedat.write(find_urls.group(1))
                cisteniedat.write(" ")
                cisteniedat.write(find_statuscode.group(2))
                cisteniedat.write(" ")
                cisteniedat.write(find_bytes.group(4))
                cisteniedat.write(" ")
                cisteniedat.write(find_referrer.group(6))
                cisteniedat.write(" ")
                cisteniedat.write(find_agent.group(1))
                cisteniedat.write("\n")
    cisteniedat.close()
    filerobots.close()
    filerobotsuseragent.close()

def getuniqueip():
    seen = set()
    with open('prvauloha.txt') as infile:
        with open('uniqueip.txt', 'w') as outfile:
            for line in infile:
                ip = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
                if ip.group(0) not in seen:
                    outfile.write(ip.group(0))
                    outfile.write("\n")
                    seen.add(ip.group(0))

def sortstringbyip():
    with open("uniqueip.txt", "r") as fp:
        ips = list(map(str.rstrip, fp))  # Read all addresses from a file
    with open("prvauloha.txt", "r") as fp:
        records = list(map(str.rstrip, fp))  # We read all the lines from the file
    records.sort(key=lambda x: ips.index(x.split()[0]))  # Sort the strings by address in the address list
    with open("sortedrecords.txt", "w") as fp:
        fp.write("\n".join(records))  # Writing sorted records to a new file

arr = []
arrtwo = []
def findlength():
    sortstring = open("sortedrecords.txt", "r")
    list = sortstring.readlines()
    for i in range(len(list)):
        try:
            ippairline = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', list[i])
            ipunpairedline = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', list[i + 1])
            firstseen = re.search(r'(\d{10}).\d\s\d\d/\w\w\w/\d\d\d\d\S\d\d\S\d\d\S\d\d', list[i])
            secondseen = re.search(r'(\d{10}).\d\s\d\d/\w\w\w/\d\d\d\d\S\d\d\S\d\d\S\d\d', list[i + 1])
            if (ippairline.group(1) == ipunpairedline.group(1)):
                duration = int(secondseen.group(1)) - int(firstseen.group(1))
                gethour = datetime.timedelta(seconds=duration)
                if (gethour.seconds < 3600 and duration > -1):
                    arrtwo.append(gethour.seconds)
                else:
                    arrtwo.append(-1)
            else:
                arrtwo.append(-1)
        except IndexError:
            arrtwo.append(-1)
    addlengthtostring = open("sortedrecords.txt", "w")
    for value in range(len(arrtwo)):
        addlengthtostring.write(str(arrtwo[value]) + " " + list[value])
        if(arrtwo[value] != -1):
            arr.append(arrtwo[value])
    sortstring.close()
    addlengthtostring.close()

def findrlength():
    countidentifsed = 0
    length = round(sum(arr) / len(arr))
    rlength = round((-math.log(0.6))/(1.0/length))
    print("Average length: " + str(length))
    print("Reference Length: " + str(rlength))
    lengthstring = open("sortedrecords.txt", "r")
    length_read = lengthstring.readlines()
    writesedenie = open("sortedrecords.txt", "w")
    for i in range(len(length_read)):
        try:
            useridpair = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s(\d{1,4})', length_read[i])
            useridipunpaired = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s(\d{1,4})', length_read[i + 1])
            newuserid = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s(\d{1,4})', length_read[i - 1])
            if(useridipunpaired.group(2) == useridpair.group(2)):
                if(arrtwo[i] <= rlength):
                    writesedenie.write(str(countidentifsed) + " " + length_read[i])
                else:
                    countidentifsed += 1
                    writesedenie.write(str(countidentifsed) + " " + length_read[i])
            else:
                writesedenie.write(str(countidentifsed) + " " + length_read[i])
                countidentifsed += 1
        except IndexError:
            if(useridpair.group(2) == newuserid.group(2)):
                if(arrtwo[i] <= rlength):
                    writesedenie.write(str(countidentifsed) + " " + length_read[i])
                else:
                    writesedenie.write(str(countidentifsed + 1) + " " + length_read[i])
            else:
                writesedenie.write(str(countidentifsed + 1) + " " + length_read[i])
    writesedenie.close()
    lengthstring.close()

def dopciest():
    writedopciest = open("dopciest.txt", "w")
    rlengthstring = open("sortedrecords.txt", "r")
    rlength_read = rlengthstring.readlines()
    testarray = []
    lsturl = []
    for i in range(len(rlength_read)):
        try:
            sedenieid = re.search(r'(^\d+)\s', rlength_read[i])
            sedenieidnext = re.search(r'(^\d+)\s', rlength_read[i + 1])
            geturl = re.search(r'\d\d/\w\w\w/\d\d\d\d\S\d\d\S\d\d\S\d\d\s\w\w\w\s(\/(.*?)\s)', rlength_read[i])
            geturl_value = geturl.group(2)
            sedenieidprev = re.search(r'(^\d+)\s', rlength_read[i - 1])
            if(sedenieid.group(1) == sedenieidnext.group(1)):
                testarray.append(rlength_read[i])
                if not geturl_value:
                    geturl_value = "testword_to_add"
                    lsturl.append(geturl_value.split())
                else:
                    lsturl.append(geturl_value.replace('/', ' ').split())
            else:
                if(sedenieid.group(1) == sedenieidprev.group(1)):
                    testarray.append(rlength_read[i])
                    if not geturl_value:
                        geturl_value = "testword_to_add"
                        lsturl.append(geturl_value.split())
                    else:
                        lsturl.append(geturl_value.replace('/', ' ').split())
                    if(sedenieid.group(1) != sedenieidnext.group(1)):
                        if len(lsturl) == 0:
                            print("there will be nothing")
                        else:
                            for j in range(len(lsturl)):
                                word = lsturl[j][0]
                                for t in range(len(lsturl)):
                                    if lsturl[t][0] == "testword":
                                        print("here we do nothing")
                                    else:
                                        if word in lsturl[t][0]:
                                            writedopciest.write(testarray[t])
                                            lsturl[t][0] = "testword"
                            lsturl.clear()
                            testarray.clear()
                else:
                    writedopciest.write(rlength_read[i])
        except IndexError:
            print("IndexError")
    writedopciest.close()
    rlengthstring.close()

#needsortdata()
prvauloha()
getuniqueip()
sortstringbyip()
findlength()
findrlength()
dopciest()