import random

GDNOON = [

    "`My wishes will always be with you, Morning wish to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good Afternoon Dear!`",

    "`With a deep blue sky over my head and a relaxing wind around me, the only thing I am missing right now is the company of you. I wish you a refreshing afternoon!`",

    "`The day has come a halt realizing that I am yet to wish you a great afternoon. My dear, if you thought you were forgotten, you’re so wrong. Good afternoon!`",

    "`Good afternoon! May the sweet peace be part of your heart today and always and there is life shining through your sigh. May you have much light and peace.`",

    "`With you, every part of a day is beautiful. I live every day to love you more than yesterday. Wishing you an enjoyable afternoon my love!`",

    "`This bright afternoon sun always reminds me of how you brighten my life with all the happiness. I miss you a lot this afternoon. Have a good time`!",

    "`Nature looks quieter and more beautiful at this time of the day! You really don’t want to miss the beauty of this time! Wishing you a happy afternoon!`",

    "`What a wonderful afternoon to finish you day with! I hope you’re having a great time sitting on your balcony, enjoying this afternoon beauty!`",

    "`I wish I were with you this time of the day. We hardly have a beautiful afternoon like this nowadays. Wishing you a peaceful afternoon!`",

    "`As you prepare yourself to wave goodbye to another wonderful day, I want you to know that, I am thinking of you all the time. Good afternoon!`",

    "`This afternoon is here to calm your dog-tired mind after a hectic day. Enjoy the blessings it offers you and be thankful always. Good afternoon!`",

    "`The gentle afternoon wind feels like a sweet hug from you. You are in my every thought in this wonderful afternoon. Hope you are enjoying the time!`",

    "`Wishing an amazingly good afternoon to the most beautiful soul I have ever met. I hope you are having a good time relaxing and enjoying the beauty of this time!`",

    "`Afternoon has come to indicate you, Half of your day’s work is over, Just another half a day to go, Be brisk and keep enjoying your works, Have a happy noon!`",

    "`Mornings are for starting a new work, Afternoons are for remembering, Evenings are for refreshing, Nights are for relaxing, So remember people, who are remembering you, Have a happy noon!`",

    "`If you feel tired and sleepy you could use a nap, you will see that it will help you recover your energy and feel much better to finish the day. Have a beautiful afternoon!`",

    "`Time to remember sweet persons in your life, I know I will be first on the list, Thanks for that, Good afternoon my dear!`",

    "`May this afternoon bring a lot of pleasant surprises for you and fills you heart with infinite joy. Wishing you a very warm and love filled afternoon!`",

    "`Good, better, best. Never let it rest. Til your good is better and your better is best. “Good Afternoon`”",

    "`May this beautiful afternoon fill your heart boundless happiness and gives you new hopes to start yours with. May you have lot of fun! Good afternoon dear!`",

    "`As the blazing sun slowly starts making its way to the west, I want you to know that this beautiful afternoon is here to bless your life with success and peace. Good afternoon!`",

    "`The deep blue sky of this bright afternoon reminds me of the deepness of your heart and the brightness of your soul. May you have a memorable afternoon!`",

    "`Your presence could make this afternoon much more pleasurable for me. Your company is what I cherish all the time. Good afternoon!`",

    "`A relaxing afternoon wind and the sweet pleasure of your company can make my day complete. Missing you so badly during this time of the day! Good afternoon!`",

    "`Wishing you an afternoon experience so sweet and pleasant that feel thankful to be alive today. May you have the best afternoon of your life today!`",

    "`My wishes will always be with you, Morning wi

sh to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good afternoon dear!`",

    "`Noon time – it’s time to have a little break, Take time to breathe the warmth of the sun, Who is shining up in between the clouds, Good afternoon!`",

    "`You are the cure that I need to take three times a day, in the morning, at the night and in the afternoon. I am missing you a lot right now. Good afternoon!`",

    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",

    "`I pray to god that he keeps me close to you so we can enjoy these beautiful afternoons together forever! Wishing you a good time this afternoon!`",

    "`You are every bit of special to me just like a relaxing afternoon is special after a toiling noon. Thinking of my special one in this special time of the day!`",

    "`May your Good afternoon be light, blessed, enlightened, productive and happy.`",

    "`Thinking of you is my most favorite hobby every afternoon. Your love is all I desire in life. Wishing my beloved an amazing afternoon!`",

    "`I have tasted things that are so sweet, heard words that are soothing to the soul, but comparing the joy that they both bring, I’ll rather choose to see a smile from your cheeks. You are sweet. I love you.`",

    "`How I wish the sun could obey me for a second, to stop its scorching ride on my angel. So sorry it will be hot there. Don’t worry, the evening will soon come. I love you.`",

    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",

    "`With you every day is my lucky day. So lucky being your love and don’t know what else to say. Morning night and noon, you make my day.`",

    "`Your love is sweeter than what I read in romantic novels and fulfilling more than I see in epic films. I couldn’t have been me, without you. Good afternoon honey, I love you!`",

    "`No matter what time of the day it is, No matter what I am doing, No matter what is right and what is wrong, I still remember you like this time, Good Afternoon!`",

    "`Things are changing. I see everything turning around for my favor. And the last time I checked, it’s courtesy of your love. 1000 kisses from me to you. I love you dearly and wishing you a very happy noon.`",

    "`You are sometimes my greatest weakness, you are sometimes my biggest strength. I do not have a lot of words to say but let you make sure, you make my day, Good Afternoon!`",

    "`Every afternoon is to remember the one whom my heart beats for. The one I live and sure can die for. Hope you doing good there my love. Missing your face.`",

    "`My love, I hope you are doing well at work and that you remember that I will be waiting for you at home with my arms open to pamper you and give you all my love. I wish you a good afternoon!`",

    "`Afternoons like this makes me think about you more. I desire so deeply to be with you in one of these afternoons just to tell you how much I love you. Good afternoon my love!`",

    "`My heart craves for your company all the time. A beautiful afternoon like this can be made more enjoyable if you just decide to spend it with me. Good afternoon!`",

]

GDNIGHT = [

    "`Good night keep your dreams alive`",

    "`Night, night, to a dear friend! May you sleep well!`",

    "`May the night fill with stars for you. May counting every one, give you contentment!`",

    "`Wishing you comfort, happiness, and a good night’s sleep!`",

    "`Now relax. The day is over. You did your best. And tomorrow you’ll do better. Good Night!`",

    "`Good night to a friend who is the best! Get your forty winks!`",

    "`May your pillow be soft, and your rest be long! Good night, friend!`",

    "`Let there be no troubles, dear friend! Have a Good Night!`",

    "`Rest soundly tonight, friend!`",

    "`Have the best night’s sleep, friend! Sleep well!`",

    "`Have a very, good night, friend! You are wonderful!`",

    "`Relaxa

tion is in order for you! Good night, friend!`",

    "`Good night. May you have sweet dreams tonight.`",

    "`Sleep well, dear friend and have sweet dreams.`",

    "`As we wait for a brand new day, good night and have beautiful dreams.`",

    "`Dear friend, I wish you a night of peace and bliss. Good night.`",

    "`Darkness cannot last forever. Keep the hope alive. Good night.`",

    "`By hook or crook you shall have sweet dreams tonight. Have a good night, buddy!`",

    "`Good night, my friend. I pray that the good Lord watches over you as you sleep. Sweet dreams.`",

    "`Good night, friend! May you be filled with tranquility!`",

    "`Wishing you a calm night, friend! I hope it is good!`",

    "`Wishing you a night where you can recharge for tomorrow!`",

    "`Slumber tonight, good friend, and feel well rested, tomorrow!`",

    "`Wishing my good friend relief from a hard day’s work! Good Night!`",

    "`Good night, friend! May you have silence for sleep!`",

    "`Sleep tonight, friend and be well! Know that you have done your very best today, and that you will do your very best, tomorrow!`",

    "`Friend, you do not hesitate to get things done! Take tonight to relax and do more, tomorrow!`",

    "`Friend, I want to remind you that your strong mind has brought you peace, before. May it do that again, tonight! May you hold acknowledgment of this with you!`",

    "`Wishing you a calm, night, friend! Hoping everything winds down to your liking and that the following day meets your standards!`",

    "`May the darkness of the night cloak you in a sleep that is sound and good! Dear friend, may this feeling carry you through the next day!`",

    "`Friend, may the quietude you experience tonight move you to have many more nights like it! May you find your peace and hold on to it!`",

    "`May there be no activity for you tonight, friend! May the rest that you have coming to you arrive swiftly! May the activity that you do tomorrow match your pace and be all of your own making!`",

    "`When the day is done, friend, may you know that you have done well! When you sleep tonight, friend, may you view all the you hope for, tomorrow!`",

    "`When everything is brought to a standstill, friend, I hope that your thoughts are good, as you drift to sleep! May those thoughts remain with you, during all of your days!`",

    "`Every day, you encourage me to do new things, friend! May tonight’s rest bring a new day that overflows with courage and exciting events!`",

]

PROGQUOTES = [

    "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.",

    "If debugging is the process of removing software bugs, then programming must be the process of putting them in.",

    "Measuring programming progress by lines of code is like measuring aircraft building progress by weight.",

    "Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program.",

    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",

    "Good code is its own best documentation. As you’re about to add a comment, ask yourself, ‘How can I improve the code so that this comment isn’t needed?",

    "One of my most productive days was throwing away 1000 lines of code.",

    "The trouble with programmers is that you can never tell what a programmer is doing until it’s too late.",

    "Hardware: The parts of a computer system that can be kicked.",

    "Computers are useless. They can only give you answers.",

    "The problem with troubleshooting is that trouble shoots back.",

    "A computer lets you make more mistakes faster than any invention in human history-with the possible exceptions of handguns and tequila.",

    "The production of too many useful things results in too many useless people.",

    "Technology makes it possible for people to gain control over everything, except over technology.",

    "Like car accidents, most hardware problems are due to driver error.",

    "Programmers 

are tools for converting caffeine into code.",

    "My software never has bugs. It just develops random features.",

    "The great thing about Object Oriented code is that it can make small, simple problems look like large, complex ones.",

    "After Perl everything else is just assembly language.",

    "The Internet: where men are men, women are men, and children are FBI agents.",

    "There are 10 types of people in the world: those who understand binary, and those who don't.",

    "Difference between a virus and windows ? Viruses rarely fail.",

    "1f u c4n r34d th1s u r34lly n33d t0 g37 l41d",

    "Hacking is like sex. You get in, you get out, and hope that you didn't leave something that can be traced back to you.",

    "Mess with the best, die like the rest."

    "QA Engineer walks into a bar. Orders a beer. Orders 0 beers. Orders 999999999 beers. Orders a lizard. Orders -1 beers. Orders a sfdeljknesv.",

    "There are only two hard things in Computer Science: cache invalidation, naming things and off-by-one errors.",

    "In software, we rarely have meaningful requirements. Even if we do, the only measure of success that matters is whether our solution solves the customer’s shifting idea of what their problem is.",

    "If Java had true garbage collection, most programs would delete themselves upon execution.",

    "C++ : Where friends have access to your private members.",

    "In C++ it’s harder to shoot yourself in the foot, but when you do, you blow off your whole leg.",

    "Most software today is very much like an Egyptian pyramid with millions of bricks piled on top of each other, with no structural integrity, but just done by brute force and thousands of slaves.",

    "I’ve noticed lately that the paranoid fear of computers becoming intelligent and taking over the world has almost entirely disappeared from the common culture.  Near as I can tell, this coincides with the release of MS-DOS.",

    "No matter how slick the demo is in rehearsal, when you do it in front of a live audience, the probability of a flawless presentation is inversely proportional to the number of people watching, raised to the power of the amount of money involved.",

    "The most amazing achievement of the computer software industry is its continuing cancellation of the steady and staggering gains made by the computer hardware industry.",

    "There are two major products that come out of Berkeley: LSD and UNIX.  We don’t believe this to be a coincidence.",

    "Computers are like bikinis. They save people a lot of guesswork.",

    "Linux is only free if your time has no value.",

    "Documentation is like sex; when it's good, it's very, very good, and when it's bad, it's better than nothing.",

    "The difference between theory and practice is that in theory, there is no difference between theory and practice.",

    "Programming is like sex: one mistake and you’re providing support for a lifetime.",

    "There are only two kinds of programming languages: those people always bitch about and those nobody uses.",

    "Beware of bugs in the above code; I have only proved it correct, not tried it. ",

    "We know about as much about software quality problems as they knew about the Black Plague in the 1600s. We’ve seen the victims’ agonies and helped burn the corpses. We don’t know what causes it; we don’t really know if there is only one disease. We just suffer — and keep pouring our sewage into our water supply.",

    "Writing the first 90 percent of a computer program takes 90 percent of the time. The remaining ten percent also takes 90 percent of the time and the final touches also take 90 percent of the time.",

    "There are two ways of constructing a software design; one way is to make it so simple that there are obviously no deficiencies, and the other way is to make it so complicated that there are no obvious deficiencies. The first method is far more difficult.",

    "You should name a variable using the same care with which you name a first-born child.",

    "Einstein argued that there must be simplified explanations of nature

, because God is not capricious or arbitrary. No such faith comforts the software engineer.",

    "XML is like violence – if it doesn’t solve your problems, you are not using enough of it.",

    "Saying that Java is good because it works on all platforms is like saying anal sex is good because it works on all genders.",

    "I love deadlines. I like the whooshing sound they make as they fly by.",

    "Perl – The only language that looks the same before and after RSA encryption.",

    "Two things are infinite: the universe and human stupidity; and I’m not sure about the universe.",

    "In theory, theory and practice are the same. In practice, they’re not.",

    "It is practically impossible to teach good programming style to students that have had prior exposure to BASIC. As potential programmers, they are mentally mutilated beyond hope of regeneration.",

    "If debugging is the process of removing software bugs, then programming must be the process of putting them in.",

    "A computer lets you make more mistakes faster than any other invention in human history, with the possible exceptions of handguns and tequila.",

    "I have always wished for my computer to be as easy to use as my telephone; my wish has come true because I can no longer figure out how to use my telephone.",

    "I don’t care if it works on your machine! We are not shipping your machine!",

    "Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning.",

    "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.",

    "On two occasions I have been asked, ‘Pray, Mr. Babbage, if you put into the machine wrong figures, will the right answers come out?’ I am not able rightly to apprehend the kind of confusion of ideas that could provoke such a question.”",

    "PHP is a minor evil perpetrated and created by incompetent amateurs, whereas Perl is a great and insidious evil, perpetrated by skilled but perverted professionals.",

    "Measuring programming progress by lines of code is like measuring aircraft building progress by weight.",

    "Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.",

    "Some people, when confronted with a problem, think “I know, I’ll use regular expressions.” Now they have two problems.",

    "It always takes longer than you expect, even when you take into account Hofstadter’s Law.",

    "Walking on water and developing software from a specification are easy if both are frozen.",

    "We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.",

]

GDMORNING = [

    "`Life is full of uncertainties. But there will always be a sunrise after every sunset. Good morning!`",

    "`It doesn’t matter how bad was your yesterday. Today, you are going to make it a good one. Wishing you a good morning!`",

    "`If you want to gain health and beauty, you should wake up early. Good morning!`",

    "`May this morning offer you new hope for life! May you be happy and enjoy every moment of it. Good morning!`",

    "`May the sun shower you with blessings and prosperity in the days ahead. Good morning!`",

    "`Every sunrise marks the rise of life over death, hope over despair and happiness over suffering. Wishing you a very enjoyable morning today!`",

    "`Wake up and make yourself a part of this beautiful morning. A beautiful world is waiting outside your door. Have an enjoyable time!`",

    "`Welcome this beautiful morning with a smile on your face. I hope you’ll have a great day today. Wishing you a very good morning!`",

    "`You have been blessed with yet another day. What a wonderful way of welcoming the blessing with such a beautiful morning! Good morning to you!`",

    "`Waking up in such a beautiful morning is a guaranty for a day that’s beyond amaz

ing. I hope you’ll make the best of it. Good morning!`",

    "`Nothing is more refreshing than a beautiful morning that calms your mind and gives you reasons to smile. Good morning! Wishing you a great day.`",

    "`Another day has just started. Welcome the blessings of this beautiful morning. Rise and shine like you always do. Wishing you a wonderful morning!`",

    "`Wake up like the sun every morning and light up the world your awesomeness. You have so many great things to achieve today. Good morning!`",

    "`A new day has come with so many new opportunities for you. Grab them all and make the best out of your day. Here’s me wishing you a good morning!`",

    "`The darkness of night has ended. A new sun is up there to guide you towards a life so bright and blissful. Good morning dear!`",

    "`Wake up, have your cup of morning tea and let the morning wind freshen you up like a happiness pill. Wishing you a good morning and a good day ahead!`",

    "`Sunrises are the best; enjoy a cup of coffee or tea with yourself because this day is yours, good morning! Have a wonderful day ahead.`",

    "`A bad day will always have a good morning, hope all your worries are gone and everything you wish could find a place. Good morning!`",

    "`A great end may not be decided but a good creative beginning can be planned and achieved. Good morning, have a productive day!`",

    "`Having a sweet morning, a cup of coffee, a day with your loved ones is what sets your “Good Morning” have a nice day!`",

    "`Anything can go wrong in the day but the morning has to be beautiful, so I am making sure your morning starts beautiful. Good morning!`",

    "`Open your eyes with a smile, pray and thank god that you are waking up to a new beginning. Good morning!`",

    "`Morning is not only sunrise but A Beautiful Miracle of God that defeats the darkness and spread light. Good Morning.`",

    "`Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good Morning!`",

    "`If you want to gain health and beauty, you should wake up early. Good Morning!`",

    "`Birds are singing sweet melodies and a gentle breeze is blowing through the trees, what a perfect morning to wake you up. Good morning!`",

    "`This morning is so relaxing and beautiful that I really don’t want you to miss it in any way. So, wake up dear friend. A hearty good morning to you!`",

    "`Mornings come with a blank canvas. Paint it as you like and call it a day. Wake up now and start creating your perfect day. Good morning!`",

    "`Every morning brings you new hopes and new opportunities. Don’t miss any one of them while you’re sleeping. Good morning!`",

    "`Start your day with solid determination and great attitude. You’re going to have a good day today. Good morning my friend!`",

    "`Friendship is what makes life worth living. I want to thank you for being such a special friend of mine. Good morning to you!`",

    "`A friend like you is pretty hard to come by in life. I must consider myself lucky enough to have you. Good morning. Wish you an amazing day ahead!`",

    "`The more you count yourself as blessed, the more blessed you will be. Thank God for this beautiful morning and let friendship and love prevail this morning.`",

    "`Wake up and sip a cup of loving friendship. Eat your heart out from a plate of hope. To top it up, a fork full of kindness and love. Enough for a happy good morning!`",

    "`It is easy to imagine the world coming to an end. But it is difficult to imagine spending a day without my friends. Good morning.`",

]

RENDISTR = [

    "`I Know Uh ez Rendi Bhay Dont show Your Randi Pesa Here`",

    "`Jag Suna suna laage Sab #maderchod bhay`",

    "`you talking behind meh wew uh iz my fan now bhay`",

    "`Wanna pass in Life Goto BRAZZER.CAM BHAY`",

    "`Uh iz Pro i iz noob your boob is landi uh are Randi`",

    "`Sellers Nasa calling Uh bhay😆`",

    "`Badwoo ki yojna behan bna ke ch*da uh iz badwa its your yozja?`",

    "`CHAND PE CHADA HAI CHANDYAAN KA GHODA TERA NAAM HAI MANSUR TU HAI BEHAN KA LOD*😂`

",

    "`Jab se dil lga baithe tanhai me maa chu*da baithe wo kho gyi kisi aur ke pyar hum apne hi jaato me aag lga baithe`",

    "`Chadii ke ander se lal pani kha se ata hai ky teri masuka ka bhosda bhi paan khata hai😂`",

    "`Sun bhosdi ke By anonyCrew MOHABBAT KE SIWA AUR BHI GAM HAI JAMANE ME BSDK GAND PAHAT JATI HAI PAISA KAMANE ME`",

    "`Thaan liya tha Sayri nhi krege Unka pichwada dekha Alfaaz nikal gye`",

    "`Ravivaar ko dekha Chand Ka Tukra Itna Baar Dekha par Jaath na Ukra`",

    "`Katal kro Tir se Talwar me Ky Rkkha hai Maal Chodo Sari Me Salwar me Ky Rkkha hai`",

]

