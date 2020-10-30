from flask import Flask, request, render_template
import json
from nitrotype import get_player_data, get_team_data
import threading
import asyncio
import time
import codecs
app = Flask(__name__)
def write_json(data, file='data.json'):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/license')
def license():
    return render_template('LICENSE.md')
@app.route('/signup')
def signup():
    return render_template('signup/signup.html')
@app.route('/signup/player')
def signupplayer():
    return render_template('signup/player.html')
@app.route('/signup/team')
def signupteam():
    return render_template('signup/team.html')
@app.route('/testlb')
def testlb():
    return render_template('leaderboard.html')
@app.route('/data.json')
def datajson():
    file = codecs.open('data.json', 'r', 'utf-8')
    return file.read()
@app.route('/leaderboard/player')
def lb():
    with open('data.json') as f:
        data = json.load(f)

    players = []
    points = []
    speeds = []
    accuracys = []
    races = []
    displays = []
    cars = []
    for elem in data['users']:
        players.append(elem['username'])
        points.append(elem['points'])
        speeds.append(round(elem['speed']))
        accuracys.append(round(elem['accuracy']))
        races.append(elem['races'])
        displays.append(elem['displayname'])
        cars.append(elem['carID'])
    
    zipped_lists = zip(points, players)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedlb = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, displays)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sorteddisplay = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, players)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedusername = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, cars)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedcars = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, races)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedraces = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, speeds)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedspeeds = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, accuracys)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedaccuracy = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, points)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedpoints = [element for _, element in sorted_zipped_lists]
    html = '<table style="border-spacing: 2px; width: 100%"><tr style="background: grey;"><td style="padding: 10px;">Car</td><td style="padding: 10px;">Display Name</td><td style="padding: 10px;">Races</td><td style="padding: 10px;">Speed</td><td style="padding: 10px;">Accuracy</td><td style="padding: 10px;">Points</td></tr>'
    x = 0
    for player in sortedlb:
        html += '<tr style="height: 100px;background: #C0C0C0;"><td style=" padding: 10px;"><img src="https://www.nitrotype.com/cars/'+str(sortedcars[sortedlb.index(player)])+r'_small_1.png"></img></td><td onclick="openProfile({str(sortedusername[sortedlb.index(player)])})" style="padding: 10px;"><span style="font-size: 20px;">'+str(sorteddisplay[sortedlb.index(player)])+'</span></td><td style="padding: 10px;"><span style="font-size: 20px;">'+str(sortedraces[sortedlb.index(player)])+'</span></td><td style="padding: 10px;"><span style="font-size: 20px;">'+str(sortedspeeds[sortedlb.index(player)])+'</span></td><td style="padding: 10px;"><span style="font-size: 20px;">'+str(sortedaccuracy[sortedlb.index(player)])+'</span></td><td style="padding: 10px;"><span style="font-size: 20px;">'+str(sortedpoints[sortedlb.index(player)])+'</span></td></tr>'
        x = x + 1
        if x == 100:
            break
    html += '</table>'
    return html

