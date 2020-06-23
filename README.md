# YoutubeTranscriptionMVC
A coding assignment to transcribe youtube videos using the MVC design pattern. This is a LOT. Remember what I told you this week, try to understand the general philosophy and motivation behind this and don't concern yourself too much with the less important aspects such as coding. It's perfectly okay for the code to not work, that's not the point of this assignment.

## Introduction
Remember that one of the topics we discussed this week was the MVC (model view controller) design pattern. This is a relatively simple but extremely powerful design pattern used broadly through industry.

You can read more about the MVC pattern [here](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html) to refresh your memory. This is a very simple approach to MVC, it can actually get quite a bit more complex and there are many different ways to approach implementation of MVC (if you're interested in learning more about what this means ask me in our next lesson!). I was surprised to see a number of other reputable websites discussing MVC pretty badly, Apple does a good job of explaining it here correctly. In any case, I would be wary of what you read on the internet regarding MVC design pattern, it seems some people on the internet do not really understand what MVC is on a foundational level.

MVC is born out of a philosophy of purity, of building a system that is inherently flexible, maintanable, defensive, modular, coordinated, among other things. This is a rapidly growing idea in the field of Computer Science and software, we touched very briefly on functional programming once and it's a great example of this philosophy. Functional programming is a programming paradigm centered on that idea of purity, it's a programming style that in simple terms leads to less bugs and is theoretically very clean.

In any case let's get to the project at hand. You'll be fleshing out a program that transcribes youtube videos and build this program using the MVC design pattern.

## Set Up
Clone this repository into your projects folder. Click the green "clone" button, copy the web url of this repository. Open terminal, navigate to the projects directory (`cd ~/Desktop/projects/`). Now run the command:
```
git clone https://github.com/foerever/Coda-Maze-Client.git
```

I'm using a python package manager called pipenv. Remember, we talked about thoughtfulness in everything we build? Package managers are a great example of this. When you're working with others, people might have different software and different versions of libraries installed. That difference can lead to bugs, can lead to programs working for you but not for others. So we document the packages and use a package manager to deal with versioning/installation. These days people take it a step further and fully replicate the entire development environment using something called docker. It's an extremely useful tool but out of the scope of this lesson. 

We already used a package manager in our previous projects that you should be somewhat familiar with, npm.

To install this package manager run the following command in terminal:
```
pip3 install pipenv
```

This will use the python 3 default package manager called pip3 to install this more sophisticated package manager called pipenv.

This repository already has a pipfile which documents what package dependencies you need. To install the required packages I specify, run this command in the terminal (your terminal should be currently in the root of this project folder). To do this open terminal, navigate to the projects directory (`cd ~/Desktop/projects/YoutubeTranscriptionMVC`).
```
pipenv install
```

When you want to work on the project you should run this command so that you are working within the context of the virtual environment set by pipenv:
```
pipenv shell
```

This should turn your regular command line prompt of:
```
anthonyc@Anthonys-MacBook-Pro-4:~/Desktop/projects/YoutubeTranscriptionMVC$ 
```

Into:
```
(YoutubeTranscriptionMVC) anthonyc@Anthonys-MacBook-Pro-4:~/Desktop/projects/YoutubeTranscriptionMVC$ 
```

Now we're ready to get started.

## Project
To do this project, we have 3 team members called model, view, and controller. You're the team leader, you need these 3 to work together to transcribe youtube videos. Each team member has something only they're capable of doing. Model can handle all the application logic. View can handle the interface. Controller can control what model and view do at any given time. Now, model and view both really hate you. They refuse to work directly with you. So you can only communicate with them through the controller. One more caveat, because of a special curse the model and view can never know each other exist. This means they can never interact directly with one another.

This is the scenario and how you should think about these 3 seperate components in the context of the MVC design pattern. 

"LMHxxvbzFqc"

### Problems
(1) In `yt_view.py` the function `get_youtube_id()`

(2) Switch out get transcript with manual first, if manual doesnt work use the auto generated.

(3) Let's say our team has had a discussion and determined that actually url parsing is application logic and therefore should not be contained in the view component. Modify the program such that the url parsing is done in the model instead.

## Styling
Thoughtfulness. Yes, that again. Now if we're being thoughtful when we're writing code, it might occur to us that we want other people to be able to understand our code easily. Likewise, we want to be able to easily understand the code of other developers. That's why developers have code style, the big companies often have great style guides that people throughout the world adhere to. For example, Airbnb has a well known style guide for javascript. For python, I think Google has written the best style guide which is called Pep 8. Let's try to adhere to that style guide for our code! But if it's a bit too much to do I completely understand!

Read about it [here](https://www.python.org/dev/peps/pep-0008/).