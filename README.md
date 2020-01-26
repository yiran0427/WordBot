# WordBot
A web app aimed at improving children's vocabulary by automating the creation vocabulary lists based on statistical methods and establishing active learning by interacting through speech.

## Inspiration

We were inspired by brainstorming ways in which we could bring all group members' interests together. This included bringing together _education_, _data visualization/analysis_, and _positive social impact_ onto one platform.

## Functionality
The web-based application attempts to emulate a classroom environment set up to improve children's communication skills through dynamic learning. This includes letting the child (student) actively interact with our vocabulary lists, keeping track of their progress, and using that feedback to adjust the difficulty of each interaction so that the child's (student's) learning progresses more smoothly while keeping them motivated.

## Design
We built this product by breaking it down to three main sub-products and then integrating them together.

* Creating a database by parsing thousands of text documents at various grade levels, formatting them to ensure quality of data, and then applying statistical models on the length and frequency of a word to determine overall difficulty of word. 
* Creating an online user-based platform that would easily be accessibly by everyone. This will be used to interact with users, track their progress, and adjust the difficulty of interaction based on the feedback received from the user. The difficulty of interaction will be repeatedly updated based on the user's learning progress. 
* Creating a way to ensure users to actively interact with the product. We chose to use a speech recognition software in which users could verbally interact with the vocabulary. It maintains a sense of physical interaction which could be difficult to produce through an online environment. We hope it provides a more active form of learning. 

Once, we finished creating the three sub-products, the last task was to put it all together. This includes importing the database to our web app and using speech recognition method to test the user.

## Use
Check this out at [my website](https://www.student.cs.uwaterloo.ca/~h286wu/WordBot/index.html).

## Possible Improvement
We might further develop this web application through the following: 
* Develop the website/app to ensure the greatest compatibility on different devices (mobile, web, tablet, etc.)
* Proof of the validity of the statistical model
* Compatibility of the integeration of each technologies and languages we used to complete subtasks
* Improve the User Interface (UI) for better users' experience
* Offering French as a new language

## Accomplishments
We are delighted that given the strict time constraint, we were able to work well both individually and as a team. The greatest problems that await us in the future are the ones which require immense cooperation as a team. As such, we are all proud to have the opportunity to help one another throughout the entire event.

Additionally, we are also proud of the potential impact our project could have on literacy rates, not just in our own community, but on a global scale where sometimes there is more technology than there are teachers/educators.

## Contributors
This game is developed by [Yiran Cao](https://github.com/yiran0427) (HTML/CSS), [Haochen Wu](https://github.com/JasonWu1103) (HTML/CSS, php), [Fahim Yusuf](https://github.com/TinyThugTim) (Python), and Maninder Bhogal(Voice Recognition API). 

## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details.