@app.route('/leaderboard/team')
def tlb():
    with open('tdata.json') as f:
        data = json.load(f)

    players = []
    points = []
    speeds = []
    accuracys = []
    races = []
    displays = []
    for elem in data['teams']:
        players.append(elem['tag'])
        points.append(elem['points'])
        speeds.append(round(elem['speed']))
        accuracys.append(round(elem['accuracy']))
        races.append(elem['races'])
        displays.append(elem['name'])
    
    zipped_lists = zip(points, players)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedlb = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, displays)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sorteddisplay = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, players)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedusername = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, races)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedraces = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, speeds)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedspeeds = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, accuracys)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedaccuracy = [element for _, element in sorted_zipped_lists]

    zipped_lists = zip(points, points)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sortedpoints = [element for _, element in sorted_zipped_lists]
    html = '<table style="border-spacing: 2px; width: 100%"><tr style="background: grey;"><td style="padding: 10px;">Tag</td><td style="padding: 10px;">Name</td><td style="padding: 10px;">Races</td><td style="padding: 10px;">Speed</td><td style="padding: 10px;">Accuracy</td><td style="padding: 10px;">Points</td></tr>'
    x = 0
    for player in sortedlb:
        html += '<tr style="height: 100px;background: #C0C0C0;"><td>'+str(sortedusername[sortedlb.index(player)])+'</span></td><td>'+str(sorteddisplay[sortedlb.index(player)])+'</span></td><td style="padding: 10px;"><span style="font-size: 20px;">'+str(sortedraces[sortedlb.index(player)])+'</span></td><td style="padding: 10px;"><span style="font-size: 20px;">'+str(sortedspeeds[sortedlb.index(player)])+'</span></td><td style="padding: 10px;"><span style="font-size: 20px;">'+str(sortedaccuracy[sortedlb.index(player)])+'</span></td><td style="padding: 10px;"><span style="font-size: 20px;">'+str(sortedpoints[sortedlb.index(player)])+'</span></td></tr>'
        x = x + 1
        if x == 100:
            break
    html += '</table>'
    return html



@app.route('/signup/send/player', methods=['POST'])
def sent():
    form = request.form
    username = form['username']
    with open('data.json') as f:
        data = json.load(f)
    for user in data['users']:
        if user['username'] == username:
            return "<body style='background-color: aqua;'><h1 style='text-align: center;'>Nitrotype Leaderboard</h1><nav style='text-align: center;'><button><a href='/'>Home</a></button><button><a href='/signup'>Join the LB</a></button><button><a href='/leaderboard'>Leaderboard</a></button></nav><p>This username is already in the database</p></body>"
    playerdata = asyncio.run(get_player_data(username))
    if playerdata is None:
        return "<body style='background-color: aqua;'><h1 style='text-align: center;'>Nitrotype Leaderboard</h1><nav style='text-align: center;'><button><a href='/'>Home</a></button><button><a href='/signup'>Join the LB</a></button><button><a href='/leaderboard'>Leaderboard</a></button></nav><p>Couldn't find the account!</p></body>"
    for stat in playerdata['racingStats']:
        if stat['board'] == 'season':
            races = stat['played']
            speed = (int(stat['typed'])/5/float(stat['secs'])*60)
            accuracy = (100-((int(stat['errs'])/int(stat['typed']))*100))
            points = round(races*(100+(speed/2))*accuracy/100)
            break
    else:
        return "<body style='background-color: aqua;'><h1 style='text-align: center;'>Nitrotype Leaderboard</h1><nav style='text-align: center;'><button><a href='/'>Home</a></button><button><a href='/signup'>Join the LB</a></button><button><a href='/leaderboard'>Leaderboard</a></button></nav><p>No season data on this account!</p></body>"
    display_name = playerdata['displayName'] or username
    data['users'].append({'username': username, 'displayname': display_name, 'races': races, 'speed': speed, 'accuracy': accuracy, 'points': points, 'carID': playerdata['carID']})
    write_json(data)
    return "<body style='background-color: aqua;'><h1 style='text-align: center;'>Nitrotype Leaderboard</h1><nav style='text-align: center;'><button><a href='/'>Home</a></button><button><a href='/signup'>Join the LB</a></button><button><a href='/leaderboard'>Leaderboard</a></button></nav>You have been added to the leaderboards & if you have any questions make sure to contact any developers via discord!</body>"