NOOBSTR = [

    "`YOU PRO NIMBA DONT MESS WIDH MEH`",

    "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",

    "`Sometimes one middle finger isn’t enough to let someone know how you feel. That’s why you have two hands`",

    "`Some Nimbas need to open their small minds instead of their big mouths`",

    "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",

    "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",

    "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",

]

CONGOREACTS = [

    "`Congratulations and BRAVO!`",

    "`You did it! So proud of you!`",

    "`This calls for celebrating! Congratulations!`",

    "`I knew it was only a matter of time. Well done!`",

    "`Congratulations on your well-deserved success.`",

    "`Heartfelt congratulations to you.`",

    "`Warmest congratulations on your achievement.`",

    "`Congratulations and best wishes for your next adventure!”`",

    "`So pleased to see you accomplishing great things.`",

    "`Feeling so much joy for you today. What an impressive achievement!`",

]

INSULT_STRINGS = [

    "Active Volcano is the best swimming pool for you.",

    "Alas! Your neurotransmitters are no more working.",

    "Are you crazy you fool.",

    "As an outsider, what do you think of the human race?",

    "Believe me you are not normal.",

    "Bot rule 420 section 69 prevents me from replying to stupid nubfuks like you.",

    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.",

    "Brains aren't everything. In your case they're nothing.",

    "Come back and talk to me when your I.Q. exceeds your age.",

    "Command not found. Just like your brain.",

    "Dance naked on a couple of HT wires.",

    "Don't drink and type.",

    "Do you realize you are making a fool of yourself? Apparently not.",

    "Everyone has the right to be stupid but you are abusing the privilege.",

    "Go Green! Stop inhaling Oxygen.",

    "God was searching for you. You should leave to meet him.",

    "Have you tried shooting yourself as high as 100m using a canon.",

    "Head shots are fun. Get yourself one.",

    "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.",

    "How about you stop breathing for like 1 day? That'll be great.",

    "I'm not saying you're stupid, I'm just saying you've got bad luck when it comes to thinking.",

    "I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.",

    "I bet your brain feels as good as new, seeing that you never use it.",

    "I don't know what makes you so stupid, but it really works.",

    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",

    "If you’re talking behind my back then you’re in a perfect position to kiss my a**!.",

    "I heard phogine is poisonous but i guess you wont mind inhaling it for fun.",

    "I think you should go home or better a mental asylum.",

    "I would ask you how old you are but I know you can't count that high.",

    "Keep talking, someday you'll say something intelligent!.......(I doubt it though)",

    "Launch yourself into outer space while forgetting oxygen on Earth.",

    "Ordinarily people live and learn. You just live.",

    "Owww ... Such a stupid idiot.",

    "People like you are the reason we have middle fingers.",

    "Pick up a gun and shoot yourself.",

    "Shock me, say something intelligent.",

    "Sorry, we do not sell brains.",

    "Stop talking BS and jump in front of a running bullet train.",

    "Stupidity is not a

 crime so you are free to go.",

    "Try bathing with Hydrochloric Acid instead of water.",

    "Try jumping from a hundred story building but you can do it only once.",

    "Try playing catch and throw with RDX its fun.",

    "Try provoking a tiger while you both are in a cage.",

    "Try this: if you hold your breath underwater for an hour, you can then hold it forever.",

    "Try to spend one day in a coffin and it will be yours forever.",

    "Volunteer for target in an firing range.",

    "What language are you speaking? Cause it sounds like bullshit.",

    "When your mom dropped you off at the school, she got a ticket for littering.",

    "You are proof that evolution CAN go in reverse.",

    "You can be the first person to step on sun. Have a try.",

    "You can stay underwater for the rest of your life without coming back up.",

    "You can type better than that.",

    "You could make a world record by jumping from a plane without parachute.",

    "You didn't evolve from apes, they evolved from you.",

    "Your IQ's lower than your shoe size.",

    "Your enzymes are meant to digest rat poison.",

    "You should Volunteer for target in an firing range.",

    "You should donate your brain seeing that you never used it.",

    "You should paint yourself red and run in a bull marathon.",

    "You should try holding TNT in your mouth and igniting it.",

    "You should try hot bath in a volcano.",

    "You should try playing snake and ladders, with real snakes and no ladders.",

    "You should try sleeping forever.",

    "You should try swimming with great white sharks.",

    "You should try tasting cyanide.",

    "You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.",

    "Zombies eat brains... you're safe.",

    "give your 100%. Now, go donate blood.",

]

