



#GOPBOT
#Coded in Python
#Coded by ZWEKKERBOY#2931
#Developed by CRO-Thehacker#7928, @laojinTheCaesium#6577 & @spooki uamee#1139
#Tested by Tovarisch NeoN#7364, WeedIsLife#3286, uncle_Миша#2403 & LaugeJ8#6904
#Hosted by Kleine#6130 
#Credits for GOPBOT profile picture: LaugeJ8#6904

#Importing libraries 
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

#Devining the bot
Gopbot = discord.Client()
gopbot = commands.Bot(command_prefix ='!')

#Setting the AdminID for ADMIN commands
#ADMINidZWEK ADMINidCRO ADMINidKLEINE
ADMINidZWEK = "239653545270312960"
ADMINidCRO = "377981578716119050"
ADMINidKLEINE = "237979016991080448"

#List with all hardbass creators
HardbassCreatorsList1 = '**HARDBASS CREATORS** \n**Adies Lad** - `https://www.youtube.com/channel/UCZvjPWODsHYX5_Y7iCmz-9g` \n**apartje.** - `https://www.youtube.com/channel/UCgL9Kp942itDl4D1Sa9mSOQ` - _Our honoured Slav that brought us Cheeki breeki hardbass._ \n**bandithedoge music** - `https://www.youtube.com/channel/UCMosYVHeaPgJ14Sd-qEubzg` \n**Davay** - `https://www.youtube.com/channel/UC2MqJ6xiLmHWgfEO1zUEnnw` - _Brought us Tri Poloski._ \n**DJ Czech Slav** - `https://www.youtube.com/channel/UCBEw_pXwlO13nN1RjLjoGpQ` \n**DJ Donk** - `https://www.youtube.com/channel/UC9E8vdJDo24V0foxR-Z12Ig` \n**DJ Frank** - `https://www.youtube.com/channel/UCibhg2m_-DNkjN3sDYlG2Uw` \n**DJ Nexeuz** - `https://www.youtube.com/channel/UC99eeiqR9IN1rFxW437YwIg` \n**DJ PUMP** - `https://www.youtube.com/channel/UCZjxTFvOYgiLBs_t3UcFpnw` \n**DJ SlavBrother** - `https://www.youtube.com/channel/UCKcRPvQrb_hdjOc7OBqCMlw` \n**DJ TOTZI** - `https://www.youtube.com/channel/UCrZ9kx-C9lb38rIUsFDU4Tg`' 
HardbassCreatorsList2 = "**EarSlav** - `https://www.youtube.com/channel/UCNrXk1ugexWqv7AFD7LLkNQ` \n**Exodus** - `https://www.youtube.com/channel/UCX10mFOnlbR_lQ6IZcqRQlg` \n**Gopnik McBlyat** -  `https://www.youtube.com/channel/UCusaOYfkki9drs2eIfRZGfQ` \n**HARD BASS SCHOOL**  - `https://www.youtube.com/channel/UCJKnwx_goBYHUOS8Zj_4LEw` \n**Jandy** - `https://www.youtube.com/user/JandyCZ` \n**Krovjaznik** - `https://www.youtube.com/channel/UCLIWsAUiWvqtHhPOHq0BGbQ` \n**Ley o'Lantern** - `https://www.youtube.com/watch?v=Yr4sKlyTbv4&t` \n**Life of Boris** - `https://www.youtube.com/channel/UCS5tt2z_DFvG7-39J3aE-bQ` - _Makes voice over for hardbass._ \n**Mordi Slav** - `https://www.youtube.com/channel/UCfm_yxHLskcYdMTLgJxV1dw` \n**Mr. Ramix Hardbas** - `https://www.youtube.com/channel/UCv_FWmHXV1Xo6fTeycT2z8A` \n**Professional Gopnik** - `https://www.youtube.com/channel/UCEwi03WbZcVwHr8vXZt0V-A` \n**SrpskiBass** - `https://www.youtube.com/channel/UCAFz3fH8jQXIbU-7LzYo_XQ` \n**STARSLAV** - `https://www.youtube.com/channel/UCgIKR-NIbODHQJSn1rIiQQw` \n**uamee** - `https://www.youtube.com/channel/UC7A3-bBLEXQKTYpH-sYQFJA` \n**XS Project** - `https://www.youtube.com/channel/UCvFIQiPVy1BbIuxQ9LAh03A` \n**If you are a hardbasscreator but not in this list, contact ZWEKKERBOY.**"

HARDBASSCREATORS = ['ADIES LAD','APARTJE.','BANDITHEDOGE MUSIC','DAVAY','DJ CZECH SLAV','DJ DONK','DJ NEXEUZ','DJ PUMP','DJ SLAVBROTHER','DJ TOTZI','EARSLAV','EXODUS','GOPNIK MCBLYAT','HARD BASS SCHOOL','JANDY','KROVJAZNIK',"LEY O'LANTERN",'LIFE OF BORIS','MORDI SLAV','MR. RAMIX HARDBASS','PROFESSIONAL GOPNIK','SRPSKIBASS','STARSLAV','UAMEE','XS PROJECT']
HardbassCreators = ['Adies Lad','apartje.','bandithedoge music','Davay','DJ Czech Slav','DJ Donk','DJ Nexeuz','DJ PUMP','DJ SlavBrother','DJ TOTZI','EarSlav','Exodus','Gopnik McBlyat','HARD BASS SCHOOL','Jandy','Krovjaznik',"Ley o'Lantern",'Life of Boris','Mordi Slav','Mr. Ramix Hardbass','Professional Gopnik','SrpskiBass','STARSLAV','uamee','XS Project']

