import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import adi
import matplotlib

matplotlib.use('TkAgg')


'''----------------------- Arayüz ----------------------------'''
# GUI Ayarları
root = tk.Tk()
resolution = "1920x1080"
root.geometry(resolution)
root.title("Spektrum Analizör")
width_r, height_r = resolution.split("x")[0], resolution.split("x")[1]
plt.style.use('dark_background')

ana_frame = tk.Frame(root)
ana_frame.pack(fill=tk.BOTH)

''' -------------------------------------- ekranın sol tarafı -------------------------------------------------------'''
sol_frame = tk.Frame(ana_frame, width=int(width_r) * 0.3, height=height_r)
sol_frame.pack(side="left", fill=tk.BOTH)

style = ttk.Style()
style.configure("Vertical.TScrollbar", background="black", bordercolor="black", arrowcolor="white")

sol_scrollbar = ttk.Scrollbar(sol_frame, style="Vertical.TScrollbar")
sol_scrollbar.grid(row=0, column=1, sticky=tk.NSEW)

sol_canvas = tk.Canvas(sol_frame, height=height_r, yscrollcommand=sol_scrollbar.set)
sol_canvas.grid(row=0, column=0, sticky=tk.NSEW)
sol_scrollbar.config(command=sol_canvas.yview)

'''------------------------------ayar menüsü-----------------------------------'''

'''----------------------------- filtre Ayarlari ------------------------------'''
filtre_Ayarlari_frame = tk.Frame(sol_canvas, relief=tk.GROOVE, padx=int(width_r) * 0.025)
filtre_Ayarlari_frame.grid(row=0, column=0, sticky=tk.NSEW)
sol_canvas.create_window(0, 0, window=filtre_Ayarlari_frame, anchor='nw')
filtre_Ayarlari = tk.Label(filtre_Ayarlari_frame, text="Filtre Ayarları", padx=int(width_r) * 0.022, font="Verdana 15")
filtre_Ayarlari.grid(row=0, column=0, sticky=tk.NSEW)
w1 = tk.Scale(filtre_Ayarlari_frame, from_=0, to=40, tickinterval=20, orient='horizontal')
w1.grid(row=1, column=0, sticky=tk.NSEW)

'''--------------------------- Gorunum Ayarlari ---------------------------------'''
gorunum_Ayarlari_frame = tk.Frame(sol_canvas, relief=tk.GROOVE, padx=int(width_r) * 0.0235)
gorunum_Ayarlari_frame.grid(row=1, column=0, sticky=tk.NSEW)
sol_canvas.create_window(0, 100, window=gorunum_Ayarlari_frame, anchor='nw')
gorunum_Ayarlari = tk.Label(gorunum_Ayarlari_frame, text="Görünüm Ayarları", padx=int(width_r) * 0.015,
                            font="Verdana 15")
gorunum_Ayarlari.grid(row=0, column=0, sticky=tk.NSEW)
w12 = tk.Scale(gorunum_Ayarlari_frame, from_=0, to=40, tickinterval=20, orient='horizontal')
w12.grid(row=1, column=0, sticky=tk.NSEW)

'''------------------------------------------------ ekranın orta tarafı ---------------------------------------------'''
frekans = 3
genlik = 1


def frekans_guncelle(new_frekans):
    global frekans, button_baslat
    if button_baslat.get() == "Durdur":
        frekans = int(new_frekans)
        gencelle_alinan_sinyal()


def gencelle_genlik(new_genlik):
    global frekans, button_baslat, genlik
    if button_baslat.get() == "Durdur":
        genlik = int(new_genlik)
        gencelle_alinan_sinyal()


def gencelle_alinan_sinyal():
    global frekans, genlik, fig, spec_data, spec

    if button_baslat.get() == "Durdur":
        # gelen data
        alinan_sinyal = np.abs(pluto.rx())
        # gelen sinyalı çizdir
        line1.set_ydata(alinan_sinyal)
        # spektrumu çizdir
        # spec_data[:-1] = spec_data[1:]
        # spec_data[-1] = np.abs(np.fft.fft(alinan_sinyal))
        # spec.set_data(10 * np.log10(spec_data))
        line2.set_ydata(np.abs(np.fft.fft(alinan_sinyal)))

        fig.canvas.draw()
        root.after(1, gencelle_alinan_sinyal)

