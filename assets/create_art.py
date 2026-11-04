#!/usr/bin/env python3
"""Original terminal-style profile artwork. Python 3 + pycairo; no network."""
from pathlib import Path
import cairo, math
P=Path(__file__).parent
BG='#131312';PANEL='#1B1B19';LINE='#353532';INK='#F4F4F0';MUTED='#A5A59C'
PIX={'A':['01110','11011','11011','11111','11011','11011','11011'], 'N':['11001','11101','11101','11011','11011','11001','11001'], 'R':['11110','11011','11011','11110','11100','11010','11011'], 'H':['11011','11011','11011','11111','11011','11011','11011'], 'G':['01111','11000','11000','11011','11011','11011','01111'], 'E':['11111','11000','11000','11110','11000','11000','11111'], 'L':['11000','11000','11000','11000','11000','11000','11111'], 'S':['01111','11000','11000','01110','00011','00011','11110']}
def col(c,h):c.set_source_rgb(*(int(h[i:i+2],16)/255 for i in (1,3,5)))
def box(c,x,y,w,h,co,r=0):
 col(c,co)
 if r:
  c.new_sub_path()
  for a,b,d in [(x+w-r,y+r,-90),(x+w-r,y+h-r,0),(x+r,y+h-r,90),(x+r,y+r,180)]:c.arc(a,b,r,math.radians(d),math.radians(d+90))
  c.close_path()
 else:c.rectangle(x,y,w,h)
 c.fill()
def text(c,s,x,y,size=22,co=INK,mono=False,bold=False):
 c.select_font_face('DejaVu Sans Mono' if mono else 'DejaVu Sans',0,cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL);c.set_font_size(size);col(c,co);c.move_to(x,y);c.show_text(s)
def rule(c,x,y,w):box(c,x,y,w,1,LINE)
def base(c,h):box(c,0,0,1200,h,BG,16)
def pixel(c,s,x,y,u):
 for letter in s:
  for row,bits in enumerate(PIX[letter]):
   for i,v in enumerate(bits):
    if v=='1':
     box(c,x+i*u+3,y+row*u+4,u-1,u-2,'#777773')
     box(c,x+i*u,y+row*u,u-1,u-2,INK)
  x+=u*6
def header(c):
 base(c,363);box(c,0,0,1200,40,'#292927',16);box(c,0,22,1200,18,'#292927')
 for i,co in enumerate(['#DF7862','#DFB75F','#85AD7F']):
  col(c,co);c.arc(22+i*19,20,5,0,math.tau);c.fill()
 text(c,'anrhangels@linux: ~',91,26,14,MUTED,True)
 text(c,'$ whoami',38,88,17,MUTED,True)
 pixel(c,'ANRHANGELS',128,116,16)
 rule(c,38,267,1124)
 text(c,'УЧУСЬ. ПРОБУЮ. РАЗБИРАЮСЬ.',38,312,22,INK,True,True)
 text(c,'LINUX / GAMES / AI',905,312,17,MUTED,True)
def about(c):
 base(c,315);text(c,'01 / ABOUT',38,43,16,MUTED,True);rule(c,38,65,1124)
 text(c,'Осваиваю Linux и делаю свои проекты.',38,112,30,INK,False,True)
 for y,s in [(159,'Я новичок в Linux и коде. Настраиваю систему под себя,'),(194,'работаю над Milo Home и пробую запускать игры на Linux.'),(243,'Использую ИИ для обучения: разбираю объяснения и ошибки.'),(278,'Здесь делюсь тем, что получилось, и тем, что ещё не работает.')]:text(c,s,38,y,24,MUTED)
def projects(c):
 base(c,135);text(c,'02 / PROJECTS',38,42,16,MUTED,True)
 text(c,'Для домашнего экрана и любимых игр.',38,91,29,INK,False,True)
def project(c,index,title,status,desc,foot,co):
 base(c,219);box(c,0,18,4,183,co)
 text(c,index,31,49,17,MUTED,True)
 text(c,title,100,53,29,INK,False,True)
 text(c,status,100,89,16,co,True)
 rule(c,100,110,1060)
 text(c,desc,100,151,23,MUTED)
 text(c,foot,100,190,18,MUTED)
 text(c,'↗',1125,53,30,INK)
def milo(c):project(c,'01','Milo Home','ANDROID TV / GOOGLE TV','Простой домашний экран: приложения, пульт и меньше лишнего.','На основе CleanYourTV. Собственные выпуски и инструкции.','#B7C6CF')
def arizona(c):project(c,'02','Arizona RP на Linux','ИГРОВОЙ ЗАПУСК ПРОВЕРЯЛСЯ','Установка, официальный лаунчер, русский текст и эмодзи.','Пошаговая инструкция и скрипт настройки.','#A5B9AA')
def radmir(c):project(c,'03','Radmir CRMP на Linux','ИГРОВОЙ ЗАПУСК ПРОВЕРЯЛСЯ','Установка, библиотеки для графики и помощник музыки.','Графика, музыка и запуск одной командой.','#A5B9AA')
def amazing(c):project(c,'04','Amazing Online на Linux','ЗАПУСК ИГРЫ НЕ ДОСТИГНУТ','Технический отчёт: проведённые тесты, ошибки и выводы.','Сохранил результат неудачной попытки, чтобы он был полезен.','#C8B28C')
def contact(c):
 base(c,110);text(c,'03 / CONTACT',38,42,16,MUTED,True)
 text(c,'Есть вопрос или идея? Можно написать.',38,86,28,INK,False,True)
def contact_card(c,label,handle,action):
 box(c,0,0,588,170,BG,16)
 text(c,label,28,44,19,MUTED,True)
 rule(c,28,64,532)
 text(c,handle,28,115,31,INK,True,True)
 text(c,action,28,148,16,MUTED)
def telegram(c):contact_card(c,'TELEGRAM','@anrhangels','Нажмите, чтобы открыть чат  ↗')
def discord(c):contact_card(c,'DISCORD','anrhangels','Найдите по имени пользователя')
for name,h,fn in [('header',363,header),('about',315,about),('projects',135,projects),('milo',219,milo),('arizona',219,arizona),('radmir',219,radmir),('amazing',219,amazing),('contact',110,contact),('telegram',170,telegram),('discord',170,discord)]:
 for ext in ['png','svg']:
  width=588 if name in ('telegram','discord') else 1200
  surface=cairo.SVGSurface(str(P/(name+'.svg')),width,h) if ext=='svg' else cairo.ImageSurface(cairo.FORMAT_ARGB32,width,h)
  fn(cairo.Context(surface))
  if ext=='png':surface.write_to_png(str(P/(name+'.png')))
  surface.finish()
print('Created 10 PNG cards and editable SVG copies.')
