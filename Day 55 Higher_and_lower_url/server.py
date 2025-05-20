from flask import Flask
import random
app=Flask(__name__)

random_number=random.randint(0,9)
print(random_number)
@app.route(f'/<int:number>')
def check(number):
    if (number==random_number):
        return ('<h1>Your guess is correct Hurray!</h1><br/>'
                '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3oxM2txZjIwN29oZGtobnV3ZzJkMnd2aG5ubWc5YmF1b2JlbXRocCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lZTvTGEGKU6gnQ2wBr/giphy.gif"'
                'alt="You are a winner"/>')
    elif(number<random_number):
        return ('<h1>Naahhh! Too Low</h1><br/>'
                '<img src="https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif?cid=ecf05e47yu9yxmxuzh7ef1u44am3bemln7qsf13p62iaglv9&ep=v1_gifs_search&rid=giphy.gif&ct=g"'
                'alt="Too low"/>')
    else:
        return ('<h1>That is absolutely high!!</h1><br/>'
                '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWNvOWw3b2RsbzJ3d2V5b3R1MmE1M2xscmZvdTA0NXF1dG9qZWpkayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PR3585ZZSvcHO9pa76/giphy.gif"'
                'alt="Too high"/>')

@app.route('/')
def guessing_game():
    return ("<h1>Guess a number between 0 and 9 </h1><br/>"
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeW43cndvZWd4N3YwdzhjbzUwMG1wODUwcWtuamlhZG5zZnBhdWZ3aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DhiRqIsofVMi7fWNBQ/giphy.gif'"
            "alt='uhh guessing a number from 0 to 9'/>")

if __name__=="__main__":
    app.run(debug=True)