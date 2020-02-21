import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('https://soundcloud.com/signin')
    await page.type('input[name=username]', "username")
    await page.click('#content > div > div > div.l-content > div.l-main > form > div > div.signinForm__step.signinForm__initial > div > button')
    await page.waitFor(2000)
    # cookies = await page.cookies()
    # page2 = await browser.newPage()
    # await page2.setCookie(cookies)
    await page.type('input[name=password]', "pass")
    await page.click('#content > div > div > div.l-content > div.l-main > form > div > div.signinForm__step.signinForm__signin_with_password > div > button')
    # await page.waitFor(2000)
    # await page.screenshot({'path': 'example.png'})
    await page.waitForNavigation();

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())