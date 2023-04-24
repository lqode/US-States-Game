import turtle
import pandas

image = "../inputs/blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic(image)
# screen.addshape(image)
# turtle.shape(image)

correct_answers = set()  # to keep track of unique states guessed

data = pandas.read_csv("../inputs/50_states.csv")
all_states = data.state.to_list()

while len(correct_answers) < 50:

    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        df = pandas.DataFrame(all_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        correct_answers.add(answer_state)
        all_states.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        # t.write(state_data.state.item())
        t.write(answer_state)