HardbassCreatorPage = { 'Adies Lad':"**Adies Lad**\nHardbass creator.\n\n**Adies Lad Links**\nYouTube - https://www.youtube.com/channel/UCZvjPWODsHYX5_Y7iCmz-9g\nSoundcloud - https://soundcloud.com/user-755112819\nFacebook - https://www.facebook.com/adi.lad.31542\n\n**Adies Lad Discord**\nAdies#7250\n\n**Adies Lad Top Rated**\n- Adies Lad  - Squat Party https://youtu.be/emiBAltrIKo\n- Adies Lad - Istrebitel https://www.youtube.com/watch?v=uYSZaCI21R8\n- Adies Lad - Grizzli https://www.youtube.com/watch?v=Igup5J7CMZg\n",
                        'apartje.': "**apartje.**\nYoutube meme maker from Germany that brought us Cheeki Breeki hardbass. Unfortunatelly he never finished cheeki breeki hardbass 2 because he died from a heroin overdosis. apartje. you are missed. \n\n**apartje. Links**\nYouTube: https://www.youtube.com/channel/UCgL9Kp942itDl4D1Sa9mSOQ\n \n **apartje. Top Rated**\n- apartje. - Cheeki Breeki Hardbass Anthem https://www.youtube.com/watch?v=BnTW6fZz-1E\n- apartje. - Cheeki Breeki Hardbass 2 https://www.youtube.com/watch?v=A2udLGQ58qQ",
                        'banditthedoge music':'**bandithedoge music** \nHardbass producer from Poland. \n \n**bandithedoge music Links** \nYouTube - https://www.youtube.com/channel/UCMosYVHeaPgJ14Sd-qEubzg \nSpotify - https://open.spotify.com/artist/3UnMO5XA2BLnvpeSckNPSu \nSoundcloud - https://soundcloud.com/bandithedoge \n Bandcamp - https://bandithedoge.bandcamp.com/ \nPatreon - https://www.patreon.com/bandithedoge  \n\n**bandithedoge music Discord** \nbandithedoge#7040  \n\n**bandithedoge music Top Rated** \n- bandithedoge music - UTC+3 https://www.youtube.com/watch?v=5A5qRMs5Tn8 \n- bandithedoge music - Rostok https://www.youtube.com/watch?v=85ZDskfzsS0 \n- bandithedoge music - Hard in the Style https://www.youtube.com/watch?v=QmPCaDDiax4',
                        'Davay':"**Davay**\nDavay is the hardbass producer who gave us tri poloski.\n\n**Davay Links**\nYouTube - https://www.youtube.com/channel/UCjoGMIUWUxozeINn6eJJQqA\nSpotify - https://open.spotify.com/artist/3E51y3Ff8aURnyOkaxDXKS\nFaceBook - https://www.facebook.com/davaystyle\nInstagram - https://www.instagram.com/davaystyle/\n\n**Davay Top Rated**\n- Davay - Tri Poloski https://www.youtube.com/watch?v=QiFBgtgUtfw\n- Davay - Op Davay https://www.youtube.com/watch?v=YTTfXNj4bPc\n- Davay - La Bamba https://www.youtube.com/watch?v=wmR51pe222o\n",
                        'DJ Czech Slav':"**DJ Czech Slav**\nHardbass creator from Czech Republic. Hardbass & Vodka are the best things ever!\n\n**DJ Czech Slav Links**\nYouTube - https://www.youube.com/channel/UCBEw_pXwlO13nN1RjLjoGpQ\nFacebook - https://www.facebook.com/DjCzechSlav/\nInstagram - https://www.instagram.com/dj_czech_sla/\n\n**DJ Czech Slav Top Rated**\n- DJ Czech Slav - Czechia at night Ft. TOTZI https://www.youtube.com/watch?v=ioxGjZfz7ak\n- DJ Czech Slav - Slavic https://www.youtube.com/watch?v=9us31HtQ7u0\n- Dj Czech Slav - Ikealand https://www.youtube.com/watch?v=gezy4ZlmqOI\n",
                        'DJ Donk':"**DJ Donk**\nHardbass producer from Russia. Legend believes that he actually lives in Chernobyl, Ukraine. \n\n**DJ Donk Links**\nYouTube  - https://www.youtube.com/channel/UC9E8vdJDo24V0foxR-Z12Ig\nSoundcloud - https://soundcloud.com/dj-slavibass\n\n**DJ Donk Discord**\nDJ Donk_Official#3442\n\n**DJ Donk Top Rated**\n- DJ Donk - Ras, ras, pidaras https://www.youtube.com/watch?v=46k3HVvELxU\n- DJ Donk - Gopniks In Reactor 4 https://www.youtube.com/watch?v=xYs6mHRWh24\n- DJ Donk - Wez Pigulke https://www.youtube.com/watch?v=jeSc0_XUDIQ\n",
                        'DJ Frank':"**DJ Frank**\nPolish hardbass producer who also posts videos about software tutorials and memes.\n\n**DJ Frank Links**\nYouTube - https://www.youtube.com/channel/UCibhg2m_-DNkjN3sDYlG2Uw\nSpotify - https://open.spotify.com/artist/6Ojx68shhAYbpquOQ8p2Bp\nSoundcloud - https://soundcloud.com/dj-frank-2k\nInstagram - https://www.instagram.com/dj_frank_2k/?hl=en\n\n**DJ Frank Discord**\nDJ Frank#5055\nhttps://discordapp.com/invite/tWx2Nd8\n\n**DJ Frank Top Rated**\n- DJ Frank - Wist 94 (feat. Krovjaznik) https://www.youtube.com/watch?v=B1H6lNrwmOY\n- DJ Frank - Reactor 4 https://www.youtube.com/watch?v=RnTFa6dRDlY\n- DJ Frank - Counter Pump (feat. Earslav) https://www.youtube.com/watch?v=I6DpFxbI5Bs\n",
                        'DJ Nexeuz':"**DJ Nexeuz**\nHeavy hardbass from Poland for all gopniks. \n\n**DJ Nexeuz Links**\nYouTube - https://www.youtube.com/channel/UC99eeiqR9IN1rFxW437YwIg\nFacebook - https://www.facebook.com/DJ-Nexeuz-380446195761068/\nSoundcloud - https://soundcloud.com/nexeuz-95\n\n**DJ Nexeuz Top Rated**\n- DJ Nexeuz x DJ Donk - Blinchiki Babushki https://www.youtube.com/watch?v=HUw6JTwk-mI\n- DJ Nexeuz - Fiat 126p https://www.youtube.com/watch?v=XsGrRZJ2ZGw\n- DJ Nexeuz - Semki https://www.youtube.com/watch?v=UMTkZ80vpQU\n",
                        'DJ PUMP':"**DJ PUMP**\nHi! I am DJ Pump a finnish wannabe producer! I make hardbass.\n\n**DJ PUMP Links**\nYouTube - https://www.youtube.com/channel/UCZjxTFvOYgiLBs_t3UcFpnw\n\n**DJ PUMP Discord**\nFinnish_Pump88#5529\n\n**DJ PUMP Top Rated**\n- DJ PUMP - Daruda Sandstorm Remix https://www.youtube.com/watch?v=ma9e2gdTpn4\n- DJ PUMP - Doki doki hardbass club https://www.youtube.com/watch?v=deADrXLROjI\n- DJ PUMP - katyusha hardbass https://www.youtube.com/watch?v=0GT2g7Ux16g\n",
                        'DJ SlavBrother':"**DJ SlavBrother**\nProffesional hardbass lover and beginning hardbass producer from SRBIJA BRE!\n\n**DJ SlavBrother Links**\nYoutube - https://www.youtube.com/channel/UCKcRPvQrb_hdjOc7OBqCMlw\n\n**DJ SlavBrother Discord**\nDj SlavBrother -Official-#5598\nhttps://discord.gg/MTXS4J2\n\n**DJ SlavBrother Top Rated**\nDJ SlavBrother - Night in Srbija https://www.youtube.com/watch?v=761b4F1qOpk\nDJ SlavBrother - HardBass from Tarkov https://www.youtube.com/watch?v=LEyvQ8smWA0\nDJ SlavBrother - Holy Slav https://www.youtube.com/watch?v=V3lZKBHCMds\n",
                        'DJ Totzi':"**DJ Totzi**\nStarted making hardbass at 22 may 2018. \n\n**DJ Totzi Links**\nYouTube - https://www.youtube.com/channel/UCrZ9kx-C9lb38rIUsFDU4Tg/featured\nGoogle+ - https://plus.google.com/u/0/117361815383983149943\n\n**DJ Totzi Top rated**\n- DJ Totzi - Hiroshima\nhttps://www.youtube.com/watch?v=yjKlBw09lO0\n- DJ Totzi - Gulag Master\nhttps://www.youtube.com/watch?v=8QF7Byjli7k\n-DJ Totzi - Hardbass Attack \nhttps://www.youtube.com/watch?v=pUGpEaISwfo\n",
                        'EarSlav':"**EarSlav**\nLives in Omsk, Russia and started publishing hardbass on YouTube at 25 may 2018. \n\n**EarSlav Links**\nYouTube  - https://www.youtube.com/channel/UCNrXk1ugexWqv7AFD7LLkNQ\nVk - https://vk.com/chernyhkonstant\nSoundcloud - https://soundcloud.com/earslav\n\n**EarSlav Discord**\nEarSlav#3381\n\n**Earslav Top Rated**\n- EarSlav - Russian Fun https://www.youtube.com/watch?v=w-Fkv0_TUiw\n- EarSlav - Dacha https://www.youtube.com/watch?v=IhU3puyEc1w\n- EarSlav - I AM SLAV https://www.youtube.com/watch?v=9yiDioGMY84\n",
                        'Gopnik McBlyat':"**Gopnik McBlyat**\nGopnik from Lublin, a city in eastern Poland. Keeping it Cheeki Breeki since 2016!\n\n**Gopnik McBlyat Links**\nYouTube - https://www.youtube.com/channel/UCusaOYfkki9drs2eIfRZGfQ\nSoundcloud - https://soundcloud.com/gopnikmcblyat\nBandcamp - https://gopnikmcblyat.bandcamp.com/\nFacebook - https://www.facebook.com/GopnikMcBlyat\n\n**Gopnik McBlyat Top Rated**\n- Gopnik McBlyat - Snakes in Tracksuits https://www.youtube.com/watch?v=LEjqfOKiGWE\n- Gopnik McBlyat - Cheeki Breeki Revolt https://www.youtube.com/watch?v=qQvwxmsRM64\n- Gopnik McBlyat - Szpion Detector https://www.youtube.com/watch?v=7qC2vAqTE2E\n",
                        'HARD BASS SCHOOL':"**HARD BASS SCHOOL**\nThe name of the music producers Pavel Zhukov and Val’ Toletov.\n\n**HARD BASS SCHOOL Links**\nYouTube - https://www.youtube.com/hardbassschool/\nSpotify - https://open.spotify.com/artist/5H8ZNi2r1xkfNC3HRkoOmZ\nSoundcloud - https://soundcloud.com/hard-bass-school\nVk - https://vk.com/hbs_official\nFacebook - https://www.facebook.com/hbsoriginal/\nInstagram - https://www.instagram.com/hardbassschool/\n\n**HARD BASS SCHOOL Top Rated**\n- HARD BASS SCHOOL - Narkotik Kal https://www.youtube.com/watch?v=KofvVAo4_0o\n- HARD BASS SCHOOL - Slav https://www.youtube.com/watch?v=nraKxjjY2Ks\n- HARD BASS SCHOOL - Opa Bila https://www.youtube.com/watch?v=XveHckJdYvY\n",
                        'Jandy':"**Jandy**\nHardbass creator.\n\n**Jandy Links**\nYouTube - https://www.youtube.com/user/JandyCZ\nGoogle+ - https://plus.google.com/u/0/111761705257612078957\n\n**Jandy Top Rated**\n- Jandy - Spuki House (feat. uamee) https://www.youtube.com/watch?v=a3EGujAgZOw\n- Jandy - Eardrum Pain https://www.youtube.com/watch?v=jdsFwMoUI3E\n- Jandy - Pitchovole https://www.youtube.com/watch?v=Ok-64FP60_w\n",
                        'Krovjaznik':"**Krovjaznik**\nProducing hardbass from Latvia and spreading slav idea! Use my music as much as you wish! Now let's have some cheeki breeki!\n\n** Krovjaznik Links**\nYouTube - https://www.youtube.com/channel/UCLIWsAUiWvqtHhPOHq0BGbQ/\nSpotify - https://open.spotify.com/artist/2qQFngHgYDE0o8oha35mDq\nSoundcloud - https://soundcloud.com/krovjaznik\nBandcamp - https://krovjaznik.bandcamp.com/\nFacebook - https://www.facebook.com/Krovjaznik/\nTwitter - https://twitter.com/krovjaznik\n\n**Krovjaznik Top Rated**\n- Krovjaznik - DOSTOYEVSKY https://www.youtube.com/watch?v=CVEYkvR8mho\n- Krovjaznik - LATVIA https://www.youtube.com/watch?v=x8K6KYMcpUg\n- Krovjaznik - GARNIZON\nhttps://www.youtube.com/watch?v=NxeWOI9Uqkw\n",
                        "Ley o'Lantern":"**Ley o'Lantern**\nHello I am Ley and I make hardbass.\n\n**Ley o'Lantern Links**\nYouTube - https://www.youtube.com/channel/UChxHRCH_PNe_bg9_PjCLqOg\nSoundcloud - https://soundcloud.com/leyolantern\n\n**Ley o'Lantern Discord**\nLeyOLantern#5734\n\n**Ley o'Lantern Top Rated**\n- Ley o'Lantern - Pancake Pump https://www.youtube.com/watch?v=Yr4sKlyTbv4\n- Ley o'Lantern - Master Gopnik https://soundcloud.com/leyolantern/master-gopnik\n- Lost Project: Ley o'Lantern - Semkibae https://soundcloud.com/leyolantern/lost-project-semkibae\n",
                        "Life of Boris":"**Life of Boris**\nThe glorious Shashlik King who has been uniting slavs since 2015. He does voiceover for hardbass.\n\n**Life of Boris Links**\nYouTube - https://www.youtube.com/user/NocturnoPlays\nVk - https://vk.com/theborislife\nFacebook - https://www.facebook.com/TheBorisLife/\nInstagram - https://www.instagram.com/the_life_of_boris\nTwitter - https://twitter.com/life_of_boris\nReddit - https://www.reddit.com/user/life_of_boris\nSteam - https://steamcommunity.com/id/life_of_boris/\nSteam group - https://steamcommunity.com/groups/life_of_boris\nPatreon - https://www.patreon.com/lifeofboris/memberships\n\n**Life of Boris Top Rated**\n- Life of Boris - How to squat like Slav https://www.youtube.com/watch?v=2-8gsWZqDBM\n- Life of Boris - How to Slav your car https://www.youtube.com/watch?v=K9CgSjQDAvE\n- Life of Boris - Cheeki Breeki Hardbass https://www.youtube.com/watch?v=rEckY-TUv9I\n",
                        "Mordi Slav":"**Mordi Slav**\nSlavic Hardbass is never about technique or skills, it's about FEELING. Mordi Slav is a 14 year old Hardbass producer from Slovakia doing his hobby, and chillin' like a slav.\n\n**Mordi Slav Links**\nYouTube - https://www.youtube.com/channel/UCfm_yxHLskcYdMTLgJxV1dw\nBandcamp - https://mordislovakian.bandcamp.com\nPatreon - https://www.patreon.com/MordiSlav\n\n**Mordi Slav Discord**\nMordi#6503\n\n**Mordi Slav Top Rated**\n- Mordi a Krovjaznik - PERVOJE MAJA https://www.youtube.com/watch?v=ycEeh2g1C4o\n- Mordi - DONBASS https://www.youtube.com/watch?v=OPHqgWmokdA\n- Mordi - PANELNIY https://www.youtube.com/watch?v=jdn2jiaS_K0\n",
                        "Mr. Ramix Hardbas":"**Mr. Ramix Hardbas**\nThe producer who's going to make the most gopniks and gopnitsas happy with his music.\n\n**Mr. Ramix Hardbas Links**\nYouTube - https://www.youtube.com/channel/UCv_FWmHXV1Xo6fTeycT2z8A\n\n**Mr. Ramix Hardbas Top Rated**\n- Mr. Ramix Hardbas - Semki Nation https://www.youtube.com/watch?v=blgimA-lDhA\n- Mr. Ramix Hardbas - Anatoly https://www.youtube.com/watch?v=YzXetUBXwzM\n- Mr. Ramix Hardbas - Molotov https://www.youtube.com/watch?v=4O188dQkNv8\n",
                        "Professional Gopnik":"**Professional Gopnik**\nYoutube's professional official hardbass approver. Beginner producer from Latvia.\n\n**Professional Gopnik Links**\nYouTube - https://www.youtube.com/channel/UCEwi03WbZcVwHr8vXZt0V-A\nSpotify - https://open.spotify.com/artist/6Fi9cmxy8qntuMgLiPxVHj?si=Nc0-tEOMQZuYw2Zbf0nf7Q\nSoundcloud - https://soundcloud.com/user-276399497\nFacebook - https://www.facebook.com/ProfessionalGopnik/\nInstagram - https://www.instagram.com/professionalgopnikofficial/\nTwitter - https://twitter.com/ProfessionalGop\nTwitch - https://www.twitch.tv/professional_gopnik\nSteam - https://steamcommunity.com/profiles/76561193825761396\nSteam group - http://steamcommunity.com/groups/ProfessionalGopnikOfficial\nPatreon - https://www.patreon.com/Progop\n\n**Professional Gopnik Discord**\nProfessional Gopnik#4255\nhttps://discord.gg/8j4dN2s\n\n**Professional Gopnik Top Rated**\n- Professional Gopnik - Soyuz feat. Krovjaznik https://www.youtube.com/watch?v=TrfvS0Bg50A\n- Professional Gopnik - LATVIA IS NUMBER ONE feat. Krovjaznik\nhttps://www.youtube.com/watch?v=3O9et1DAj7s\n- Professional Gopnik - Moskvich\nhttps://www.youtube.com/watch?v=1IAbKJh5Irk\n",
                        "SrpskiBass":"**SrpskiBass**\nYoung Hardbass producer from Serbia.\n\n**SrpskiBass Links**\nYouTube - https://www.youtube.com/channel/UCAFz3fH8jQXIbU-7LzYo_XQ\nSpotify - https://open.spotify.com/artist/5cV0edMqnNvu9nGnVUJGMA\nSoundcloud - https://soundcloud.com/srpskibass\nBandcamp - https://srpskibass.bandcamp.com/\nVk - https://vk.com/srpskibass\nFacebook - https://www.facebook.com/srpskibass69/\nInstagram - https://www.instagram.com/srpskibass/\nTwitter - https://twitter.com/SrpskiBass\nSteam - https://steamcommunity.com/id/srpskibass/\n\n**SrpskiBass Discord**\nSrpskiBass#0769\nhttps://discord.gg/47xYTPH\n\n**SrpskiBass Top Rated**\n- SrpskiBass - Gopnik Refugee https://www.youtube.com/watch?v=p7a7VG2Ob18\n- SrpskiBass - Meanwhile In The Reactor https://www.youtube.com/watch?v=CotkKTlfCJA\n- SrpskiBass - SlavBass https://www.youtube.com/watch?v=lOq5bPkauLY\n",
                        "STARSLAV":"**STARSLAV**\nSTARSLAV who’s name is Max is a 21 Years old Hardbass producer and content creator.\n\n**STARSLAV Links**\nYouTube - https://www.youtube.com/STARSLAV\nSpotify - https://open.spotify.com/artist/2IUDbfpHOHsFeGqcwe3XvU?si=AzAmI-xITk6tpIR2Y6GfTA\nInstagram - https://www.instagram.com/starslavhardbass/\n\n**STARSLAV Discord**\nDiscord name - Starslav#9815\n\n**STARSLAV Top Rated**\n- Starslav - OPA https://www.youtube.com/watch?v=VoCgT9GCoEo\n- Starslav - adiblyat https://www.youtube.com/watch?v=Af9WN3yt9S8\n- Starslav - Idi Nahui Ft. Anomaly https://www.youtube.com/watch?v=4DGBX1ItPT0\n",
                        "uamee":"**uamee**\nTop quality hardbass from your favourite hardbass producer, uamee! Squat 'till you bleed!\n\n**uamee Links**\nYouTube - https://www.youtube.com/channel/UC7A3-bBLEXQKTYpH-sYQFJA\nSpotify - https://open.spotify.com/artist/1zBfiaC9hWHLUDZrbWm5FH\nFacebook - https://www.facebook.com/uameeYT/\nInstagram - https://www.instagram.com/uameeyt/\nBandcamp - http://uamee.bandcamp.com/\nSoundcloud - https://soundcloud.com/uamee\nPatreon - https://www.patreon.com/uamee\n\n**uamee Discord**\nDiscord name - uamee#8055\nhttps://discord.gg/MBWFUrG\n\n**uamee Top Rated**\n- uamee - HALVA https://www.youtube.com/watch?v=oLoT0dm88zU\n- uamee - SMASHED IN WARSAW https://www.youtube.com/watch?v=nACEGWfjxhM\n- uamee - MOSIN https://www.youtube.com/watch?v=okV53tw97jQ\n",
                        "XS Project":"**XS Project**\nHardbass group founded in 2002 by two Russian producers Levon and Andrey.\n\n**XS Project Links**\nYouTube - https://www.youtube.com/user/MrXSproject\nSpotify - https://open.spotify.com/artist/7FSj8kD4474FKP2gYjZPos\nSoundcloud - https://soundcloud.com/xsproject\nVk - https://vk.com/xsproject2\nFacebook - https://www.facebook.com/xsprojectOfficial\nInstagram - https://www.instagram.com/xsproject/\nTwitter - https://twitter.com/xsproj\nPatreon - https://www.patreon.com/xsproject/memberships\n\n**XS Project Top Rated**\n- XS Project - Vodovorot https://www.youtube.com/watch?v=2Y3xSv5Cs6U\n- XS Project - Narkobaron https://www.youtube.com/watch?v=61fVT7aiR0A\n- XS Project - Bochka, Bass, Kolbaser https://www.youtube.com/watch?v=r5uzc3U8Qhc\n"
                       }

