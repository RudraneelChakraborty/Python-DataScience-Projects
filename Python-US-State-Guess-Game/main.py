import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data_file = pd.read_csv('50_states.csv')
all_states = data_file.state.to_list()
game_is_on = True
guessed_state = []

while game_is_on:
    answer_state = screen.textinput(title = f'{len(guessed_state)}/50 States Correct', prompt = "What's another state name?").title()
    print(answer_state)
    
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle
        t.penup()
        state_data = data_file[data_file.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())


    if len(guessed_state) == 50 or answer_state == 'Exit':
        game_is_on = False
        


screen.exitonclick()