# figure aç
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 9.5), layout="tight")
spec_data = np.zeros((1000, 1024))

orta_frame = tk.Frame(ana_frame, height=height_r)
orta_frame.pack(side="left")

'''------------------------ Anlik sinyal ve spektrum akış zaman  Grafik ----------------------------------'''
anlik_grafik = tk.Frame(orta_frame, height=int(height_r) * 0.5)
anlik_grafik.pack(side="bottom", fill=tk.BOTH)
anlik_grafik_canvas = FigureCanvasTkAgg(fig, anlik_grafik)
anlik_grafik_canvas.get_tk_widget().pack(fill=tk.BOTH)
anlik_grafik_canvas.tkcanvas.pack(side="bottom", fill=tk.BOTH, expand=1)

toolbar_frame = tk.Frame(orta_frame)
toolbar_frame.pack(side="top", fill=tk.BOTH)

toolbar = NavigationToolbar2Tk(anlik_grafik_canvas, toolbar_frame)
toolbar.update()
toolbar.pack(side="left", fill=tk.BOTH)

msg_log_txt = tk.Text(toolbar_frame, height=2)
msg_log_txt.pack(side="right", fill=tk.BOTH)
msg_log_txt.tag_configure("green", foreground="green")
msg_log_txt.tag_configure("red", foreground="red")
msg_log_txt.tag_configure("orange", foreground="orange")


msg_log_label = tk.Label(toolbar_frame, text="Message Log:")
msg_log_label.pack(side="right", fill=tk.BOTH)
'''-------------------------------------------- ekranın sağ tarafı --------------------------------------------------'''
sag_frame = tk.Frame(ana_frame, width=int(width_r) * 0.3, height=height_r)
sag_frame.pack(side="left", fill=tk.BOTH)

sag_scrollbar = ttk.Scrollbar(sag_frame, style="Vertical.TScrollbar")
sag_scrollbar.grid(row=0, column=0, sticky=tk.NSEW)

sag_canvas = tk.Canvas(sag_frame, height=height_r, yscrollcommand=sag_scrollbar.set)
sag_canvas.grid(row=0, column=1, sticky=tk.E)
sag_scrollbar.config(command=sag_canvas.yview)


def pozisyon_degistir(entry_widget, slide_bar):
    value = entry_widget.get()
    if value:
        slide_bar.set(int(value))
    else:
        messagebox.showerror("Error", "Değer Girilmemiş")


'''------------------------ Adalm Pluto Ayarlari ----------------------------------'''
adalmPlutoAyarlari_frame = tk.Frame(sag_canvas, relief=tk.GROOVE, padx=int(width_r) * 0.03)
sag_canvas.create_window(0, 0, window=adalmPlutoAyarlari_frame)

adalmPlutoAyarlari = tk.Label(adalmPlutoAyarlari_frame, text="ADALM-PLUTO Ayarları", font="Verdana 15")
adalmPlutoAyarlari.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)