RUNSREACTS = [

    "`Runs to Thanos`",

    "`Runs far, far away from earth`",

    "`Running faster than supercomputer, cuzwhynot`",

    "`Runs to SunnyLeone`",

    "`ZZzzZZzz... Huh? what? oh, just them again, nevermind.`",

    "`Look out for the wall!`",

    "Don't leave me alone with them!!",

    "`You run, you die.`",

    "`Jokes on you, I'm everywhere`",

    "You could also try /kickme, I hear that's fun.",

    "`You can run, but you can't hide.`",

    "I'm behind you...",

    "We can do this the easy way, or the hard way.",

    "You just don't get it, do you?",

    "Yeah, you better run!",

    "I'd run faster if I were you.",

    "May the odds be ever in your favour.",

    "Famous last words.",

    "And they disappeared forever, never to be seen again.",

    '"Oh, look at me! I\'m so cool, I can run from a bot!" - this person',

    "Yeah yeah, just tap /kickme already.",

    "Here, take this ring and head to Mordor while you're at it.",

    "Legend has it, they're still running...",

    "Unlike Harry Potter, your parents can't protect you from me.",

    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "

    "be the next Vader.",

    "Keep it up, not sure we want you here anyway.",

    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",

    "NO RUNNING IN THE HALLWAYS!",

    "Hasta la vista, baby.",

    "Who let the dogs out?",

    "My milkshake brings all the boys to yard... So run faster!",

    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",

    "Hey, look at them! They're running from the inevitable banhammer... Cute.",

    "What are you running after, a white rabbit?",

    "As The Doctor would say... RUN!",

    "`Running a marathon...there's an app for that.`",

]

