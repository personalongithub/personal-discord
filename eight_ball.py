import random
def eight_ball(question):
    answer = random.randint(1, 20)
    if '?' in question:
        if answer == 1: return 'Yes - definitely.'
        elif answer == 2: return 'It is decidedly so.'
        elif answer == 3: return 'Without a doubt.'
        elif answer == 4: return 'Reply hazy, try again.'
        elif answer == 5: return 'Ask again later.'
        elif answer == 6: return 'Better not tell you now.'
        elif answer == 7: return 'My sources say no.'
        elif answer == 8: return 'Outlook not so good.'
        elif answer == 9: return 'Very doubtful.'
        elif answer == 10: return 'It is certain.'
        elif answer == 11: return 'You may rely on it.'
        elif answer == 12: return 'As I see it, yes.'
        elif answer == 13: return 'Most likely.'
        elif answer == 14: return 'Outlook good.'
        elif answer == 15: return 'Yes.'
        elif answer == 16: return 'Signs point to yes.'
        elif answer == 17: return 'Cannot predict now.'
        elif answer == 18: return 'Concentrate and ask again.'
        elif answer == 19: return "Don't count on it."
        elif answer == 20: return 'My reply is no.'
        else: return 'There has been an error!'
    else: return 'A question must contain a question mark.'