#The lists for HARDBASS commands
randomhardbassblyat = ['https://www.youtube.com/watch?v=hV-AyjRDZek%22%22', 'https://www.youtube.com/watch?v=7kiNUCkB1PU', 'https://www.youtube.com/watch?v=fro6je9L5kg', 'https://www.youtube.com/watch?v=qfxNrOZqc3A', 'https://www.youtube.com/watch?v=BnTW6fZz-1E', 'https://www.youtube.com/watch?v=QIjKijhv1OU', 'https://www.youtube.com/watch?v=q3sOu52Uk_M', 'https://www.youtube.com/watch?v=2tch4J_pP9o', 'https://www.youtube.com/watch?v=fksEkuGPXzI', 'https://www.youtube.com/watch?v=ze_94FDyzPw', 'https://www.youtube.com/watch?v=4xei2-cW9eo', 'https://www.youtube.com/watch?v=G0VMbbuqeNc']
playlistlink = "https://www.youtube.com/playlist?list=PLhx1osf4RTuLCsfHkC_GkBSC0DXozTPLI&jct=V-35t7bcjMQZ2Pp9Imox-rjqDBODYw&disable_polymer=true"

#Help message variable
HelpBlyat = ":regional_indicator_g: :regional_indicator_o: :regional_indicator_p: :regional_indicator_b: :regional_indicator_o: :regional_indicator_t:\n\n**INFORMATION**\nThe GOPBOT is ready to squat down, drink and have some fun. It can do some cheeki breeki commands and welcomes you the slav way!\n\n**COMMANDS**\n**`GOPBOT Help`** - Gives you the information and commands.\n**`GOPBOT Credits`** - Shows all the credits for the making of GOPBOT.\n\n**`GOPBOT Code`** - Gives you a sheet of the code, it’s not always up to date.\n**`GOPBOT Playing`** - Admin command to change what the bot is playing.\n**`GOPBOT Testbot`** - Just a command to get to know if the bot is working fine.\n\n**`GOPBOT Playhardbassblyat `** - Gets you a random hardbass video.\n**`GOPBOT Playlist`** - Gets you a hardbass playlist.\n\n**`GOPBOT Country`** - Gets you a list of Slavic and Baltic countries.\n\n**`GOPBOT Hardbass Creators`** - A list of all hardbass creators.\n**`GOPBOT Hardbass Creator Check - {name of the hardbass creator}`** - Check if someone is a hardbass creator or not.\n**`GOPBOT Hardbass Creator Page - {name of the hardbass creator}`** - A page of the hardbass creator with all information.\n\n**`Cyka `** - BLYAT!\n**`Kurwa `** - MAÇ!\n**`Idi `** - NAHUI!\n**`Vodka `** - Makes the bot go crazy.\n\n**WELCOME**\nTo get GOPBOT welcoming slavs the slavic way, you need a textchannel named ‘welcome’  where it has the rights to send messages!\n\n**Thank you for using GOPBOT. Stalin would be proud of you!**"

