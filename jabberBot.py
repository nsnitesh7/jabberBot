import subprocess
import sys
from jabberbot import *

logging.basicConfig(level=logging.DEBUG)

jid = 'email id'
password = 'password'

class Fire_bot(JabberBot):

    @botcmd
    def youtube(self, mess, args):
        """Generates download link for youtube video"""
        return subprocess.check_output(['youtube-dl', '-g', args]).strip()    
	

username = jid
password = password
fire_bot = Fire_bot(username, password)
fire_bot.serve_forever()
