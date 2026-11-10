import requests
from random import choice
def findTemperatureLive():  
  
    # Get the weather page
    weather = requests.get("https://www.boston.com/weather").text
    # The temperature can be found after the span class label
    # "local-weather__current-info-temp" and immediately before the
    # HTML code "<sup>&deg</sup>; (the superscript degree symbol)
    curLoc = weather.find("local-weather__current-info-temp")
    if curLoc != -1:
        # Now, find the degree symbol ("<sup>&deg;") following the temperature
        degLoc = weather.find("<sup>&deg", curLoc)
        # The temperature number is preceded by an HTML tag
        tempLoc = weather.rfind(">", 0, degLoc)
        # Temperature value is everything between the tag and the degree symbol
        return weather[tempLoc+1:degLoc]
    else:
        return 'Page has changed cannot find the temperature'
def sentence():
    """Generate a random sentence from a select set."""
    nouns = [
        "Mark",
        "Adam",
        "Angela",
        "Larry",
        "Jose",
        "Matt",
        "Jim"
        ]
    verbs = [
        "runs",
        "skips",
        "sings",
        "leaps",
        "jumps",
        "climbs",
        "fires a Civil War cannon",
        "swims",
        "argues",
        "giggles"
        ]
    phrases = [
        "in a tree",
        "through every room in the house",
        "very loudly",
        "around the bush",
        "while reading the newspaper",
        "very badly",
        "while skipping",
        "instead of grading",
        "while programming Python"
        ]
    return (choice(nouns) + " " + choice(verbs) + " " + choice(phrases)+".")
def createWebPage(fileName):
   
    file = open(fileName, "wt")
    file.write(createDocType())
    file.write(startHTML())
    file.write(createHead("Nuoheng"))
    file.write(startBody())
    file.write(createHeading("Nuoheng"))
    file.write(createParagraph("I am a computer science student from China.\n"))
    file.write(createImage("nuoheng.jpeg", "Picture of Nuoheng"))
    # REMAINDER OF PAGE OMITTED
    file.write(createParagraph("Today's Temperature is " + findTemperatureLive() + " degrees."))
    file.write(createParagraph(sentence()))
    file.write(endBody())
    file.write(endHTML())
    file.close()

def createDocType():
    return '<!DOCTYPE html>\n'

def startHTML():
    return '<html>\n\n'

def endHTML():
    return '</html>\n'

def createHead(title):
    return '<head>\n' + '<title>' + title +'</title>\n' + '</head>\n'

def createHeading(h1):
    return '<h1>' + h1 + '</h1>\n'

def createParagraph(p):
    return '<p>' + p + '</p>\n'


def startBody():
    return '<body>\n\n'
def endBody():
    return '</body>\n'

def createImage(imgfile, alttext):
    return f'<img src="{imgfile}" alt="{alttext}" />'


if __name__ == "__main__":
    createWebPage("l10.html")
