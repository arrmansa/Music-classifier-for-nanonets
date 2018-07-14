import os
import wave
import numpy as np
import matplotlib.pyplot as plt
import pylab
import gc
def graph_spectrogram(wav_file,name):
    sound_info, frame_rate, channels = get_wav_info("songs/" + wav_file)
    sound_info = sound_info[::int(channels)]
    NFFT = 4096    # the length of the windowing segments
    Fs = frame_rate  # the sampling rate
    for start_time in np.arange(0*int(5*frame_rate),len(sound_info),int(5*frame_rate)):
        data = np.asarray(sound_info)[start_time:(start_time+5*frame_rate)]
        name = str((start_time*2)/frame_rate)
        # plot signal and spectrogram
        data, freqs, bins, im = plt.specgram(data ,NFFT=NFFT, Fs=Fs,window = np.hamming(NFFT),noverlap=NFFT-128)
        ax3 = plt.subplot(111)
        plt.pcolormesh(bins, freqs, 10 * np.log10(data), cmap=plt.cm.plasma)
        plt.axis('off')
        ax3.set_yscale('log')
        plt.ylim(20,10000)    
        ax3.axes.get_xaxis().set_visible(False)
        ax3.axes.get_yaxis().set_visible(False)
        plt.savefig(wav_file[:-4]+name+'.png', bbox_inches='tight', pad_inches = 0)
        #plt.show()
        del data, freqs, bins, im
        plt.close()
        gc.collect()
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    channels = wav.getnchannels()
    wav.close()
    return sound_info, frame_rate, channels
for filename in os.listdir("songs/"):
    if filename.endswith(".wav"):
        graph_spectrogram(filename,filename)

