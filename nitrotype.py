import aiohttp
from bs4 import BeautifulSoup
from json import loads
from re import findall
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
async def get_player_data(racer):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, f'https://www.nitrotype.com/racer/{racer}')
    newdata = {}
    soup = BeautifulSoup(response, 'html5lib')
    for script in soup.find('head'):
        if 'RACER_INFO' in str(script):
            newdata = loads(findall('{".+}', str(script))[0])
    if newdata == {}:
        success = False
        return
    return newdata
async def get_team_data(team):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, f'https://www.nitrotype.com/api/teams/{team}')
    data = loads(response)
    if data['success'] == False:
        return
    else:
        return data['data']