RAPE_STRINGS = [

    "`Rape Done Drink The Cum`",

    "`EK baat yaad rkhio, Chut ka Chakkar matlab maut se takkar`",

    "`The user has been successfully raped`",

    "`Dekho Bhaiyya esa hai! Izzat bachailo apni warna Gaand maar lenge tumhari`",

    "`Relax your Rear, ders nothing to fear,The Rape train is finally here`",

    "`Rape coming... Raped! haha 😆`",

    "`Kitni baar Rape krvyega mujhse?`",

    "`Tu Randi hai Sabko pta hai😂

`",

    "`Don't rape too much bossdk, else problem....`",

    "`Tu sasti rendi hai Sabko pta hai😂`",

    "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",

]

ABUSE_STRINGS = [

    "`Chutiya he rah jaye ga`",

    "`Ja be Gaandu`",

    "`Muh Me Lega Bhosdike ?`",

    "`Kro Gandu giri kam nhi toh Gand Maar lenge tumhari hum😂`",

    "`Suno Lodu Jyda muh na chalo be muh me lawda pel Diyaa jayega`",

    "`Sharam aagyi toh aakhe juka lijia land me dam nhi hai apke toh Shilajit kha lijia`",

    "`Kahe Rahiman Kaviraaj C**t Ki Mahima Aisi,L**d Murjha Jaaye Par Ch**t Waisi Ki Waisi`",

    "`Chudakkad Raand Ki Ch**T Mein Pele L*Nd Kabeer, Par Aisa Bhi Kya Choda Ki Ban Gaye Fakeer`",

]

