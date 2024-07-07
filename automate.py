import pywhatkit
import connectivity
from datetime import datetime
import threading
import message

# Auto-whatsapp sending
def send_mssg(mob,mssg):
    tm = datetime.now()
    hr = int(tm.strftime("%H"))
    min = int(tm.strftime("%M")) + 1
    pywhatkit.sendwhatmsg(mob,mssg,hr,min)

# Main Execution
mssg = message.get_mssg()
rows = connectivity.get_rows()
for row in rows:
    name = row[1]
    profile = row[2]
    mob = row[3]
    formatted_mssg = mssg.format(name=name,profile=profile)
    thread = threading.Thread(target=send_mssg,args=(mob,formatted_mssg))
    thread.start()
    thread.join()