#Slav country variable
GOPBOTcountry = "**SLAVIC COUNTRIES**\n:flag_by:  `Belarus`\n:flag_ba:  `Bosnia and Herzegovina`\n:flag_bg:  `Bulgaria`\n:flag_hr:  `Croatia`\n:flag_cz:  `Czech Republic`\n:flag_mk:  `Macedonia`\n:flag_me:  `Montenegro`\n:flag_pl:  `Poland`\n:flag_ru:  `Russia`\n:flag_rs:  `Serbia`\n:flag_sk:  `Slovakia`\n:flag_si:  `Slovenia`\n:flag_ua:  `Ukraine`\n\n **BALTIC COUNTRIES**\n:flag_ee:  `Estonia`\n:flag_lv:  `Latvia`\n:flag_lt:  `Lithuania`\n\n_If your country is not in this list it doesn’t matter blyat. Just spread the culture of Cheeki Breeki!_"

#GOPBOT ready for action
@gopbot.event
async def on_ready():
    print ("Ready to squat down, drink and have some fun. ")
    print (gopbot.user.name)
    print (gopbot.user.id)
    print("=============================================")


#@gopbot.event
#async def on_member_join(member):
#    for channel in member.server.channels:
#        if channel.name == 'general':
#            await gopbot.send_message(channel, '{} just arrived. Mama get the kompot!'.format(member.mention))

#GOPBOT welcome            
@gopbot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'welcome':
            name = format(member.mention)
            RandomWelcome = ['Welcome ' + name + ', leave your weapons by the door.' ,'Papa Stalin would be proud of ' + name + '.' ,'Work harder ' + name + '!' ,'Do not Gopstop ' + name + ' yet!' ,'' + name + ' is here to start war and eat semechki. ' + name + ' is all out of semechki.' ,'Rush B ' + name + '!' ,'' + name + ' entered the zone!' ,'' + name + ' is sweet as babushkas kompot.' ,'A slavic ' + name + ' appeared.' ,'' + name + ' don’t let the KGB get you!' ,'' + name + ' joined, pretend like your working!' ,'' + name + ' escaped from Gulag by arriving here!' ,'' + name + ' is not Gullaged yet!' ,'Drink and have some fun ' + name + '!' ,'' + name + ' just arrived. Mama get the kompot!' ,'' + name + ' just became a comrade!' ,'' + name + ' became a true Gopnik' ,'Blyat, welcome to Russia ' + name + '!' ,'' + name + ' sneaked in with the tactics of sneeki breeki!' ,'' + name + ' I hope you brought some semechki and pivo with you, Welcome comrade!' ,'Congrats!!! You are now a true comrade, ' + name + '!!!' ,'Motherland welcomes you,  ' + name + '!' ,'Don’t forget your protivogaz,  ' + name + '!' ,'Welcome ' + name + ', hope you are prepared for some cheeki breeki!!!' ,'Cyka blyat! You scared me... Welcome  ' + name + '!']
            await gopbot.send_message(channel, "%(welcome)s" % {'welcome' : random.choice(RandomWelcome)})


    