GEY_STRINGS = [

    "`you gey bsdk`",

    "`you gey`",

    "`you gey in the house`",

    "`you chakka`",

    "`Bhago BC! Chakka aya`",

    "`you gey gey gey gey gey gey gey gey`",

    "`you gey go away`",

]

PRO_STRINGS = [

    "`This gey is pro as phack.`",

    "`Proness Lebel: 6969696969`",

    "`Itna pro banda dekhlia bc, ab to marna hoga.`",

    "`U iz pro but i iz ur DAD, KeK`",

    "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",

    "`Sometimes one middle finger isnâ€™t enough to let someone know how you feel. Thatâ€™s why you have two hands`",

    "`Some Nimbas need to open their small minds instead of their big mouths`",

    "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",

    "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",

    "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",

]

CHU_STRINGS = [

    "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",

    "`jindagi ki na toote lari iski lulli hoti nhi khadi`",

    "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",

    "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`",

    "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",

    "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",

    "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",

]

FUK_STRINGS = [

    "`It's better to let someone think you are an Idiot than to open your mouth and prove it.`",

    "`Talking to a liberal is like trying to explain social media to a 70 years old`",

    "`CHAND PE HAI APUN LAWDE.`",

    "`Pehle main tereko chakna dega, fir daru pilayega, fir jab aap dimag se nahi L*nd se sochoge, tab bolega..`",

    "`Pardhan mantri se number liya, parliament apne :__;baap ka hai...`",

    "`Cachaa Ooo bhosdi wale Chacha`",

    "`Aaisi Londiya Chodiye, L*nd Ka Aapa Khoye, Auro Se Chudi Na Ho, Biwi Wo Hi Hoye`",

    "`Nachoo Bhosdike Nachoo`",

    "`Jinda toh jaat ke baal bhi hai`",

    "`Sab ko pta tu randi ka baccha hai (its just a joke)`",

]

