import simpleguitk as simplegui
import random, math

#Delayem programmy
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
PAD_WIDTH = 8
PAD_HEIGHT = 80
BALL_RADIUS = 10
PADDLE_VEL=0
PADDLE_VEL2=0
PADDLE1_POS=HEIGHT/2
PADDLE2_POS=HEIGHT/2
BALL_VEL=0
BALL_VEL2=0
score1=0
score2=0
kof=-2
p=0
b=0

# helper function that spawns a ball by updating the ball's position vector
# and velocity vector if right is True, the ball's velocity is upper right, else upper left
def ball_init(right=True):
    global ball_pos, BALL_VEL, p, b # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    p=random.randint (-2,2)
    b=random.randint(-1,1)
    if p==0:
        p+=random.randrange(1,2)
    if b==0:
        b+=random.randrange(1,2)
    BALL_VEL=[p*random.randrange(2,4), b*random.randrange(3,5)]

def draw(c):
    global score1, score2, PADDLE1_POS, PADDLE_VEL, PADDLE2_POS, PADDLE_VEL2, ball_pos, BALL_VEL, kof

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH-PAD_WIDTH, 0],[WIDTH-PAD_WIDTH, HEIGHT], 1, "White")

    PADDLE1_POS = PADDLE1_POS + PADDLE_VEL
    PADDLE2_POS = PADDLE2_POS + PADDLE_VEL2

    # draw paddles
    c.draw_line([WIDTH-PAD_WIDTH/2, PADDLE2_POS+PAD_HEIGHT/2],[WIDTH-PAD_WIDTH/2, PADDLE2_POS-PAD_HEIGHT/2], 8, "Aqua")  #r
    c.draw_line([0+PAD_WIDTH/2, PADDLE1_POS+PAD_HEIGHT/2],[0+PAD_WIDTH/2, PADDLE1_POS-PAD_HEIGHT/2], 8, "Aqua")    #l

    # paddle_1
    if PADDLE1_POS-PAD_HEIGHT/2<=0:
        PADDLE1_POS=PAD_HEIGHT/2
    if PADDLE1_POS+PAD_HEIGHT/2>=HEIGHT:
        PADDLE1_POS=HEIGHT - PAD_HEIGHT/2

    # paddle_1
    if PADDLE2_POS-PAD_HEIGHT/2<=0:
        PADDLE2_POS=PAD_HEIGHT/2
    if PADDLE2_POS+PAD_HEIGHT/2>=HEIGHT:
        PADDLE2_POS=HEIGHT - PAD_HEIGHT/2

    # update ball
    ball_pos[0]+=BALL_VEL[0]
    ball_pos[1]+=BALL_VEL[1]

        #d ball
    if ball_pos[1]+BALL_RADIUS>=HEIGHT:
        BALL_VEL[1]*=-1
    elif ball_pos[1]-BALL_RADIUS<=0:
        BALL_VEL[1]*=-1
#left
    elif ball_pos[0]-BALL_RADIUS<=PAD_WIDTH:
        if (ball_pos[1]<=PADDLE1_POS+PAD_HEIGHT/2) and (ball_pos[1]>=PADDLE1_POS-PAD_HEIGHT/2):
            BALL_VEL[0]*=kof
        else:
            score2+=1
            ball_init(True)
#right
    elif ball_pos[0]+BALL_RADIUS>=WIDTH-PAD_WIDTH:
        if (ball_pos[1]<=PADDLE2_POS+PAD_HEIGHT/2) and (ball_pos[1]>=PADDLE2_POS-PAD_HEIGHT/2):
            BALL_VEL[0]*=kof
        else:
            score1+=1
            ball_init(True)

    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Aqua", "White")
   # canvas.draw_text(score1, [150, 30], 20, "White")
    c.draw_text(str(score1), [20, 60], 36, "#A9D4F0")
    c.draw_text(str(score2), [WIDTH-50, 60], 36, "#A9D4F0")




def keydown(key):
    #left
    global  PADDLE_VEL, PADDLE_VEL2
    if key==simplegui.KEY_MAP["W"]:
        PADDLE_VEL=-10
    if key==simplegui.KEY_MAP["S"]:
        PADDLE_VEL=10

    #right
    if key==simplegui.KEY_MAP["up"]:
        PADDLE_VEL2=-10
    if key==simplegui.KEY_MAP["down"]:
        PADDLE_VEL2=10

def keyup(key):
    #left
    global PADDLE_VEL, PADDLE_VEL2
    if key==simplegui.KEY_MAP["W"]:
        PADDLE_VEL=0
    if key==simplegui.KEY_MAP["S"]:
        PADDLE_VEL=0

    #right
    if key==simplegui.KEY_MAP["up"]:
        PADDLE_VEL2=0
    if key==simplegui.KEY_MAP["down"]:
        PADDLE_VEL2=0

def restart():
    global score1, score2
    global paddle1_pos, paddle2_pos
    global side
    score1, score2 = 0, 0
    ball_init()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)

restart()

# start frame
frame.start()