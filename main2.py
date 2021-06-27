import shutil
import tempfile
import urllib2.request

urlOri = 'https://calendar.google.com/calendar/u/0/embed?src=ps62t3hlmljku5ogtti3sct478@group.calendar.google.com&ctz=America/Argentina/La_Rioja&mode=AGENDA'

with urllib2.request.urlopen(urlOri) as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass