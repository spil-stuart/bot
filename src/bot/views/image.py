from yardbird.irc import IRCResponse
from viewer.models import Image, Link
from bot.utils import parse_request, fix_url

def image(request, url=None):
    url = fix_url(url)
    (c, n, m) = parse_request(request)
    nsfw = True if 'nsfw' in m else False
    img_obj = Image.objects.create(dest_url=url, nsfw=nsfw, posted_channel=c, posted_by=n, message=m)
    return IRCResponse('#test', 'added')