THANOS_STRINGS = [

    "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",

    "`Pani kam hai matkey me ga*d mardunga teri ek jatke me`",

    "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",

    "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",

    "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",

    "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",

    "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",

    "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",

    "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",

    "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",

]

ABUSEHARD_STRING = [

    "`Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller cha

le tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KIS`",

    "`Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa..ki unko ab bada loudha chahye..ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega..vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw..ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain... Aur agar tb b the apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha...ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga`",

    "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",

    "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",

    "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",

    "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`",

    "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",

    "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",

    "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",

    "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",

    "`Pani kam hai matke me gand marlunga jhatke me.`",

    "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",

    "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",

    "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",

    "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",

    "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",

    "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",

    "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baa

p Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",

    "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",

]

HELLOSTR = [

    "`Hi !`",

    "`‘Ello, gov'nor!`",

    "`What’s crackin’?`",

    "`‘Sup, homeslice?`",

    "`Howdy, howdy ,howdy!`",

    "`Hello, who's there, I'm talking.`",

    "`You know who this is.`",

    "`Yo!`",

    "`Whaddup.`",

    "`Greetings and salutations!`",

    "`Hello, sunshine!`",

    "`Hey, howdy, hi!`",

    "`What’s kickin’, little chicken?`",

    "`Peek-a-boo!`",

    "`Howdy-doody!`",

    "`Hey there, freshman!`",

    "`I come in peace!`",

    "`Ahoy, matey!`",

    "`Hiya!`",

    "`Oh retarded gey! Well Hello`",

]

SLAP_TEMPLATES = [

    "{user1} {hits} {victim} with a {item}.",

    "{user1} {hits} {victim} in the face with a {item}.",

    "{user1} {hits} {victim} around a bit with a {item}.",

    "{user1} {throws} a {item} at {victim}.",

    "{user1} grabs a {item} and {throws} it at {victim}'s face.",

    "{user1} {hits} a {item} at {victim}.",

    "{throws} a few {item} at {victim}.",

    "{user1} grabs a {item} and {throws} it in {victim}'s face.",

    "{user1} launches a {item} in {victim}'s general direction.",

    "{user1} sits on {victim}'s face while slamming a {item} {where}.",

    "{user1} starts slapping {victim} silly with a {item}.",

    "{user1} pins {victim} down and repeatedly {hits} them with a {item}.",

    "{user1} grabs up a {item} and {hits} {victim} with it.",

    "{user1} starts slapping {victim} silly with a {item}.",

    "{user1} holds {victim} down and repeatedly {hits} them with a {item}.",

    "{user1} prods {victim} with a {item}.",

    "{user1} picks up a {item} and {hits} {victim} with it.",

    "{user1} ties {victim} to a chair and {throws} a {item} at them.",

    "{user1} {hits} {victim} {where} with a {item}.",

    "{user1} ties {victim} to a pole and whips them {where} with a {item}."

    "{user1} gave a friendly push to help {victim} learn to swim in lava.",

    "{user1} sent {victim} to /dev/null.",

    "sent {victim} down the memory hole.",

    "{user1} beheaded {victim}.",

    "threw {victim} off a building.",

    "{user1} replaced all of {victim}'s music with Nickelback.",

    "{user1} spammed {victim}'s email.",

    "made {victim} a knuckle sandwich.",

    "{user1} slapped {victim} with pure nothing.",

    "{user1} hit {victim} with a small, interstellar spaceship.",

    "{user1} quickscoped {victim}.",

    "put {victim} in check-mate.",

    "{user1} RSA-encrypted {victim} and deleted the private key.",

    "{user1} put {victim} in the friendzone.",

    "{user1} slaps {victim} with a DMCA takedown request!",

]

ITEMS = [

    "cast iron skillet",

    "large trout",

    "baseball bat",

    "cricket bat",

    "wooden cane",

    "nail",

    "printer",

    "shovel",

    "pair of trousers",

    "CRT monitor",

    "diamond sword",

    "baguette",

    "physics textbook",

    "toaster",

    "portrait of Richard Stallman",

    "television",

    "mau5head",

    "five ton truck",

    "roll of duct tape",

    "book",

    "laptop",

    "old television",

    "sack of rocks",

    "rainbow trout",

    "cobblestone block",

    "lava bucket",

    "rubber chicken",

    "spiked bat",

    "gold block",

    "fire extinguisher",

    "heavy rock",

    "chunk of dirt",

    "beehive",

    "piece of rotten meat",

    "bear",

    "ton of bricks",

]

