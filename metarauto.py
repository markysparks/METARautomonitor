#!/usr/bin/env python
import sys
import logging

import re

import datetime

logging.basicConfig()
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

import get_metarstatus
import metarautomonitor_gui as gui

if sys.version_info[0] < 3:
    import Tkinter as tk
    import tkMessageBox
else:
    import tkinter as tk
    from tkinter import messagebox as tkMessageBox

__author__ = 'Mark Baker  email: mark.baker@metoffice.gov.uk'


class Controller:
    """Main GUI controller, handles mouse, keyboard and data change events."""

    def __init__(self):
        self.root = tk.Tk()
        self.main_view = gui.MainView(self.root)

        self.icao1 = None
        self.icao2 = None
        self.icao3 = None
        self.icao4 = None
        self.icao5 = None
        self.icao6 = None
        self.icao7 = None
        self.icao8 = None
        self.icao9 = None
        self.icao10 = None

        self.icao_msg0 = None
        self.icao_msg1 = None
        self.icao_msg2 = None
        self.icao_msg3 = None
        self.icao_msg4 = None
        self.icao_msg5 = None
        self.icao_msg6 = None
        self.icao_msg7 = None
        self.icao_msg8 = None
        self.icao_msg9 = None

        self.latest_time = None
        self.latest_data = None
        self.latest_data_str = None
        self.old_data = ()

        self.monitoring = False

        self.main_view.controls_view.monitor_button.bind('<Button>', self.start_monitor)
        self.main_view.controls_view.monitor_button.bind('<Return>', self.start_monitor)

        self.main_view.controls_view.exit_button.bind('<Button>', self.exit_app)
        self.main_view.controls_view.exit_button.bind('<Return>', self.exit_app)

        self.main_view.controls_view.update_data_button.bind('<Button>', self.update_data_now)
        self.main_view.controls_view.update_data_button.bind('<Return>', self.update_data_now)

        self.main_view.app_view.icao1_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao2_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao3_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao4_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao5_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao6_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao7_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao8_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao9_entry.bind('<KeyRelease>', self.caps)
        self.main_view.app_view.icao10_entry.bind('<KeyRelease>', self.caps)

    def run(self):
        """Start the application"""
        self.root.title('AUTO METAR monitor v1.1')
        self.root.deiconify()
        self.root.mainloop()

    def start_monitor(self, event):
        """Start the automatic monitoring of Heathrow QNH, initial value is collected and fields updated
        before setting up scheduled check
        :param event: Start Monitoring button pressed"""
        if not self.monitoring:
            self.monitoring = True
            self.check_metars()
            self.data_check_sched()
            self.main_view.controls_view.monitor_button.configure(text='Monitoring...')
            self.main_view.controls_view.status_label.configure(text=' ')

    def data_check_sched(self):
        """Set a schedule for updating and checking the Heathrow METAR message using a background scheduler. """

        scheduler = BackgroundScheduler()
        trigger = IntervalTrigger(seconds=500)

        scheduler.add_job(self.check_metars, trigger)
        scheduler.start()

    def update_data_now(self, event):
        """Response action for 'Update Now' button press - initiate update of QNH/Time fields.
        :param event: 'Update Now' button pressed.
        """
        self.check_metars()

    def check_metars(self):
        """ Get the latest QNH and obs time readings, check if time is different from last METAR and if
        QNH value has changed from a previous reading. Initiate an Info box message window if QNH has changed and this
        is not the first check"""

        timestamp = str(datetime.datetime.strftime(datetime.datetime.utcnow(), '%d%H%M Z'))
        self.main_view.app_view.time.set(timestamp)

        self.latest_data = get_metarstatus.get_metar_data(self.main_view.app_view.icao1.get(),
                                                          self.main_view.app_view.icao2.get(),
                                                          self.main_view.app_view.icao3.get(),
                                                          self.main_view.app_view.icao4.get(),
                                                          self.main_view.app_view.icao5.get(),
                                                          self.main_view.app_view.icao6.get(),
                                                          self.main_view.app_view.icao7.get(),
                                                          self.main_view.app_view.icao8.get(),
                                                          self.main_view.app_view.icao9.get(),
                                                          self.main_view.app_view.icao10.get())

        self.latest_data_str = ''.join(self.latest_data)
        self.latest_data_str = re.sub('AUTO', 'AUTO \n', self.latest_data_str )

        if re.search('AUTO', self.latest_data_str):

            if self.compare_tuples(self.latest_data, self.old_data):

                self.send_alert('\n{0}'.format(str(self.latest_data_str)))

            self.old_data = self.latest_data

    def compare_tuples(self, t1, t2):
        return sorted(t1) != sorted(t2)

    def send_alert(self, alert_msg):

        tkMessageBox.showwarning('AUTO METAR ALERT', 'Last METAR from following station(s) was AUTO:' + str(alert_msg))

    def caps(self, event):
        """Capatilise characters typed into ICAO boxes
        :param event: Keyboard character typed into an ICAO box."""
        self.main_view.app_view.icao1.set(self.main_view.app_view.icao1.get().upper())
        self.main_view.app_view.icao2.set(self.main_view.app_view.icao2.get().upper())
        self.main_view.app_view.icao3.set(self.main_view.app_view.icao3.get().upper())
        self.main_view.app_view.icao4.set(self.main_view.app_view.icao4.get().upper())
        self.main_view.app_view.icao5.set(self.main_view.app_view.icao5.get().upper())
        self.main_view.app_view.icao6.set(self.main_view.app_view.icao6.get().upper())
        self.main_view.app_view.icao7.set(self.main_view.app_view.icao7.get().upper())
        self.main_view.app_view.icao8.set(self.main_view.app_view.icao8.get().upper())
        self.main_view.app_view.icao9.set(self.main_view.app_view.icao9.get().upper())
        self.main_view.app_view.icao10.set(self.main_view.app_view.icao10.get().upper())

    @staticmethod
    def exit_app(self):
        sys.exit()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
