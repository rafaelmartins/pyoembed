#!/usr/bin/env python
# coding: utf-8

from pyoembed import oEmbed
from pyoembed.exceptions import PyOembedException

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
    'http://www.collegehumor.com/video/6953943/sir-david-attenborough-narrates-olympic-curling',
    'https://www.collegehumor.com/video/6953943/sir-david-attenborough-narrates-olympic-curling',

    # Jest
    'http://www.jest.com/video/201448/twitter-parody-political-account-graveyard',

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

    # Chirbit
    'http://chirb.it/89xLas',

    # NFB
    'http://www.nfb.ca/film/king_of_blades?hpen=feature_2',
    'https://www.nfb.ca/film/king_of_blades?hpen=feature_2',

    # Dotsub
    'http://dotsub.com/view/99eaba09-787a-40a9-9125-27a729de71db',
    'https://dotsub.com/view/99eaba09-787a-40a9-9125-27a729de71db',
]


for i in URLS:
    try:
        print i, '...',
        oEmbed(i)
    except PyOembedException, e:
        print 'fail'
        print e.message
    else:
        print 'ok'