@app.route('/signup/send/team', methods=['POST'])
def tsent():
    form = request.form
    tag = form['teamTag']
    with open('tdata.json') as f:
        data = json.load(f)
    for user in data['teams']:
        if user['tag'] == tag.upper():
            return "<body style='background-color: aqua;'><h1 style='text-align: center;'>Nitrotype Leaderboard</h1><nav style='text-align: center;'><button><a href='/'>Home</a></button><button><a href='/signup'>Join the LB</a></button><button><a href='/leaderboard'>Leaderboard</a></button></nav><p>This username is already in the database</p></body>"
    teamdata = asyncio.run(get_team_data(tag))
    if teamdata is None:
        return "<body style='background-color: aqua;'><h1 style='text-align: center;'>Nitrotype Leaderboard</h1><nav style='text-align: center;'><button><a href='/'>Home</a></button><button><a href='/signup'>Join the LB</a></button><button><a href='/leaderboard'>Leaderboard</a></button></nav><p>Couldn't find the account!</p></body>"
    for stat in teamdata['stats']:
        if stat['board'] == 'season':
            races = stat['played']
            speed = (int(stat['typed'])/5/float(stat['secs'])*60)
            accuracy = (100-((int(stat['errs'])/int(stat['typed']))*100))
            points = round(races*(100+(speed/2))*accuracy/100)
            break
    else:
        return "<body style='background-color: aqua;'><h1 style='text-align: center;'>Nitrotype Leaderboard</h1><nav style='text-align: center;'><button><a href='/'>Home</a></button><button><a href='/signup'>Join the LB</a></button><button><a href='/leaderboard'>Leaderboard</a></button></nav><p>No season data on this account!</p></body>"
    team_name = teamdata['info']['name'] or tag
    data['teams'].append({'tag': tag.upper(), 'name': team_name, 'races': races, 'speed': speed, 'accuracy': accuracy, 'points': points})
    write_json(data, 'tdata.json')
    return "<body style='background-color: aqua;'><h1 style='text-align: center;'>Nitrotype Leaderboard</h1><nav style='text-align: center;'><button><a href='/'>Home</a></button><button><a href='/signup'>Join the LB</a></button><button><a href='/leaderboard'>Leaderboard</a></button></nav>You have been added to the leaderboards & if you have any questions make sure to contact any developers via discord!</body>"
def runflask():
    app.run(host='0.0.0.0')
def task():
    while True:
        print(str(round(time.time()))+' - Updated Leaderboard File')
        with open('data.json') as f:
            data = json.load(f)
        users = data['users']
        data['users'] = []
        for user in users:
            playerdata = asyncio.run(get_player_data(user['username']))
            try:
                for stat in playerdata['racingStats']:
                    if stat['board'] == 'season':
                        races = stat['played']
                        speed = (int(stat['typed'])/5/float(stat['secs'])*60)
                        accuracy = (100-((int(stat['errs'])/int(stat['typed']))*100))
                        points = round(races*(100+(speed/2))*accuracy/100)
                display_name = playerdata['displayName'] or user['username']
                data['users'].append({'username': user['username'], 'displayname': display_name, 'races': races, 'speed': speed, 'accuracy': accuracy, 'points': points, 'carID': playerdata['carID']})
            except TypeError:
                pass
        write_json(data)
        time.sleep(600)
def task1():
    while True:
        print(str(round(time.time()))+' - Updated Team Leaderboard File')
        with open('tdata.json') as f:
            data = json.load(f)
        users = data['teams']
        data['teams'] = []
        for user in users:
            teamdata = asyncio.run(get_team_data(user['tag']))
            try:
                for stat in teamdata['stats']:
                    if stat['board'] == 'season':
                        races = stat['played']
                        speed = (int(stat['typed'])/5/float(stat['secs'])*60)
                        accuracy = (100-((int(stat['errs'])/int(stat['typed']))*100))
                        points = round(races*(100+(speed/2))*accuracy/100)
                display_name = teamdata['info']['name']
                data['teams'].append({'tag': user['tag'].upper(), 'name': display_name, 'races': races, 'speed': speed, 'accuracy': accuracy, 'points': points})
            except TypeError:
                pass
        write_json(data, 'tdata.json')
        time.sleep(600)
runthread = threading.Thread(target=runflask)
taskthread = threading.Thread(target=task)
task1thread = threading.Thread(target=task1)
runthread.start()
taskthread.start()
task1thread.start()
runthread.join()