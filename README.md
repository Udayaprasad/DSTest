# DSTest


In this exercise , we will use an  open API  - The Lord of the Rings API.

The Lord of the Rings API is at https://the-one-api.herokuapp.com/
The documentation is at https://the-one-api.herokuapp.com/documentation ( Scroll to the bottom to see API details)

NOTE:       quote is a dialog in a movie

Exercise:
--------
You must code in Python and must use the micro web framework Flask.
You are free to use any Python open source library.

Please develop one and only one REST endpoint as follows:
'quotes/movie/{movieId}/character/{characterId}' where  {movieId} and {characterId} are HTTP path parameters

The above REST endpoint returns all quotes by a character in a movie

Response format:
--------
{
  "character_name": "<<CHARACTER_NAME>>"
  ,"movie_name" : "<<MOVIE_NAME>>"
  ,"quotes" : [
    "quote 1"
    ,"quote 2"
    ,"quote 3"
  ]
}

You are free to use all the API REST endpoints provided by The Lord of the Rings API


Example
------
Character name: Gandalf
character Id: 5cd99d4bde30eff6ebccfea0

Movie name: The Two Towers
Movie Id: 5cd95395de30eff6ebccde5b


The following REST endpoint returns all quotes by Gandalf in the movie  The Two Towers

quotes/movie/5cd95395de30eff6ebccde5b/character/5cd99d4bde30eff6ebccfea0


Response:

```
{
  "character_name": "Gandalf"
  ,"movie_name" : "The Two Towers"
  ,"quotes" : [
      "Sauron's wrath will be terrible, his retribution swift.           ",
      "The battle for Helm's Deep is over. The battle for Middle-earth is about to begin.",
      "(looking back out to Mordor) All our hopes now lie with two little Hobbits...",
      "...somewhere in the wilderness.",
      "Look to my coming at first light on the fifth day. At dawn......Iook to the east.",
      " Theoden King stands alone.,            ",
      "Theodred's death was not of your making.",
      "He was strong in life. His spirit will find its way to the halls of your     fathers. Westu h'l. Fer'u, Th'odred, Fer'u. ",
      "The veiling shadow that glowers in the east takes shape.Sauron will suffer no rival.From the summit of Barad-durhis Eye watches ceaselessly.But he is not so mighty yetthat he is above fear.Doubt ever gnaws at him.The rumor has reached him.The heir of Numenor still lives.",
      "This is but a taste of the terror that Saruman will unleash.    ,All     the more potent for he is driven now by fear of Sauron. Ride out and meet     him head on. Draw him away from your women and children.    , You must     fight. ",
      "Helm's Deep.",
      "There is no way out of that ravine. Theoden is walking into a trap. He     thinks he's leading them to safety. What they will get is a massacre.     Theoden has a strong will, but I fear for him. I fear for the survival of     Rohan. , He will need     you before the end,    Aragorn. The people of Rohan will need you. ,The defenses , to hold.  ",
      "Sauron fears you, Aragorn.He fears what you may become.And so he'll strike hard and fastat the world of Men.He will use his puppet Sarumanto destroy Rohan.War is coming.Rohan must defend itselfand therein lies our first challenge......for Rohan is weak and ready to fall.    ,The king's mind is enslavedit's an old device of Saruman's.His hold over King Theodenis now very strong.Sauron and Sarumanare tightening the noose.But for all their cunning......we have one advantage. The Ring remains hidden.And that we should seek to destroy it......has not yet enteredtheir darkest dreams. And so the weapon of the enemyis moving towards Mordor......in the hands of a Hobbit.Each day brings it closerto the fires of Mount Doom. We must trust now in Frodo.Everything depends upon speed......and the secrecy of his quest. ",
      "Did he?Did he, indeed? Good. Yes, very good.",
      "Do not regret your decision to leave him.Frodo must finish this task alone.",
      "The Grey Pilgrim.     That's what they used to call me. Three hundred lives of Men I've walked     this earth, and now I have no time. With luck, my search will not be in     vain. ,Look to my coming at first light on the fifth day. At dawn, look to     the east. ",
      "You shall not pass!",
      "I am a servant of the Secret Fire, wielder of the flame of Anor.    Go back to the Shadow.The dark fire will not avail you,flame of Udun!",
      "You cannot pass!",
      "Fly, you fools! ",
      "Edoras and the Golden Hall of Meduseld. There dwells Theoden,     King of Rohan...... whose mind is overthrown. Saruman's hold over King     Theoden is now very strong. ",
      "Be careful what you say.Do not look for welcome here.",
      "Hmmm ,You     would not part an old man from his walking stick.",
      "The courtesy of your hall is somewhat lessened of late......Theoden     King.",
      "Be silent. Keep your forked tongue behind your teeth. I have     not passed through fire and death......to bandy crooked words with a witless     worm.",
      "Theoden......son of Thengel......too long have you sat in     the Shadows.",
      "Hearken to me! I release you......from the spell.",
      "I will draw you, Saruman, as poison is drawn from a wound.",
      "You did not kill me......you     will not kill him.",
      "Be gone.",
      "You are tracking the footstepsof two young Hobbits.",
      "Breathe the free air again, my friend. ",
      "I am Saruman.Or rather, Sarumanas he should have been. ",
      "Through fire.....and water.",
      "From the lowest dungeonto the highest peak...... I fought with the Balrogof Morgoth.",
      "Until at last I threw downmy enemy......and smote his ruinupon the mountainside.",
      "Your fingers would remember their old strength     better......if they grasped your sword.",
      "Stars wheeled overhead......and every day was as longas a life age of the Earth.But it was not the end.I felt life in me again.",
      "Darkness took me......and I strayed out of thoughtand time.",
      "I've been sent back...... until my task is done.",
      "Gandalf? ,Yes.That was what they used to call me.Gandalf the Grey.That was my name.",
      "I am Gandalf the White.And I come back to you now......at the turn of the tide.",
      "One stage of your journey is over.Another begins. We must travel to Edoras with all speed.",
      "Yes, and it will not be easily cured. ",
      "It was more than mere chance thatbrought Merry and Pippin to Fangorn.A great power has been sleeping herefor many long years.The coming of Merry and Pippinwill be like the falling of small stones......that starts an avalanchein the mountains.",
      "A thing is about to happen that has nothappened since the Elder Days.The Ents are going to wake up.....and find that they are strong.",
      "Shadowfax.He is the lord of all horses......and has been my friendthrough many dangers.",
      "So stop your fretting, Master Dwarf.Merry and Pippin are quite safe.In fact, they are far saferthan you are about to be. "
  ]
}

```