THROW = [

    "throws",

    "flings",

    "chucks",

    "hurls",

]

HIT = [

    "hits",

    "whacks",

    "fek ke maari",

    "slaps",

    "smacks",

    "bashes",

]

WHERE = ["in the chest", "on the head", "on the butt", "on the crotch"]

async def slap(replied_user, event, DEFAULTUSER):

    """Construct a funny slap sentence !!"""

    user_id = replied_user.user.id

    first_name = replied_user.user.first_name

    username = replied_user.user.username

    if username:

        slapped = "@{}".format(username)

    else:

        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)

    

item = random.choice(ITEMS)

    hit = random.choice(HIT)

    throw = random.choice(THROW)

    where = random.choice(WHERE)

    return temp.format(

        user1=DEFAULTUSER,

        victim=slapped,

        item=item,

        hits=hit,

        throws=throw,

        where=where,

    )

UWUS = [

    "(・`ω´・)",

    ";;w;;",

    "owo",

    "UwU",

    ">w<",

    "^w^",

    r"\(^o\) (/o^)/",

    "( ^ _ ^)∠☆",

    "(ô_ô)",

    "~:o",

    ";-;",

    "(*^*)",

    "(>_",

    "(♥_♥)",

    "*(^O^)*",

    "((+_+))",

]

SHGS = [

    "┐(´д｀)┌",

    "┐(´～｀)┌",

    "┐(´ー｀)┌",

    "┐(￣ヘ￣)┌",

    "╮(╯∀╰)╭",

    "╮(╯_╰)╭",

    "┐(´д`)┌",

    "┐(´∀｀)┌",

    "ʅ(‌◡◝)ʃ",

    "ლ(ﾟдﾟლ)",

    "┐(ﾟ～ﾟ)┌",

    "┐('д')┌",

    "ლ｜＾Д＾ლ｜",

    "ლ（╹ε╹ლ）",

    "ლ(ಠ益ಠ)ლ",

    "┐(‘～`;)┌",

    "ヘ(´－｀;)ヘ",

    "┐( -“-)┌",

    "乁༼☯‿☯✿༽ㄏ",

    "ʅ（´◔౪◔）ʃ",

    "ლ(•ω •ლ)",

    "ヽ(゜～゜o)ノ",

    "ヽ(~～~ )ノ",

    "┐(~ー~;)┌",

    "┐(-。ー;)┌",

    r"¯\_(ツ)_/¯",

    r"¯\_(⊙_ʖ⊙)_/¯",

    "乁ʕ •‌ ۝ •‌ ʔㄏ",

    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",

    "乁( ⁰‌  Ĺ‌ ⁰‌ ) ㄏ",

]

CRI = [

    "أ‿أ",

    "╥﹏╥",

    "(;﹏;)",

    "(ToT)",

    "(┳Д┳)",

    "(ಥ﹏ಥ)",

    "（；へ：）",

    "(T＿T)",

    "（πーπ）",

    "(Ｔ▽Ｔ)",

    "(⋟﹏⋞)",

    "（ｉДｉ）",

    "(´Д⊂ヽ",

    "(;Д;)",

    "（>﹏<）",

    "(TдT)",

    "(つ﹏⊂)",

    "༼☯﹏☯༽",

    "(ノ﹏ヽ)",

    "(ノAヽ)",

    "(╥_╥)",

    "(T⌓T)",

    "(༎ຶ⌑༎ຶ)",

    "(☍﹏⁰)｡",

    "(ಥ_ʖಥ)",

    "(つд⊂)",

    "(≖‌_≖‌)",

    "(இ﹏இ`｡)",

    "༼ಢ_ಢ༽",

    "༼ ༎ຶ ෴ ༎ຶ༽",

]

