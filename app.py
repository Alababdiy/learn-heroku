

from flask import request,Flask,render_template
import json

app = Flask(__name__,static_url_path='/static')


@app.route('/ATriggerVerify.txt')
def ATrigger():
    return render_template('ATriggerVerify.txt')

from random import randint
@app.route('/A901705BCA20474D850A0B95EF503A',methods=['POST'])
def post_values():
    return 'This Script NOT Available <br/> contact with  Developer MSGR : m.me/Alababdiy <br/> Email : alababdiy@gmail.com'
    prm = json.loads(request.get_data().decode('utf-8'))
    try:
        USER_XP = float(prm['USER_XP'])
        ENEMY_XP = float(prm['ENEMY_XP'])
        USER_HEALTH = float(prm['USER_HEALTH'])
        ENEMY_HEALTH = float(prm['ENEMY_HEALTH'])
    except:
        return 'PLEACE SEND ALL Vars  '

    ADVANTAGE_XP = USER_XP / ENEMY_XP

    ADVANTAGE_HEALTH = USER_HEALTH - ENEMY_HEALTH

    random_num = randint(0, 100)
    ODDS = random_num + ADVANTAGE_HEALTH

    if ODDS < 0:
        ODDS = 0

    EDGE = round(ODDS * ADVANTAGE_XP) / 50
    REWARD =  INJURY = 0
    if EDGE >= 1:
        RESULT = "WIN"
    else:
        RESULT = "LOSE"

    if RESULT == "WIN":
        REWARD = (EDGE - 1) * 100
    else:
        INJURY = round((100 - EDGE * 100) / 10)
        if INJURY >= USER_HEALTH:
            INJURY = USER_HEALTH

    rspns = {
        "ADVANTAGE_XP": ADVANTAGE_XP,
        "ADVANTAGE_HEALTH": ADVANTAGE_HEALTH,
        "ODDS": ODDS,
        "EDGE": EDGE,
        "RESULT": RESULT,
        "RANDOM": random_num,
        "REWARD": REWARD,
        "INJURY": INJURY
    }

    return json.dumps(rspns)




if __name__ == '__main__':
    app.run()

