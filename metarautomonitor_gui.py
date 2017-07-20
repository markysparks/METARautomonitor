#!/usr/bin/env python
import sys

if sys.version_info[0] < 3:
    import Tkinter as tk
    import ttk
else:
    import tkinter as tk
    from tkinter import ttk as ttk

__author__ = 'Mark Baker  email: mark.baker@metoffice.gov.uk'


class MainView:
    """Main GUI class responsible for initiating separate window frames for the various display elements."""

    def __init__(self, master):
        self.frame = ttk.Frame(master)
        self.frame.grid(row=0, column=0, padx=5, pady=5)
        self.app_view = AppView(master)
        self.controls_view = ControlsView(master)


class AppView:
    """Label window frame containing the widgets for displaying Obs time, latest and previous QNH. """

    def __init__(self, root):
        self.frame_metar_monitor = tk.LabelFrame(root, text='AUTO METAR monitor')
        self.frame_metar_monitor.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

        self.time_label = ttk.Label(self.frame_metar_monitor, text="Last Check:", anchor=tk.E)
        self.time_label.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

        self.time = tk.StringVar()
        self.time_result = ttk.Label(self.frame_metar_monitor, textvariable=self.time, width=8, anchor=tk.W)
        self.time_result.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

        self.icao1_label = ttk.Label(self.frame_metar_monitor, text="ICAO :")
        self.icao1_label.grid(row=1, column=0, padx=15, pady=5)

        self.icao1 = tk.StringVar()
        self.icao1_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao1, width=6)
        self.icao1_entry.grid(row=2, column=0, padx=15, pady=5)

        self.icao2_label = ttk.Label(self.frame_metar_monitor, text="ICAO :")
        self.icao2_label.grid(row=1, column=1, padx=15, pady=5)

        self.icao2 = tk.StringVar()
        self.icao2_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao2, width=6)
        self.icao2_entry.grid(row=2, column=1, padx=15, pady=5)

        self.icao3_label = ttk.Label(self.frame_metar_monitor, text="ICAO :")
        self.icao3_label.grid(row=1, column=2, padx=15, pady=5)

        self.icao3 = tk.StringVar()
        self.icao3_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao3, width=6)
        self.icao3_entry.grid(row=2, column=2, padx=15, pady=5)

        self.icao4_label = ttk.Label(self.frame_metar_monitor, text="ICAO :")
        self.icao4_label.grid(row=1, column=3, padx=15, pady=5)

        self.icao4 = tk.StringVar()
        self.icao4_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao4, width=6)
        self.icao4_entry.grid(row=2, column=3, padx=15, pady=5)

        self.icao5_label = ttk.Label(self.frame_metar_monitor, text="ICAO :")
        self.icao5_label.grid(row=1, column=4, padx=15, pady=5)

        self.icao5 = tk.StringVar()
        self.icao5_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao5, width=6)
        self.icao5_entry.grid(row=2, column=4, padx=15, pady=5)

        self.icao6 = tk.StringVar()
        self.icao6_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao6, width=6)
        self.icao6_entry.grid(row=3, column=0, padx=15, pady=5)

        self.icao7 = tk.StringVar()
        self.icao7_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao7, width=6)
        self.icao7_entry.grid(row=3, column=1, padx=15, pady=5)

        self.icao8 = tk.StringVar()
        self.icao8_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao8, width=6)
        self.icao8_entry.grid(row=3, column=2, padx=15, pady=5)

        self.icao9 = tk.StringVar()
        self.icao9_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao9, width=6)
        self.icao9_entry.grid(row=3, column=3, padx=15, pady=5)

        self.icao10 = tk.StringVar()
        self.icao10_entry = ttk.Entry(self.frame_metar_monitor, textvariable=self.icao10, width=6)
        self.icao10_entry.grid(row=3, column=4, padx=15, pady=5)


class ControlsView:
    """ GUI elements - monitoring, update and exit buttons"""
    def __init__(self, root):

        self.frame_controls = ttk.Frame(root)
        self.frame_controls.grid(row=2, column=0, padx=5, pady=5)

        self.monitor_button = ttk.Button(self.frame_controls, text='Start Monitor', width=13)
        self.monitor_button.grid(sticky=tk.W, row=0, column=0, padx=5, pady=5)

        self.status_label = ttk.Label(self.frame_controls, width=10, text='           ')
        self.status_label.grid(sticky=tk.W, row=0, column=1, padx=5, pady=5)

        self.update_data_button = ttk.Button(self.frame_controls, text='Update Now')
        self.update_data_button.grid(sticky=tk.W, row=0, column=4, padx=5, pady=5)

        self.exit_button = ttk.Button(self.frame_controls, text='Exit')
        self.exit_button.grid(sticky=tk.E, row=0, column=5, padx=5, pady=5)

