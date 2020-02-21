import asyncio
import configparser
from pyppeteer import launch


async def main():
# if __name__ == "__main__":
    
    config = configparser.ConfigParser()
    config.read('conf.ini')
    username = config['DEFAULT']['somosmas_user'].strip('"')
    password = config['DEFAULT']['somosmas_pass'].strip('"')
    # print(username)

    title = "Title"
    description = "Description"
    category = "Política, economía y opinión"
    tags = "Cuba"
    genre = "Podcast"
    language = "castellano"

    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('https://us.ivoox.com/es/')
    await page.waitFor(1000)
    await page.click('#main-navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a')
    await page.waitFor(1000)
    # await page.waitForNavigation();
    await page.type('#at-user', username)
    await page.type('#at-pw', password)

    await page.click('#btn-enter')
    await page.waitForNavigation()
    await page.click("#main-navbar > ul.nav.navbar-nav.navbar-right > li.hidden-xs > a")


    await page.waitForSelector('input[type=file]')
    await page.waitFor(1000)
    inputUploadHandle = await page.querySelector('input[type=file]')
    await inputUploadHandle.uploadFile('karlito.mp3')
    await page.waitFor(30000)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())