def basla_durdur():
    global pluto, line1, line2, fig, ax1, ax2, center_freq_entery, samp_rate_entery, num_samps_entery, gain_entery, spec, spec_data


    if button_baslat.get() == "Başlat":
        try:
            pluto = adi.Pluto(uri=f"ip:{ip_entery.get()}")

            log_date = datetime.now().strftime("%H:%M:%S")
            msg_log_txt.insert("1.0", f"[{log_date}]: Cihaz Bağlandı.\n", "green")

        except:
            # messagebox.showerror("Error", "Cihaza bağlanılamadı.")
            msg_log_txt.delete("1.0", tk.END)
            log_date = datetime.now().strftime("%H:%M:%S")
            msg_log_txt.insert("1.0", f"[{log_date}]: Cihaz Bulunmadı.\n", "red")
            return

        else:
            button_baslat.set("Durdur")
            pluto.gain_control_mode_chan0 = 'manual'
            # pluto.rx_hardwaregain_chan0 = int(gain_entery.get())   # dB
            # pluto.rx_lo = int(center_freq_entery.get())
            # pluto.sample_rate = int(samp_rate_entery.get())
            pluto.rx_rf_bandwidth = int(samp_rate_entery.get())
            # pluto.rx_buffer_size = int(num_samps_entery.get())

            line1, = ax1.plot(np.abs(pluto.rx()))
            # spektrumu hesapla
            # spec_data = np.zeros((1000, 1024))
            # spec = ax2.imshow(spec_data, origin="lower", aspect="auto", cmap="jet", vmin=-120, vmax=0)
            line2, = ax2.plot(np.abs(np.fft.fft(pluto.rx())))
            ax1.set_ylabel("Amplitude (V)")
            ax1.set_xlabel("Time (samples)")
            ax1.set_ylim([-200, 1000])
            ax2.set_xlabel("Frequency (Hz)")
            ax2.set_ylabel("wwwwwwww")

            gencelle_alinan_sinyal()
    else:
        button_baslat.set("Başlat")
        log_date = datetime.now().strftime("%H:%M:%S")
        msg_log_txt.insert("1.0", f"[{log_date}]: Cihaz Durduruldu.\n", "orange")
        ax1.clear()
        ax2.clear()


ip_addr = tk.StringVar()
ip_addr.set("192.168.2.1")
ip_label = tk.Label(adalmPlutoAyarlari_frame, text="IP Address: ")
ip_label.grid(row=1, column=0,sticky=tk.W)
ip_entery = tk.Entry(adalmPlutoAyarlari_frame, textvariable=ip_addr, width=10)
ip_entery.grid(row=1, column=1)

center_freq = tk.StringVar()
center_freq.set("100000000") # Hz 2.45GHz
center_freq_label = tk.Label(adalmPlutoAyarlari_frame, text="Başlangıç frekans: ")
center_freq_label.grid(row=2, column=0)
center_freq_entery = tk.Entry(adalmPlutoAyarlari_frame, textvariable=center_freq, width=10)
center_freq_entery.grid(row=2, column=1)

num_samps = tk.StringVar()
num_samps.set("10000") # number of samples per call to rx()
num_samps_label = tk.Label(adalmPlutoAyarlari_frame, text="Son frekans: ")
num_samps_label.grid(row=3, column=0,sticky=tk.W)
num_samps_entery = tk.Entry(adalmPlutoAyarlari_frame, textvariable=num_samps, width=10)
num_samps_entery.grid(row=3, column=1)

samp_rate = tk.StringVar()
samp_rate.set("1000000") # MHz
samp_rate_label = tk.Label(adalmPlutoAyarlari_frame, text="Sample rate: ")
samp_rate_label.grid(row=4, column=0,sticky=tk.W)
samp_rate_entery = tk.Entry(adalmPlutoAyarlari_frame, textvariable=samp_rate, width=10)
samp_rate_entery.grid(row=4, column=1)

gain = tk.StringVar()
gain.set("70.0") # MHz
gain_label = tk.Label(adalmPlutoAyarlari_frame, text="Gain: ")
gain_label.grid(row=5, column=0,sticky=tk.W)
gain_entery = tk.Entry(adalmPlutoAyarlari_frame, textvariable=gain, width=10)
gain_entery.grid(row=5, column=1)

button_baslat = tk.StringVar()
button_baslat.set("Başlat")
button_baslat1 = ttk.Button(adalmPlutoAyarlari_frame, textvariable=button_baslat, command=basla_durdur, width=2)
button_baslat1.grid(row=6, column=0, columnspan=2, sticky=tk.NSEW)

'''------------------------ Frekans Ayarlari -------------------------------------'''
frekansAyarlari_frame = tk.Frame(sag_canvas, relief=tk.GROOVE, padx=int(width_r) * 0.03)
sag_canvas.create_window(0, 250, window=frekansAyarlari_frame)

