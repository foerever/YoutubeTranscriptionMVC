# YoutubeTranscriptionMVC
A coding assignment to transcribe youtube videos using the MVC design pattern. This is a LOT in terms of the depth of thinking you need to do. Remember what I told you this week, try to understand the general philosophy and motivation behind this and don't concern yourself too much with the less important aspects such as coding. It's perfectly okay for the code to not work, that's not the point of this assignment. Give your best shot and write down every thought in your head concerning each question.

## Introduction
Remember that one of the topics we discussed this week was the MVC (model view controller) design pattern. This is a relatively simple but extremely powerful design pattern used broadly through industry.

You can read more about the MVC pattern [here](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html) to refresh your memory. This is a very simple approach to MVC, it can actually get quite a bit more complex and there are many different ways to approach implementation of MVC (if you're interested in learning more about what this means ask me in our next lesson!). I was surprised to see a number of other reputable websites discussing MVC pretty badly, Apple does a good job of explaining it here correctly. In any case, I would be wary of what you read on the internet regarding MVC design pattern, it seems some people on the internet do not really understand what MVC is on a foundational level.

MVC is born out of a philosophy of purity, of building a system that is inherently flexible, maintanable, defensive, modular, coordinated, among other things. This is a rapidly growing idea in the field of Computer Science and software, we touched very briefly on functional programming once and it's a great example of this philosophy. Functional programming is a programming paradigm centered on that idea of purity, it's a programming style that in simple terms leads to less bugs and is theoretically very clean.

In any case let's get to the project at hand. You'll be working on a program that transcribes youtube videos and hopefully better understand what MVC means in the real world.

## Set Up
Clone this repository into your projects folder. Click the green "clone" button, copy the web url of this repository. Open terminal, navigate to the projects directory (`cd ~/Desktop/projects/`). Now run the command:
```
https://github.com/foerever/YoutubeTranscriptionMVC.git
```

I'm using a python package manager called pipenv. Remember, we talked about thoughtfulness in everything we build? Package managers are a great example of this. When you're working with others, people might have different software and different versions of libraries installed. That difference can lead to bugs and can lead to programs working for you but not for others. So we document the packages and use a package manager to deal with versioning/installation. These days people take it a step further and fully replicate the entire development environment using something called docker. It's an extremely useful tool but out of the scope of this lesson. 

We already used a package manager in our previous projects that you should be somewhat familiar with, npm.

To install this package manager run the following command in terminal:
```
pip3 install pipenv
```

This will use the python 3 default package manager called pip3 to install this somewhat more sophisticated package manager called pipenv.

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

This indicates that you are working in the correct python environment for this project defined by the pipfile. Now we're ready to get started.

## Project
To do this project, we have 3 team members called model, view, and controller. You're the team leader, you need these 3 to work together to transcribe youtube videos. Each team member has something only they're capable of doing. Model can handle all the application logic. View can handle the interface. Controller can control what model and view do at any given time. Now, model and view both really hate you. They refuse to work directly with you. So you can only communicate with them through the controller. One more caveat, because of a special curse the model and view can never know each other exist. This means they can never interact directly with one another.

This is the scenario and how you should think about these 3 seperate components in the context of the MVC design pattern.

The way this program is extremely simple since our aim is very simple. Our view is the interface for our user, it allows a user to input a youtube url that they want a transcription of. The model is able to retrieve the transcript of a youtube video given its id. 

### Problems
(1) What's the problem with using (`get_manually_created_transcript()`) in yt_controller? What if our youtube video doesn't have manually created transcript? 

For example, try inputting this WSJ interview with Microsoft CEO Satya Nadella:
```
https://www.youtube.com/watch?v=kexuG-YcQFA
```

Conveniently for us, youtube actually has ~okay auto generated youtube captions which we'll fetch and turn into our transcript. Even more conveniently for us, some other developer (me) already wrote a generalized version that will get the auto generated transcript if the manually created one doesn't exist. This function is `get_transcript()` in the model component. Luckily for us, it's very easy to replace the erroneous part in the controller because we're following the MVC design pattern. 

Change the error prone transcribe method used in the controller with the more generalized version.

(2) In `yt_view.py` the function `get_youtube_id()` is somewhat problematic. For one thing, it's succeptible to bugs because we rely too heavily on external dependencies to process inputs that can vary wildly. But one important thing to note is that in using the elegant ternary operator in the last line we don't tell the user why they have to re-input the youtube url. If we fail to capture the video id whether that is the fault of the user or our program, there is simply no handling of this error at all.

Write some error handling code that at a minimum notifies the user of why they have to re-input the youtube url in the case of faulty input or processing.

(3) Let's say our team has had a discussion and determined that url parsing is application logic and therefore should not be contained in the view component. Modify the program such that the url parsing is done in the model instead.

(4) The transcript isn't very pretty. It's in dictionary form. Concatenate the transcript into one long string and print that instead.

(BONUS) Create additional functionality in our program such that a user can search the video for the timestamp(s) (if any) in which the video mentions some key phrase (which the user can input). 

For example, you can imagine that there is a student who is looking through long (1-2 hour) lecture videos about the biology and chemistry of a sunflower. You're specifically looking for information regarding photosynthesis of sunflower plants. Now the student doesn't want to sit through 6 hours of sunflower biology when this student only wants to know about how a sunflower does photosynthesis. Unfortunately you can't control-f in a youtube video. But with our program maybe they can. The student should be able to enter a search term "photosynthesis" as well as a youtube video url and get a list of the exact timestamps where photosynthesis is mentioned!

## Styling
Thoughtfulness. Yes, that again. Now if we're being thoughtful when we're writing code, it might occur to us that we want other people to be able to understand our code easily. Likewise, we want to be able to easily understand the code of other developers. That's why developers have code style, the big companies often have great style guides that people throughout the world adhere to. For example, Airbnb has a well known style guide for javascript. For python, I think Google has written the best style guide which is called Pep 8. Let's try to adhere to that style guide for our code! But if it's a bit too much to do I completely understand!

Read about it [here](https://www.python.org/dev/peps/pep-0008/).