FACEREACTS = [

    [

        "( ‌° ‌ʖ ‌°)",

        "(ʘ‿ʘ)",

        "(✿´‿`)",

        "=‌٩(๑☉ᴗ☉)੭ु⁾⁾",

        "(*⌒▽⌒*)θ～♪",

        "°˖✧◝(⁰▿⁰)◜✧˖°",

        "✌(-‿-)✌",

        "⌒°(❛ᴗ❛)°⌒",

        "(ﾟ<|＼(･ω･)／|>ﾟ)",

        "ヾ(o✪‿✪o)ｼ",

    ],

    [

        "(҂⌣‌_⌣‌)",

        "（；¬＿¬)",

        "(-｡-;",

        "┌[ O ʖ‌ O ]┐",

        "〳 ‌° Ĺ‌ ‌° 〵",

    ],

    [

        "(ノ^∇^)",

        "(;-_-)/",

        "@(o・ェ・)@ノ",

        "ヾ(＾-＾)ノ",

        "ヾ(◍’౪`◍)ﾉﾞ♡",

        "(ό‿ὸ)ﾉ",

        "(ヾ(´・ω・｀)",

    ],

    [

        "༎ຶ‿༎ຶ",

        "(‿ˠ‿)",

        "╰U╯☜(◉ɷ◉ )",

        "(;´༎ຶ益༎ຶ`)♡",

        "╭∩╮(︶ε︶*)chu",

        "( ＾◡＾)っ (‿|‿)",

    ],

    [

        "乂❤‿❤乂",

        "(｡♥‿♥｡)",

        "( ‌~ ‌ʖ ‌°)",

        "໒( ♥ ◡ ♥ )७",

        "༼♥ل‌♥༽",

    ],

    [

        "(・_・ヾ",

        "｢(ﾟﾍﾟ)",

        "﴾‌๏‌๏﴿",

        "(￣■￣;)!?",

        "▐ ˵ ‌° (oo) °‌ ˵ ▐",

        "(-_-)ゞ゛",

    ],

    [

        "(✖╭╮✖)",

        "✖‿✖",

        "(+_+)",

        "(✖﹏✖)",

        "∑(✘Д✘๑)",

    ],

    [

        "(＠´＿｀＠)",

        "⊙︿⊙",

        "(▰˘︹˘▰)",

        "●︿●",

        "(　´_ﾉ` )",

        "彡(-_-;)彡",

    ],

    [

        "-ᄒᴥᄒ-",

        "◖⚆ᴥ⚆◗",

    ],

    [

        "( ‌° ‌ʖ ‌°)",

        r"¯\_(ツ)_/¯",

        "( ‌°( ‌° ‌ʖ( ‌° ‌ʖ ‌°)ʖ ‌°) ‌°)",

        "ʕ•ᴥ•ʔ",

        "(▀‌Ĺ‌▀‌ ‌)",

        "(ง ‌° ‌ل‌ ‌°)ง",

        "༼ つ ◕_◕ ༽つ",

        "ಠ_ಠ",

        "(☞ ‌° ‌ʖ ‌°)☞",

        r"¯\_༼ ି ~ ି ༽_/¯",

        "c༼ ‌° ‌ʖ ‌° ༽⊃",

        "ʘ‿ʘ",

        "ヾ(-_- )ゞ",

        "(っ˘ڡ˘ς)",

        "(´ж｀ς)",

        "( ಠ ʖ‌ ಠ)",

        "(° ‌ʖ‌°)╭∩╮",

        "(ᵟຶ︵ ᵟຶ)",

        "(งツ)ว",

        "ʚ(•｀",

        "(っ▀¯▀)つ",

        "(◠﹏◠)",

        "( ‌ಠ ʖ‌ ‌ಠ)",

        "( ఠ ‌ʖ ఠ)",

        "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",

        "(⊃｡•‌‿•‌｡)⊃",

        "(._.)",

        "{•‌_•‌}",

        "(ᵔᴥᵔ)",

        "♨_♨",

        "⥀.⥀",

        "ح˚௰˚づ ",

        "(҂◡_◡)",

        "ƪ(ړײ)‎ƪ",

        "(っ•‌｡•‌)♪♬",

        "◖ᵔᴥᵔ◗ ♪ ♫ ",

        "(☞ﾟヮﾟ)☞",

        "[¬º-°]¬",

        "(Ծ‸ Ծ)",

        "(•‌ᴗ•‌)و ‌",

        "ヾ(´〇`)ﾉ♪♪♪",

        "(ง'‌-'‌)ง",

        "ლ(•‌•‌ლ)",

        "ʕ •‌؈•‌ ₎",

        "♪♪ ヽ(ˇ∀ˇ )ゞ",

        "щ（ﾟДﾟщ）",

        "( ˇ෴ˇ )",

        "눈_눈",

        "(๑•‌ ₃ •‌๑) ",

        "( ˘ ³˘)♥ ",

        "ԅ(≖‿≖ԅ)",

        "♥‿♥",

        "◔_◔",

        "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",

        "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",

        "( ఠൠఠ )ﾉ",

        "٩(๏_๏)۶",

        "┌(ㆆ㉨ㆆ)ʃ",

        "ఠ_ఠ",

        "(づ｡◕‿‿◕｡)づ",

        "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",

        "“ヽ(´▽｀)ノ”",

        "༼ ༎ຶ ෴ ༎ຶ༽",

        "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",

        "(づ￣ ³￣)づ",

        "(⊙.☉)7",

        "ᕕ( ᐛ )ᕗ",

        "t(-_-t)",

        "(ಥ⌣ಥ)",

        "ヽ༼ ಠ益ಠ ༽ﾉ",

        "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",

        

"ミ●﹏☉ミ",

        "(⊙_◎)",

        "¿ⓧ_ⓧﮌ",

        "ಠ_ಠ",

        "(´･_･)",

        "ᕦ(ò_óˇ)ᕤ",

        "⊙﹏⊙",

        "(╯°□°）╯︵ ┻━┻",

        r"¯\_(⊙︿⊙)_/¯",

        "٩◔‌◔۶",

        "°‿‿°",

        "ᕙ(⇀‸↼‶)ᕗ",

        "⊂(◉‿◉)つ",

        "V•ᴥ•V",

        "q(❂‿❂)p",

        "ಥ_ಥ",

        "ฅ^•ﻌ•^ฅ",

        "ಥ﹏ಥ",

        "（ ^_^）o自自o（^_^ ）",

        "ಠ‿ಠ",

        "ヽ(´▽)/",

        "ᵒᴥᵒ#",

        "( ‌° ‌ʖ ‌°)",

        "┬─┬﻿ ノ( ゜-゜ノ)",

        "ヽ(´ー｀)ノ",

        "☜(⌒▽⌒)☞",

        "ε=ε=ε=┌(;*´Д)ﾉ",

        "(╬ ಠ益ಠ)",

        "┬─┬⃰‌ (ᵔᵕᵔ‌ )",

        "┻━┻ ︵ヽ(Д´)ﾉ︵﻿ ┻━┻",

        r"¯\_(ツ)_/¯",

        "ʕᵔᴥᵔʔ",

        "(`･ω･´)",

        "ʕ•ᴥ•ʔ",

        "ლ(｀ー´ლ)",

        "ʕʘ‌ʘ‌ʔ",

        "（　ﾟДﾟ）",

        r"¯\(°_o)/¯",

        "(｡◕‿◕｡)",

    ],

]
