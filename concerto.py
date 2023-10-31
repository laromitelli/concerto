import json
import requests


# GLOBAL
SEATS_API = 'https://api.eventim.com/seatmap/api/SeatMapHandler?smcVersion=v5.2&version=v6.0.1&cType=fansale' \
      '&cId=13007&evId=1173407&a_sessionId=EVE_NO_SESSION&a_promotionId=0&a_systemId=1&a_affiliate=FIT' \
      '&fun=json&areaId=0&a_seatViewInfos=1'
EVENT_URL = 'https://www.fansale.it/fansale/tickets/pop-amp-rock/club-dogo/468801/17796612'
EMAIL_ALERT_URL = "http://wanderapp.altervista.org/api/send_reminder.php?email={}&object={}&body={}"
EMAIL = "la.romitelli@gmail.com"
EMAIL_OBJECT = "Concerto DOGO"
EMAIL_BODY = "Posto in parterre disponibile per il 10 Marzo"

# SCRIPT
code_request = requests.get(SEATS_API)
blocks = json.loads(code_request.text)['blocks']

for block in blocks:
    if block['name'] == 'Parterre In Piedi':
        available_seats = 0
        for graph in block['graphics']:
            available_seats = available_seats + (len(graph['pcBlock']))
        print('There are {} seats available.'.format(available_seats))
        if available_seats > 0:
            request = requests.get(EMAIL_ALERT_URL.format(EMAIL, EMAIL_OBJECT, EMAIL_BODY))
            if request.status_code == 200:
                print("Alert e-mail sent.")




