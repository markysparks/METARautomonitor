import sys
import re
import socket
import requests
from requests import exceptions

if sys.version_info[0] < 3:
    import tkMessageBox
else:
    from tkinter import messagebox as tkMessageBox

__author__ = 'Mark Baker  email: mark.baker@metoffice.gov.uk'


def get_metar_data(icao1, icao2, icao3, icao4, icao5, icao6, icao7, icao8, icao9, icao10):
    socket.setdefaulttimeout(8)
    response = ''

    """Get the latest METAR for specified ICAOs, format: &stn01=EGUW&stn02=EGLL&stn03=EGSS"""
    station_str = '&stn01=' + icao1 + '&stn02=' + icao2 + '&stn03=' + icao3 + '&stn04=' + icao4 + '&stn05=' + icao5 + \
                  '&stn06=' + icao6 + '&stn07=' + icao7 + '&stn08=' + icao8 + '&stn09=' + icao9 + '&stn10=' + icao10

    db_rqst_str = 'http://mdbdb-prod/cgi-bin/moods/webret.pl?pageType=mainpage&subtype=METARS&system=mdbdb-prod&idType=ICAO' \
                  + station_str + '&submit=Retrieve+Latest+Report'

    # example response = 'Obs returned = 0003 CODE NAME -: mdb VERSION ---: 4.25.0 COMPILED @ : 10:32:54 on Jul 19 2016
    # LATEST PLATFORM EGLL EGSS EGUW ELEMENTS MTR_RPT_TXT RCT_DAY RCT_HR RCT_MNT ICAO_ID DAY HR MNTRTABLE: Retrieval table
    # used: /usr/local/moods/tables//retrieval_tableRTABLE: TABLES base location: /usr/local/moods/tables/ddhhmmZ
    # ident report 270850Z EGLL  EGLL 270850Z 23012KT 9999 SCT012 BKN018 18/17 Q1015 TEMPO BKN014 270850Z EGSS  EGSS
    # 270850Z AUTO 23010KT 9999 -RA BKN005 17/16 Q1014 REDZ 270850Z EGUW  EGUW 270850Z AUTO 24010KT 4500 RA BKN009
    # OVC014 17/16 Q1014 GRN BECMG 7 000 -RA GRN'

    # Query to get the latest METAR web page result
    try:
        response = requests.get(db_rqst_str)

    except requests.exceptions.RequestException as e:
        pass
        tkMessageBox.showerror('Communications Error',
                               'Error retrieving data from MetDB - will retry if monitoring on.')

    # Check we have a response to our query before proceeding
    if response is not None:
        result = re.findall('.... \d\d\d\d\d\dZ AUTO', response.text)
        return result


if __name__ == "__main__":
    print('METAR Data= ', get_metar_data('EGSS', 'EGLL', 'EGUW', 'EGXE', 'EGKK'))
