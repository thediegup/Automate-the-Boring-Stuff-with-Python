close all, clear all, clc
Fs = 21000
F = [392 784 1176 1568 1960]
A = [32.64 9.748 13.15 2.388 3.627]
P = [angle(392) angle(784) angle(1176) angle(1568) angle(1960)]
Y = 0
t= 1:Fs
for i=1:length(F)
    Y = Y + A(i)*sin(2*pi*F(i)*t/Fs + P(i));
end
env = envelope(Y,40,'rms')
Yrec = Y.*env/5000;
figure,plot(abs(fft(Yrec))),grid on, title("Espectro de amplitud de la señal generada")
sound(Yrec, Fs)