#GOPBOT command handling   
@gopbot.event
async def on_message(message):
    #Cyka - BLYAT!
    if message.content.upper() == 'CYKA':
                 GopnikID = message.author.id
                 await gopbot.send_message(message.channel, "<@%s> BLYAT " % (GopnikID))

    #Idi - NAHUI!
    if message.content.upper() == 'IDI':
                 GopnikID = message.author.id
                 await gopbot.send_message(message.channel, "<@%s>  NAHUI " % (GopnikID))

    #Kurwa - MAÇ!
    if message.content.upper() == 'KURWA':
                 GopnikID = message.author.id
                 await gopbot.send_message(message.channel, "<@%s>  MAÇ " % (GopnikID))
        

    #PLAYHARDBASSBLYAT - Gets you a random hardbass video.
    if message.content.upper().startswith ('GOPBOT PLAYHARDBASSBLYAT'):
                await gopbot.send_message(message.channel, "CYKA LISIN TO THIS! \n%(hardbass)s" % {'hardbass' : random.choice(randomhardbassblyat)})

    #PLAYLIST - Gets you a hardbass playlist.
    if message.content.upper().startswith ('GOPBOT PLAYLIST'):
                await gopbot.send_message(message.channel, "The bot is starting playlist...")
                await gopbot.send_message(message.channel, " %(s)s" % {'s' : playlistlink })


    #Country - Gets you a list of Slavic countries 
    if message.content.upper().startswith ('GOPBOT COUNTRY') or message.content.upper().startswith ('GOPBOT COUNTRIES'):
                await gopbot.send_message(message.channel, GOPBOTcountry)

    #Vodka - Makes the bot go crazy.
    if message.content.upper() == "VODKA":
                await gopbot.send_message(message.channel, "WHERE THE BLYAT IS MY VODKA?!")

    #YO MOM GEY - No u.
    if message.content.upper() == "GOPBOT YO MOM GEY":
                
                await gopbot.send_message(message.channel, "No u.")


    #Hardbass creators - Gets you a list of Hardbass creators 
    if message.content.upper() == 'GOPBOT HARDBASS CREATORS' or message.content.upper() == 'GOPBOT HARDBASS CREATOR' or message.content.upper() == 'GOPBOT HARDBASSCREATORS' or message.content.upper() == 'GOPBOT HARDBASSCREATOR':
                await gopbot.send_message(message.channel, HardbassCreatorsList1)
                await gopbot.send_message(message.channel, HardbassCreatorsList2)

    #Hardbass creator - Check if someone is a hardbass creator or not.        
    if message.content.upper().startswith("GOPBOT HARDBASS CREATORS CHECK")  or message.content.upper().startswith ('GOPBOT HARDBASS CREATOR CHECK') or message.content.upper().startswith ('GOPBOT HARDBASSCREATORS CHECK') or message.content.upper().startswith ('GOPBOT HARDBASSCREATOR CHECK'):
                Vodka = message.content.split("-")
                if len(Vodka) > 1:
                        Vodka2 = ''.join(Vodka[1]).strip()
                        Vodka3 = Vodka2.upper()
                        if Vodka3 in HARDBASSCREATORS:
                                Vodka4 = (HARDBASSCREATORS.index(Vodka3))
                                await gopbot.send_message(message.channel,''.join(HardbassCreators[Vodka4]) )

                                await gopbot.send_message(message.channel, "Yes comrade! " + ''.join(HardbassCreators[Vodka4]) + " has good hardbass blyat!")
                        else:
                                await gopbot.send_message(message.channel, "No cyka! This is western spy shit!")
                else:
                                await gopbot.send_message(message.channel, "You need to use the command like this: 'GOPBOT HARDBASS CREATOR CHECK - {Creator}'")

    #Hardbass creator page - Gets you a page of the hardbass creator. 
    if message.content.upper().startswith("GOPBOT HARDBASS CREATORS PAGE")  or message.content.upper().startswith ('GOPBOT HARDBASS CREATOR PAGE') or message.content.upper().startswith ('GOPBOT HARDBASSCREATORS PAGE') or message.content.upper().startswith ('GOPBOT HARDBASSCREATOR PAGE'):
                Vodka = message.content.split("-")
                if len(Vodka) > 1:
                        Vodka2 = ''.join(Vodka[1]).strip()
                        Vodka3 = Vodka2.upper()
                        if Vodka3 in HARDBASSCREATORS:
                                Vodka4 = (HARDBASSCREATORS.index(Vodka3))

                                await gopbot.send_message(message.channel, HardbassCreatorPage[''.join(HardbassCreators[Vodka4])])
                        else:
                                await gopbot.send_message(message.channel, "Cyka! We can't find this creator blyat! This might be Western pig music! You are sure you typed well or you want to go to Gulag?")



    #CODE - Gives you a sheet of the code, it’s not always up to date.
    if message.content.upper().startswith ("GOPBOT CODE"):
                await gopbot.send_message(message.channel, "This is the code for the GOPBOT: \n%(URL)s" % {'URL' : "https://docs.google.com/document/d/1SEzU0vYVxPrmO_PdHZXQjMMMCUQT9jHd4_kgovS0k1k/edit?usp=sharing"})

    #!CREDITS - Shows all the credits for the making of GOPBOT.
    if message.content.upper().startswith ("GOPBOT CREDITS") or message.content.upper().startswith ("GOPBOT CREDIT"):
                await gopbot.send_message(message.channel, ":regional_indicator_g: :regional_indicator_o: :regional_indicator_p: :regional_indicator_b: :regional_indicator_o: :regional_indicator_t:\n\n**Coded by:** @ZWEKKERBOY#2931\n**Developed by:** @CRO-Thehacker#7928, @laojinTheCaesium#6577 & @spooki uamee#1139\n**Tested by:** @Tovarisch NeoN#7364, @WeedIsLife#3286, @uncle_Миша#2403 & @LaugeJ8#6904\n**Hosted by:** @Kleine#6130 and Papa Putin\n**GOPBOT Profile picture by:** @LaugeJ8#6904")

    #Help - Gives you the information and commands.
    if message.content.upper().startswith ("GOPBOT HELP") or message.content.upper().startswith("GOPBOT INFORMATION") or message.content.upper() == "GOPBOT":
                await gopbot.send_message(message.channel, HelpBlyat)

    #!PLAYING - Admin command to change what the bot is playing.
    if message.content.upper().startswith ("GOPBOT PLAYING"):
        if message.author.id == ADMINidZWEK or message.author.id == ADMINidCRO or message.author.id == ADMINidKLEINE:
            activity = message.content[15:]
            print ("I'm now playing " + activity + " blyat!")
            await gopbot.change_presence(game=discord.Game(name=activity))
            await gopbot.send_message(message.channel, "I'm now playing " + activity + " blyat!")
        else:
            await gopbot.send_message(message.channel, "You western spy! Don't try to do a admin command! YOU ARE NOT STALIN!")


        
    #TESTBOT - Just a command to get to know if the bot is working fine.
    elif message.content.upper() == "GOPBOT TESTBOT":
                await gopbot.send_message(message.channel, "[  GOT INFO IN: 00.112 per/s  ]\n IP: 104.16.58.5\n Port: 443\n Protocol: HTTPS\n\n The server is going 100% cheeki breeki")
   
 #   elif message.content.upper() == "UPTIME":
