# Model
The model is available through Google Drive 
[Link](https://drive.google.com/file/d/1Og8cjnlB9Z0SmW8iw6ze-mY2tomjMKMF/view?usp=sharing)

# Problem Summary

What should I watch? Due to the current pandemic the global community is facing, many Canadians are now forced to stay in their homes. A minority of the total population have yards and areas to play within; however many live in small apartments and condos forcing them to watch more TV and movies then they would probably like.

With such a massive amount of choice, it can be somewhat daunting to choose just one. This recommender hopes to help.

# Approach

In order to solve this problem, we can gather data from user input and compare it to a of movies maintained by [grouplens](https://grouplens.org/). From this we can create an algorithm to provide movie list recommendations to the user.

The parameters we will be working with are; 

* movie genres

With this data we can build a recommender system in which the user inputs the desired genre they wish to watch. Based on these inputs we will generate a short list of movies that fit their preferences.

# Problem Statement

Canadians are stuck indoors more than usual due to the Covid pandemic, we would like to help them find the right movie to suit their tastes, and relieve some of the frustration they may currently be facing.

## Ideal

The user tells the recommender program the genres they would ideally like to watch. The program then uses the input given to recommend the best movies that best suit the user’s choice.

## Reality

With all the streaming options available today, it can be very difficult to narrow downa list of movies that suits everyone. They often settle on the path of least resistance, choosing often to watch a movie that does not satisty everyone.

## Limitations

Due to the limitations of processing power, we are currently limited to the size of our dataset. We were forced to work with;

- MovieLens 1M movie ratings. Stable benchmark dataset. 1 million ratings from 6000 users on 4000 movies. Released 2/2003.

Hopefully, as we improve the code and model, we can increase the size of the dataset and include more current movies. BUT, just because a movie is old, does not mean it is not good to watch.

## Proposal

At this time Canadians are stuck indoors more than usual, we would like to alleviate some of the stress they may now face daily and help them find the right movie to suit their tastes.

# Rationale

We want to simplify the choices and get people on the couch watching a great film as quickly as possible.

