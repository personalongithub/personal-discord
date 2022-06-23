"""Gives the functions of a Magic 8-Ball."""
import random


def eight_ball(question):
    """Functions like a Magic 8-Ball."""
    answer = random.randint(1, 20)
    if '?' in question:
        if answer == 1:
            returned_answer ='Yes - definitely.'
        elif answer == 2:
            returned_answer = 'It is decidedly so.'
        elif answer == 3:
            returned_answer = 'Without a doubt.'
        elif answer == 4:
            returned_answer = 'Reply hazy, try again.'
        elif answer == 5:
            returned_answer = 'Ask again later.'
        elif answer == 6:
            returned_answer = 'Better not tell you now.'
        elif answer == 7:
            returned_answer = 'My sources say no.'
        elif answer == 8:
            returned_answer = 'Outlook not so good.'
        elif answer == 9:
            returned_answer = 'Very doubtful.'
        elif answer == 10:
            returned_answer = 'It is certain.'
        elif answer == 11:
            returned_answer = 'You may rely on it.'
        elif answer == 12:
            returned_answer = 'As I see it, yes.'
        elif answer == 13:
            returned_answer = 'Most likely.'
        elif answer == 14:
            returned_answer = 'Outlook good.'
        elif answer == 15:
            returned_answer = 'Yes.'
        elif answer == 16:
            returned_answer = 'Signs point to yes.'
        elif answer == 17:
            returned_answer = 'Cannot predict now.'
        elif answer == 18:
            returned_answer = 'Concentrate and ask again.'
        elif answer == 19:
            returned_answer = "Don't count on it."
        elif answer == 20:
            returned_answer = 'My reply is no.'
        else:
            returned_answer = 'There has been an error!'
    else:
        returned_answer = 'A question must contain a question mark.'
    return returned_answer
