# Scoring game

import tkinter
from graphics import Canvas
import random
import time


"Cricket is a sport loved by millions globally. My_Score is a game of luck that generates runs for a player to beat the fastest scorer"

CANVAS_WIDTH = 850
CANVAS_HEIGHT = 850
CIRCLE_SIZE = 40


def main():
    lead_cricketer = str('Shane W')
    lead_scorer_score = 100
    size = 40
    your_score = 0
    score_time = 20
    badge = 0
    top_badges = 20
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    myfinal_project = canvas.create_text(10,100, text="Final Project - CIP, Stanford University", font='Arial', anchor='sw',
                                          color="red")


    #canvas.wait_for_click()
    #canvas.mainloop()

    canvas.pack()

    my_score_cricketintro = canvas.create_text(10, 150, text="Cricket is a sport loved by millions globally.",
                                               font='Arial', anchor='sw', color='blue')
    my_score_intro = canvas.create_text(10, 200, text="MyCricScore - a new cricket game ", font='Arial', anchor='sw',
                                        color='black')
    my_score_name = canvas.create_text(10, 260, text="Created and developed by Ritika Hiranandani", font='Arial',
                                       anchor='sw', color='black')
    my_score_intro1 = canvas.create_text(10, 310, text="Top player on MyCricScore - Shane Warner. Can you beat his score - " + str(lead_scorer_score) + " runs in "
                                                       + str(score_time) + " seconds",
                                         font='Arial', anchor='sw', color='blue')
    my_score_yes = canvas.create_text(10, 360, text="Double Click to Play", font='Arial',anchor='sw', color='red')
    canvas.pack()
    canvas.wait_for_click()
    canvas.delete(myfinal_project)
    canvas.delete(my_score_intro)
    canvas.delete(my_score_intro1)
    canvas.delete(my_score_cricketintro)
    canvas.delete(my_score_yes)
    canvas.delete(my_score_name)
    center_x = random.randint(25, 250)
    center_y = random.randint(25, 250)

    N_CIRCLES = random.randint(2, 6)
    lead_cricketer = str('Shane W')
    lead_scorer_score = 100
    size = 40
    your_score = 0
    score_time = 20
    badge = 0
    # """print('The Top Scorer is ' +lead_cricketer+ '-' + str(lead_scorer_score) + ' runs in ' + str(score_time) +  ' seconds')
    # print ('Do you want to beat his score? Press the Enter key to play')
    # response = input()"""

    # if response == 'No' or response == 'no':
    # print("Sorry, you do not want to score today See you again soon!")
    # if response == 'Yes' or response == 'yes':

    # if response =='':

    start = time.time()
    print(start)
    your_score = 0

    lead_scorer_score = 100


    while True:

        canvas.wait_for_click()
        canvas.delete('all')
        your_score = int(N_CIRCLES + your_score)





        for i in range(N_CIRCLES):

            random_circles(canvas, center_x, center_y, size)
            current_time = time.time()
            time_elapsed = current_time -start
            print("Start")
            print(start)
            print("Current time")
            print(current_time)
            print("Time elapsed")
            print(time_elapsed)
            time_remaining =  int(score_time-time_elapsed)
            print("time remaining")
            print(time_remaining)



            print("T")
            text_runs = canvas.create_text(100, 100, text="You scored  " + str(N_CIRCLES) + " runs", font='Arial',
                                           anchor='sw', color='blue')
            text_runs = canvas.create_text(8, 350, text="Click 'Yes' to continue scoring ", font='Arial', anchor='sw',
                                           color='black')
            text_runs = canvas.create_text(300, 100, text="Time remaining: " + str(time_remaining) + " seconds", font='Arial', anchor='sw',
                                           color='blue')
            text_runs = canvas.create_text(350, 450, text="Current score: " + str(your_score) + " runs",
                                           font='Arial', anchor='sw',
                                           color='blue')



            center_x = random.randint(25, 250)
            center_y = random.randint(25, 250)


        if N_CIRCLES == 4:
            # print('Congratulations! You hit a boundary')
            text_runs = canvas.create_text(10,250,  text="Great job! You hit a boundary  ", font ='Arial', anchor='sw',color='blue')
            text_runs = canvas.create_text(8, 350, text="Click 'Yes' to continue scoring ", font='Arial', anchor='sw',
                                           color='black')
            text_runs = canvas.create_text(300, 100, text="Time remaining: " + str(time_remaining) + " seconds",
                                           font='Arial', anchor='sw',
                                           color='blue')
            text_runs = canvas.create_text(350, 450, text="Current score: " + str(your_score) + " runs",
                                           font='Arial', anchor='sw',
                                           color='blue')

            canvas.delete(text_runs)


        if N_CIRCLES == 6:
            # print('Congratulations! You hit a sixer, Master Blaster!')
            text_runs = canvas.create_text(10, 250, text="Excellent sixer! Master Blaster! ", font='Arial',
                                           anchor='sw', color='blue')
            text_runs = canvas.create_text(8, 350, text="Click 'Yes' to continue scoring ", font='Arial', anchor='sw',
                                           color='black')
            text_runs = canvas.create_text(300, 100, text="Time remaining: " + str(time_remaining) + " seconds",
                                           font='Arial', anchor='sw',
                                           color='blue')
            text_runs = canvas.create_text(350, 450, text="Current score: " + str(your_score) + " runs",
                                           font='Arial', anchor='sw',
                                           color='blue')
            #canvas.delete('all')

            #text_gameover = canvas.create_text(10, 250, text="Game Over!", font='Arial', anchor='sw', color='blue')


            # print('Your total score is ' + str(your_score) + ' runs')

        if your_score > lead_scorer_score:

            canvas.delete('all')
            #canvas.clear()
            #time.sleep(1)

            #canvas.pack()
            #time.sleep(2)
            print('Congratulations! You beat the top scorer')
            end = time.time()
            length = int(end - start)
            print('It took you ' + str(length) + ' seconds to beat Warner! You are now the top scorer')
            print('Game Over!')
            #canvas.delete('all')



            print("canvas")
            text_gameover = canvas.create_text(100, 250, text="Game Over!", font='Arial', anchor='sw', color='blue')

            text_badge = canvas.create_text(100, 300, text="Congratulations! You won a MyCricScore badge",
                                                font='Arial', anchor='sw', color='blue')
            text_score = canvas.create_text(100, 350, text="Your total score is " + str(your_score) + " runs",
                                                font='Arial', anchor='sw', color='blue')
            text_time = canvas.create_text(100, 400, text="It took you " + str(length) + " seconds to beat Shane W",
                                               font='Arial', anchor='sw', color='red')
            #text_congrats = canvas.create_text(10, 350,  text="You are now the topmost scorer on My_Score!", font = 'Arial',font_size=15, color='blue')
            rect = canvas.create_rectangle(130, 130, 200, 200, color='yellow')
            canvas.wait_for_click()

            canvas.pack()

            #time.sleep(2)
            canvas.mainloop()
            print('break')
            #text_gameover = canvas.create_text(100, 250, text="Game Over!", font='Arial', anchor='sw', color='blue')
            break
        # print('Press Enter to continue scoring')
        # response = input()

        N_CIRCLES = random.randint(2, 6)

        #your_score = int(N_CIRCLES + your_score)

    """if your_score > lead_scorer_score:
     print('xxx')
     canvas.delete('all')
     rect = canvas.create_rectangle(130, 130, 200, 200, color='yellow')
     text_runs = canvas.create_text(130, 130, text="Click 'Yes' to continue scoring ", font='Arial', anchor='sw',
                                    color='black')
    #canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
     canvas.wait_for_click()

     canvas.pack()
     time.sleep(2)
     print("end")
    #text_runs = canvas.create_text(100, 100, text="Hello", font='Ariel', anchor='sw', color='blue')"""




def random_circles(canvas, center_x, center_y, size):
            left_x = center_x - size / 2
            top_y = center_y - size / 2
            right_x = left_x + size
            bottom_y = top_y + size

            circle_color = random_color()
            # canvas = Canvas(CANVAS_WIDTH/2, CANVAS_HEIGHT/2)
            canvas.create_oval(left_x, top_y, right_x, bottom_y, 'red')

def random_color():
            """
            This is a function to use to get a random color for each circle. We have
            defined this for you and there is no need to edit code in this function,
            but feel free to read it over if you are interested.
            """
            colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
            return random.choice(colors)



if __name__ == '__main__':
            main()




