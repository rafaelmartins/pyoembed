#!/usr/bin/env python
# coding: utf-8

from pyoembed import oEmbed
from pyoembed.exceptions import PyOembedException

import sys

URLS = [

    # IFTTT
    'http://ifttt.com/recipes/147788-feed-to-facebook-page',
    'https://ifttt.com/recipes/147788-feed-to-facebook-page',

    # YouTube
    'http://www.youtube.com/watch?v=EBRMq2Ioxsc',
    'https://www.youtube.com/watch?v=EBRMq2Ioxsc',
    'http://youtube.com/watch?v=EBRMq2Ioxsc',
    'https://youtube.com/watch?v=EBRMq2Ioxsc',
    'http://youtu.be/EBRMq2Ioxsc',

    # Flickr
    'http://www.flickr.com/photos/24736958@N06/2337532608/',
    'https://www.flickr.com/photos/24736958@N06/2337532608/',
    'http://flic.kr/p/4yyt1m',

    # Revision3
    'http://revision3.com/tekzilla/free-file-sync-meg-turney',
    'http://www.revision3.com/tekzilla/free-file-sync-meg-turney',

    # Vimeo
    'http://vimeo.com/12414863',
    'https://vimeo.com/12414863',
    'http://vimeo.com/groups/musicvideo/videos/76253725',
    'https://vimeo.com/groups/musicvideo/videos/76253725',

    # CollegeHumor
    'http://www.collegehumor.com/video/6953943/sir-david-attenborough-'
    'narrates-olympic-curling',
    'https://www.collegehumor.com/video/6953943/sir-david-attenborough-'
    'narrates-olympic-curling',

    # Jest
    'http://www.jest.com/video/201448/twitter-parody-political-account-'
    'graveyard',

    # Poll Everywhere
    'http://www.polleverywhere.com/clickable_images/VkPbmAmhfr4iiyG',
    'http://www.polleverywhere.com/free_text_polls/1bhoWkklqgnqrWI',
    'http://www.polleverywhere.com/multiple_choice_polls/9VqZBgDLV7kO4T6',
    'https://www.polleverywhere.com/clickable_images/VkPbmAmhfr4iiyG',
    'https://www.polleverywhere.com/free_text_polls/1bhoWkklqgnqrWI',
    'https://www.polleverywhere.com/multiple_choice_polls/9VqZBgDLV7kO4T6',

    # iFixIt
    'http://www.ifixit.com/Guide/Xbox+360+Red+Ring+of+Death+Fix+Kit/3550',

    # deviantART
    'http://stefangrosjean.deviantart.com/art/Naked-Shoulder-434517931',
    'http://fav.me/d76p86j',
    'http://sta.sh/01pdlk4en9zk',

    # Slideshare
    'http://www.slideshare.net/mitsuhiko/flask',
    'https://www.slideshare.net/mitsuhiko/flask',

    # NFB
    'http://www.nfb.ca/film/king_of_blades?hpen=feature_2',
    'https://www.nfb.ca/film/king_of_blades?hpen=feature_2',

    # Dotsub
    'http://dotsub.com/view/99eaba09-787a-40a9-9125-27a729de71db',
    'https://dotsub.com/view/99eaba09-787a-40a9-9125-27a729de71db',

    # Rdio
    'http://www.rdio.com/artist/Vanguart/album/Muito_Mais_Que_o_Amor/',
    'http://www.rdio.com/artist/Vanguart/album/Muito_Mais_Que_o_Amor/track/'
    'Meu_Sol/',
    'http://www.rdio.com/people/ChuckHipolitho/playlists/1104311/'
    'As_minhas_10%2B_do_Pop_Rock_Nacional/',
    'http://rd.io/x/QWpm2TddcnxH/',

    # Mixcloud
    'http://www.mixcloud.com/MarkusSchulz/global-dj-broadcast-feb-20-2014/',

    # Screenr
    'http://www.screenr.com/2hv8',

    # Funny or Die
    'http://www.funnyordie.com/videos/fe14c065c8/the-hug-with-bryce-dallas-'
    'howard',

    # Videojug
    'http://www.videojug.com/film/how-to-fit-thermostatic-radiator-valves',
    'http://www.videojug.com/interview/the-job-interview',

    # videos.sapo.pt
    'http://videos.sapo.pt/JySyzZSW0A1UBZBLhAW1',

    # justin.tv
    'http://www.justin.tv/fredrin',

    # official.fm
    'http://www.official.fm/playlists/9NMy?from=homepage&track_id=PfqH',

    # HuffDuffer
    'http://huffduffer.com/ethosophical/148918',

    # Mobypicture
    'http://www.mobypicture.com/user/kotetu005/view/16603797',
    'http://moby.to/439cks',

    # 23hq
    'http://www.23hq.com/catherinedaze/photo/15483108',

    # dailymotion
    'http://www.dailymotion.com/video/xrqdma_el-chavo-del-ocho-1981-funny-'
    'moment-el-maestro-longaniza_fun',

    # crowdranking
    'http://crowdranking.com/crowdrankings/t9288g0--best-soundtracks',

    # CircuitLab
    'https://www.circuitlab.com/circuit/7pq5wm/welcome-to-circuitlab/',

    # geograph.org.uk
    'http://www.geograph.org.uk/photo/3335661',
    'http://www.geograph.co.uk/photo/3335661',
    'http://www.geograph.ie/photo/3335661',

    # Geograph Deutschland
    'http://geo.hlipp.de/photo/47294',
    'http://geo-en.hlipp.de/photo/47294',
    'http://germany.geograph.org/photo/47294',

    # Coub
    'http://coub.com/view/swwj69q',

    # Speaker Deck
    'https://speakerdeck.com/mitsuhiko/advanced-flask-patterns',

    # blip.tv
    'http://blip.tv/jeffreytheseries/jeffrey-dear-diary-episode-1-6721010',
    'http://www.blip.tv/jeffreytheseries/jeffrey-dear-diary-episode-1-6721010',

    # Instagram
    'http://instagram.com/p/kf07KDKC0e/',
    'http://instagr.am/p/kf07KDKC0e/',

    # SoundCloud
    'https://soundcloud.com/vespasmandarinas/vespas-mandarinas-antes-que-1',

    # AOL On
    'http://on.aol.com/video/google-announces-new-milestones-for-lunar-'
    'xprize----discovery-news-518132683?icid=OnHomepageC2Wide_MustSee_Img'

    # Kickstarter
    'https://www.kickstarter.com/projects/1667991158/brazil-culture-and-'
    'history-podcast'

    # Ustream.tv
    'http://ustream.tv/ufc',
    'http://www.ustream.tv/ufc',
    'http://ustream.com/ufc',
    'http://www.ustream.com/ufc',

    # dailymile
    'http://www.dailymile.com/people/raegold/entries/27493726',

    # Sketchfab
    'http://sketchfab.com/show/8be963d578e544299bcd0332e3a6e30f',
    'https://sketchfab.com/show/8be963d578e544299bcd0332e3a6e30f',

    # Imgur
    'http://i.imgur.com/fo06aLJ.jpg',
    'http://imgur.com/fo06aLJ.jpg',
    'http://i.imgur.com/fo06aLJ',

    # Twitter
    'http://twitter.com/rafaelmartins/status/424199153364008960',
    'http://www.twitter.com/rafaelmartins/status/424199153364008960',
    'https://twitter.com/rafaelmartins/status/424199153364008960',
    'https://www.twitter.com/rafaelmartins/status/424199153364008960',

    # Spotify
    'http://open.spotify.com/track/0jkz56cwzYKs5xO1xwhZmr',
    'http://play.spotify.com/track/6oTb6ZMymRaepsn1lQeOpa',
    'https://open.spotify.com/track/0jkz56cwzYKs5xO1xwhZmr',
    'https://play.spotify.com/track/6oTb6ZMymRaepsn1lQeOpa',
]


if __name__ == '__main__':
    errors = 0
    for i in URLS:
        try:
            print >> sys.stdout, i, '...',
            sys.stdout.flush()
            oEmbed(i)
        except PyOembedException, e:
            print >> sys.stdout, 'fail'
            print >> sys.stderr, e.message
            errors += 1
        else:
            print >> sys.stdout, 'ok'
    print >> sys.stdout, 'Errors: %d' % errors
    sys.exit(1 if errors > 0 else 0)
