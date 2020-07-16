
from bs4 import BeautifulSoup
from discord.ext import commands
import discord
import requests
import mechanicalsoup

class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Command 
    @commands.Cog.listener()
    async def on_ready(self):
        print('Weather Beta Commands Loaded')

    @commands.command(aliases=['SPC','SPCTest','storm','spc'])
    async def Storm(self, ctx, * SPCDay):
        await ctx.send(f'Here are the Day One Outlook for today:\n https://www.spc.noaa.gov/products/outlook/')

    @commands.command(aliases=['WPC','wpc'])
    async def weathermap(self, ctx):
    	await ctx.send(f'Here is the latest National Weather Map:\n https://www.wpc.ncep.noaa.gov/NationalForecastChart/staticmaps/noaad1.png')

    @commands.command(aliases=['nws'])
    async def NWS(self, ctx, *, nwsoffice):
        await ctx.send(f'Here is the {nwsoffice} NWS Office Website:\n https://weather.gov/{nwsoffice}//')

    @commands.command(aliases=['nwshelp'])
    async def NWSHelp(self, ctx):
    	await ctx.send(f'Map of NWS Offices are here:\n https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/NWS_Weather_Forecast_Offices.svg/480px-NWS_Weather_Forecast_Offices.svg.png')

    @commands.command(aliases=['radar'])
    async def Radar(self, ctx, *, radarstation):
    	await ctx.send(f'Here is the {radarstation} radar:\n https://radar.weather.gov/radar.php?rid={radarstation}')

    @commands.command(aliases=['radarhelp'])
    async def RadarHelp(self, ctx):
    	await ctx.send(f'List of Radar Stations are Here:\n https://radar.weather.gov/index_lite.htm')

    @commands.command(aliases=['SPCDayOne','spcdayone','SPCdayone','spcDayone','SPC1'])
    async def DayOneOutlook(self, ctx):
        await ctx.send(f'Day 1 Storm Prediction Center Outlook:\n https://www.spc.noaa.gov/products/outlook/day1otlk.html')

    @commands.command()
    async def temp(self, ctx, *, city):
        #MechanicalSoup
        browser = mechanicalsoup.StatefulBrowser(
            soup_config={'features': 'lxml'},
            raise_on_404=True,
            user_agent='MyBot/0.1: mysite.example.com/bot_info',
        )
        browser.set_verbose(2)
        browser.open("https://www.weather.gov/")
        browser.launch_browser()
        browser.select_form('browser[action="/zipcity"]')
        browser["inputstring"] = city
        browser.submit_selected(btnName="Go2")
        print(browser.get_url)
        citysite = browser.get_url
        #BeautifulSoup
        source = requests.get(citysite).text
        soup = BeautifulSoup(source, 'lxml')
        body = soup.find('body')
        current_conditions = body.find('div', class_='panel-body')
        temperture = current_conditions.find('p', class_='myforecast-current-lrg').text
        await ctx.send(f'The temperature in {city} is {temperture}')

def setup(client):
    client.add_cog(Weather(client))
    
   	