#	            await gopbot.send_message(message.channel, " %s " % uptimeonserver())


    #Not used yet
#    if message.content.upper().startswith ('HELLO'):
#        args = message.content.split (" ")
#        await gopbot.send_message(message.channel, "%s" % (" ".join(args[1:]))

    if message.content.upper() == 'GOPBOT TIMEHELP':
                 GopnikID = message.author.id
                 await gopbot.send_message(message.channel, ":regional_indicator_w: :regional_indicator_h: :regional_indicator_a: :regional_indicator_s:  :regional_indicator_t: :regional_indicator_h: :regional_indicator_e: :regional_indicator_r: :regional_indicator_e:  :regional_indicator_t: :regional_indicator_i: :regional_indicator_m: :regional_indicator_e:\n Welcome to the WhatsTheTime Bot!\n\n TIMEHELP - List's help.\n TIMEIN - Tells user time in place.\n ")
    if message.content == 'GOPBOT TIMEIN USA':
                 GopnikID = message.author.id
                 await gopbot.send_message(message.channel, "TIME IN THE US :: HELP\n\n In the **USA** there are: **9** time zones.\n\n 1. The Atlantic standard time zone\n 2. The Eastern standard time zone\n 3. The Central standard time zone\n 4. The Mountain standard time zone\n 5. The Pacific standard time zone\n 6. The Alaska standard time zone\n 7. The Hawaii–Aleutian standard time zone\n 8. The Samoa standard time zone\n 9. The Chamorro standard time zone\n\n To list **USA** table do: TIMEIN USA {NAME OF TIME ZONE}")

    if message.content == 'GOPBOT TIMEIN USA TABLE':
                GopnikID = message.author.id
                await gopbot.send_message(message.channel, "**USA TIME TABLE**\n\n **Standard time and daylight saving time**\n\n `Hawaii–Aleutian Time Zone:`\n **HAST (UTC−10:00)** ,, **HADT (UTC−09:00)**\n DST's: Alaska, Hawaii (no DST)\n\n\n `Alaska Time Zone:`\n **AKST (UTC−09:00)** ,, **AKDT (UTC−08:00)**\n DST's: Alaska\n\n\n `Pacific Time Zone:`\n  **PST (UTC−08:00)** ,, **PDT (UTC−07:00)**\n DST's: California, Washington, Oregon, Nevada, Idaho\n\n\n `Mountain Time Zone:`\n **MST (UTC−07:00)** ,, **MDT (UTC−06:00)**\n DST's: Arizona (no DST outside of Navajo Nation), Colorado, Idaho, Kansas, Montana, Nebraska, New Mexico, North Dakota, Oregon, South Dakota, Texas, Utah, Wyoming\n\n\n `Central Time Zone:`\n **CST (UTC−06:00)** ,, **CDT (UTC−05:00)**\n DST's: Alabama, Arkansas, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Michigan, Minnesota, Mississippi, Missouri, Nebraska, North Dakota, Oklahoma, South Dakota, Tennessee, Texas, Wisconsin\n\n\n`Eastern Time Zone:` **EST (UTC−05:00)** ,, **EDT (UTC−04:00)**\n DST's: Alabama, Connecticut, Florida, District of Columbia, Delaware, Georgia, Indiana, Kentucky, Maine, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Maryland, Virginia, West Virginia")

    if message.content == 'GOPBOT TIMEIN Russia':
            GopnikID = message.author.id
            await gopbot.send_message(message.channel, '''	
**KALT**
`Kaliningrad Time:`
 	UTC+2
 	(MSK–1)
	
**MSK**
`Moscow Time:`
 	UTC+3
 	(MSK±0)
	
**SAMT**
`Samara Time:`
 	UTC+4
 	(MSK+1)
	
**YEKT**
`Yekaterinburg Time:`
	UTC+5
	(MSK+2)
	
**OMST**
`Omsk Time:`
	UTC+6
	(MSK+3)
 	
**KRAT**
`Krasnoyarsk Time:`
 	UTC+7
 	(MSK+4)
	
**IRKT**
`Irkutsk Time:`
	UTC+8
	(MSK+5)
	
**YAKT**
`Yakutsk Time:`
 	UTC+9
	(MSK+6)
	
**VLAT**
`Vladivostok Time:`
	UTC+10
	(MSK+7)
	
**MAGT**
`Magadan Time:`
 	UTC+11
 	(MSK+8)
**PETT**
`Kamchatka Time:`
	UTC+12
	(MSK+9)''')



#Get's the bot online!     
gopbot.run(Token)
