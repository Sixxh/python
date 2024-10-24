# faca um programa em python que abra e reproduza o audio de um arquivo mp3
#from playsound import playsound
#playsound('C:/Users/Sixh/Downloads/Martin-Solveig-Hello.mp3')
#print('Playing sound with playsound')
#professor
import pygame
pygame.init()
pygame.mixer.music.load('exercicios\ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()