frekansAyarlari = tk.Label(frekansAyarlari_frame, text="Frekans (MHz)", font="Verdana 15")
frekansAyarlari.grid(row=0, column=0, sticky=tk.NSEW)

'''------------- Değer girme kutusu ---------------'''
w3_e = ttk.Entry(frekansAyarlari_frame, width=4)
w3_e.grid(row=1, column=0, sticky=tk.NSEW)

'''------------- frekans slidebar -----------------'''
w3 = tk.Scale(frekansAyarlari_frame, from_=0, to=40, tickinterval=20, orient='horizontal', command=frekans_guncelle)
w3.grid(row=2, column=0, sticky=tk.NSEW)

'''------------- frekans ayarlama düğmesi ---------'''
w3_b = ttk.Button(frekansAyarlari_frame, text='Pozisyon Degistir', command=lambda: pozisyon_degistir(w3_e, w3))
w3_b.grid(row=3, column=0, sticky=tk.NSEW)

'''------------------------ Bant Genisligi Ayarlari ----------------------------------'''
bantGenisligiAyarlari_frame = tk.Frame(sag_canvas, relief=tk.GROOVE, padx=int(width_r) * 0.03)
sag_canvas.create_window(0, 450, window=bantGenisligiAyarlari_frame)

bantGenisligiAyarlari = tk.Label(bantGenisligiAyarlari_frame, text="Bant Genişliği (kHz)", font="Verdana 15")
bantGenisligiAyarlari.grid(row=0, column=0, sticky=tk.NSEW)
w4_e = ttk.Entry(bantGenisligiAyarlari_frame, width=4)
w4_e.grid(row=1, column=0, sticky=tk.NSEW)
w4 = tk.Scale(bantGenisligiAyarlari_frame, from_=0, to=40, tickinterval=20, orient='horizontal')
w4.grid(row=2, column=0, sticky=tk.NSEW)
w4_b = ttk.Button(bantGenisligiAyarlari_frame, text='Pozisyon Degistir', command=lambda: pozisyon_degistir(w4_e, w4))
w4_b.grid(row=3, column=0, sticky=tk.NSEW)

'''----------------------------- Kazanc Ayarlari -----------------------------------'''
kazancAyarlari_frame = tk.Frame(sag_canvas, relief=tk.GROOVE, padx=int(width_r) * 0.03)
sag_canvas.create_window(0, 650, window=kazancAyarlari_frame)

kazancAyarlari = tk.Label(kazancAyarlari_frame, text="Kazanç (dB)", font="Verdana 15")
kazancAyarlari.grid(row=0, column=0, sticky=tk.NSEW)

'''------------- Değer girme kutusu ---------------'''
w5_e = ttk.Entry(kazancAyarlari_frame, width=4)
w5_e.grid(row=1, column=0, sticky=tk.NSEW)

'''----------*-- Kazanç ayarlama slidebar ---------'''
w5 = tk.Scale(kazancAyarlari_frame, from_=0, to=40, tickinterval=20, orient='horizontal', command=gencelle_genlik)
w5.grid(row=2, column=0, sticky=tk.NSEW)

'''------------- Kazanç ayarlama düğmesi -----------'''
w5_b = ttk.Button(kazancAyarlari_frame, text='Pozisyon Degistir', command=lambda: pozisyon_degistir(w5_e, w5))
w5_b.grid(row=3, column=0, sticky=tk.NSEW)

# verilen ayarlara göre sinyalı güncelle
adalmPlutoAyarlari_frame.update_idletasks()
frekansAyarlari_frame.update_idletasks()
bantGenisligiAyarlari_frame.update_idletasks()
kazancAyarlari_frame.update_idletasks()
sag_canvas.config(scrollregion=sag_canvas.bbox('all'))
filtre_Ayarlari_frame.update_idletasks()
gorunum_Ayarlari_frame.update_idletasks()
sol_canvas.config(scrollregion=sol_canvas.bbox('all'))

# GUI çalıştır
root.mainloop()
