from ctypes import alignment
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from data_witch import *
#colors
co0="#444466"
co1="#feffff"
co2="#6f9fbd"
co3="#403d3d"

window = Tk()
window.title("")
window.geometry('550x700')
window.resizable(width=FALSE, height=FALSE)
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0,column=1,ipadx=272)

main_frame=Frame(window, width=500, height=520, bg=co2)
main_frame.grid(row=0,column=0, padx=1, pady=1)

def choose_witch(i):
    global icon_1, img_witch
    main_frame['bg']=witch[i]['others'][1]

    witch_name['text'] = i
    witch_name['bg']=witch[i]['others'][1]
    witch_element['text'] = witch[i]['type'][1]
    witch_element['bg']=co3
    witch_number['text']=witch[i]['type'][0]
    witch_number['bg']=witch[i]['others'][1]

    image=witch[i]['others'][0]
    img_witch = Image.open(image)
    img_witch = img_witch.resize((230,450))
    img_witch=ImageTk.PhotoImage(img_witch)

    l_icon_1 = Label(main_frame, image=img_witch, bg=witch[i]['others'][1])
    l_icon_1.place(x=60,y=50)

    #loading status
    hp_status['text']=witch[i]['status'][0]
    power['text']=witch[i]['status'][1]
    defence['text']=witch[i]['status'][2]
    speed['text']=witch[i]['status'][3]
    witch_tot['text']=witch[i]['status'][4]

    # loading skills
    skill_1['text']=witch[i]['skills'][0]
    skill_2['text']=witch[i]['skills'][1]
    skill_3['text']=witch[i]['skills'][2]
 
    witch_element.lift()
    witch_number.lift()
witch_name=Label(main_frame,text="Witch Name", anchor="center", font=("Ivy 20 bold"), fg=co0)
witch_name.place(x=15,y=15)

witch_element = Label(main_frame, text="Element", anchor="center", font=("Ivy 10 bold"), fg=co1)
witch_element.place(x=20, y=50)

witch_number = Label(main_frame, text="Witch number", anchor="center", font=("Ivy 10 bold"), fg=co1)
witch_number.place(x=20, y=75)

witch_element.lift()
witch_number.lift()
# Witch image
# img_witch = Image.open('images_witch/will.png')
# img_witch = img_witch.resize((260,520))
# img_witch=ImageTk.PhotoImage(img_witch)

# l_icon_1 = Label(window, image=img_witch)
# l_icon_1.place(x=60,y=50)


# status-----------------------------
witch_status = Label(window, text="Status", font=("Verdana 20 bold"), bg=co1, fg=co0)
witch_status.place(x=15, y=525)

hp_status=Label(window, text="HP:60",font=("Verdana 12 bold"), bg=co1,fg=co0)
hp_status.place(x=20, y=570)

power=Label(window, text="Power:80",font=("Verdana 12 bold"), bg=co1,fg=co0)
power.place(x=20, y=595)

defence=Label(window, text="Defence:70",font=("Verdana 12 bold"), bg=co1,fg=co0)
defence.place(x=20, y=620)

speed=Label(window, text="Speed:80",font=("Verdana 12 bold"), bg=co1,fg=co0)
speed.place(x=20, y=645)

witch_tot=Label(window, text="Total:290",font=("Verdana 12 bold"), bg=co1,fg=co0)
witch_tot.place(x=20, y=670)

#Skills----------------------------------------
skill=Label(window, text="Skills",font=("Verdana 20 bold"), bg=co1,fg=co0)
skill.place(x=180, y=525)

skill_1=Label(window, text="Thunder Bolt", font=("Verdana 12 bold"), bg=co1, fg=co0)
skill_1.place(x=185, y=570)

skill_2=Label(window, text="Energy Explosion", font=("Verdana 12 bold"), bg=co1, fg=co0)
skill_2.place(x=185, y=595)

skill_3=Label(window, text="Lightning Sphere", font=("Verdana 12 bold"), bg=co1, fg=co0)
skill_3.place(x=185, y=620)

# loading all guardians-----------------------------------------------------------------
# will_icon
img_will=Image.open('images_witch/will_s.png')
img_will=img_will.resize((80,80))
img_will=ImageTk.PhotoImage(img_will)

icon_1=Button(window,text='Will Vandom',command=lambda:choose_witch('Will'), width=200,height=80, image=img_will, padx=6, compound=LEFT, overrelief=RIDGE, anchor=NW,font=("Verdana 11 bold"), bg=co1, fg=co0)
icon_1.place(x=320,y=25)
# irma_icon
img_irma=Image.open('images_witch/irma_s.png')
img_irma=img_irma.resize((80,80))
img_irma=ImageTk.PhotoImage(img_irma)

icon_2=Button(window,text='Irma Layer',command=lambda:choose_witch('Irma'), width=200, height=80,image=img_irma, padx=6, compound=LEFT, overrelief=RIDGE, anchor=NW,font=("Verdana 11 bold"), bg=co1, fg=co0)
icon_2.place(x=320,y=125)
# taranee_icon
img_taranee=Image.open('images_witch/taranee_s.png')
img_taranee=img_taranee.resize((70,80))
img_taranee=ImageTk.PhotoImage(img_taranee)

icon_3=Button(window,text='Taranee Cook',command=lambda:choose_witch('Taranee'), width=200,height=80, image=img_taranee, padx=6, compound=LEFT, overrelief=RIDGE, anchor=NW,font=("Verdana 11 bold"), bg=co1, fg=co0)
icon_3.place(x=320,y=225)
# cornelia_icon
img_corni=Image.open('images_witch/corni_s.png')
img_corni=img_corni.resize((80,80))
img_corni=ImageTk.PhotoImage(img_corni)

icon_4=Button(window,text='Cornelia Hale',command=lambda:choose_witch('Cornelia'), width=200,height=80, image=img_corni, padx=6, compound=LEFT, overrelief=RIDGE, anchor=NW,font=("Verdana 11 bold"), bg=co1, fg=co0)
icon_4.place(x=320,y=325)
# haylin_icon
img_haylin=Image.open('images_witch/haylin_s.png')
img_haylin=img_haylin.resize((80,80))
img_haylin=ImageTk.PhotoImage(img_haylin)

icon_5=Button(window,text='Hay Lin',command=lambda:choose_witch('Hay Lin'), width=200,height=80, image=img_haylin, padx=6, compound=LEFT, overrelief=RIDGE, anchor=NW,font=("Verdana 11 bold"), bg=co1, fg=co0)
icon_5.place(x=320,y=425)

choose_witch('Will')
window.mainloop()