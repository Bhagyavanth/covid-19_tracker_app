from tkinter import ttk
from tkinter import *
from webscrapinggui import *
# Gui
country_list=['USA', 'Brazil', 'India', 'Russia', 'South Africa', 'Peru', 'Mexico', 'Colombia', 'Spain', 'Chile', 'Iran', 'Argentina', 'UK', 'Saudi Arabia', 'Bangladesh', 'Pakistan', 'Italy', 'Turkey', 'France', 'Germany', 'Iraq', 'Philippines', 'Indonesia', 'Canada', 'Qatar', 'Bolivia', 'Ukraine', 'Ecuador', 'Israel', 'Kazakhstan', 'Egypt', 'Dominican Republic', 'Panama', 'Sweden', 'Oman', 'Belgium', 'Kuwait', 'Romania', 'Belarus', 'Guatemala', 'Netherlands', 'UAE', 'Poland', 'Japan', 'Singapore', 'Portugal', 'Honduras', 'Morocco', 'Nigeria', 'Bahrain', 'Ethiopia', 'Ghana', 'Kyrgyzstan', 'Armenia', 'Algeria', 'Venezuela', 'Switzerland', 'Uzbekistan', 'Afghanistan', 'Azerbaijan', 'Costa Rica', 'Moldova', 'Nepal', 'Kenya', 'Serbia', 'Ireland', 'Austria', 'Australia', 'El Salvador', 'Czechia', 'Palestine', 'Cameroon', 'Bosnia and Herzegovina', 'S. Korea', 'Ivory Coast', 'Denmark', 'Bulgaria', 'Madagascar', 'Paraguay', 'North Macedonia', 'Lebanon', 'Senegal', 'Sudan', 'Libya', 'Zambia', 'Norway', 'DRC', 'Malaysia', 'Greece', 'Guinea', 'Albania', 'French Guiana', 'Croatia', 'Tajikistan', 'Gabon', 'Haiti', 'Finland', 'Luxembourg', 'Maldives', 'Mauritania', 'Namibia', 'Zimbabwe', 'Malawi', 'Djibouti', 'Hungary', 'Equatorial Guinea', 'Hong Kong', 'CAR', 'Nicaragua', 'Montenegro', 'Eswatini', 'Congo', 'Cuba', 'Suriname', 'Mozambique', 'Cabo Verde', 'Rwanda', 'Slovakia', 'Thailand', 'Somalia', 'Mayotte', 'Tunisia', 'Sri Lanka', 'Lithuania', 'Slovenia', 'Mali', 'Gambia', 'Uganda', 'South Sudan', 'Syria', 'Estonia', 'Angola', 'Guinea-Bissau', 'Benin', 'Iceland', 'Sierra Leone', 'Yemen', 'Bahamas', 'Jordan', 'Malta', 'Jamaica', 'New Zealand', 'Aruba', 'Botswana', 'Uruguay', 'Cyprus', 'Georgia', 'Trinidad and Tobago', 'Latvia', 'Burkina Faso', 'Togo', 'Liberia', 'Réunion', 'Niger', 'Andorra', 'Guyana', 'Lesotho', 'Vietnam', 'Chad', 'Guadeloupe', 'Sao Tome and Principe', 'Belize', '163', 'San Marino', 'Channel Islands', 'Myanmar', 'Tanzania', 'Taiwan', 'Martinique', 'Turks and Caicos', 'Burundi', 'Papua New Guinea', 'Sint Maarten', 'Comoros', 'Faeroe Islands', 'French Polynesia', 'Mauritius', 'Isle of Man', 'Eritrea', 'Mongolia', 'Cambodia', 'Gibraltar', 'Cayman Islands', 'Saint Martin', 'Bhutan', 'Bermuda', 'Barbados', 'Brunei ', 'Seychelles', 'Monaco', 'Liechtenstein', 'Antigua and Barbuda', 'St. Vincent Grenadines', 'Curaçao', 'Macao', 'Fiji', 'British Virgin Islands', 'Saint Lucia', 'Timor-Leste', 'Grenada', 'New Caledonia', 'Laos', 'Dominica', 'St. Barth', 'Saint Kitts and Nevis', 'Greenland', 'Montserrat', 'Caribbean Netherlands', 'Falkland Islands', 'Vatican City', 'Western Sahara', '212', 'Saint Pierre Miquelon', 'Anguilla', 'China']

root=Tk()
root.geometry('600x600')
root.resizable(0,0)
root.title('Covid-19 Cases Tracker')
root.configure(bg='purple')


def get_cases():
    webScraping()
    country_name=choice.get()
    cases=get_dic(country_name)
    total_cases_text.delete(1.0, END)
    new_cases_text.delete(1.0, END)
    total_death_text.delete(1.0, END)
    total_recovered_text.delete(1.0, END)
    active_cases_text.delete(1.0, END)
    total_cases_text.insert(END,str(cases[0]))
    new_cases_text.insert(END,str(cases[1]))
    total_death_text.insert(END,str(cases[2]))
    total_recovered_text.insert(END,str(cases[4]))
    active_cases_text.insert(END,str(cases[6]))

def reset_data():
    total_cases_text.delete(1.0, END)
    new_cases_text.delete(1.0, END)
    total_death_text.delete(1.0, END)
    total_recovered_text.delete(1.0, END)
    active_cases_text.delete(1.0, END)




label=Label(root,text='Stay Home Stay Safe',font=('arial', 14,'bold'),
            bg='orange',fg='black',height=2)
label.pack(side=TOP,fill=BOTH)

# select the country
choice=ttk.Combobox(root,values=country_list,height=10)
choice.place(x=220,y=70)
choice.set('India')

total_cases=Label(root,text='Total Cases',font=('arial 20'),bg='purple',fg='black')
total_cases.place(x=90,y=130)

total_cases_text=Text(root,font='arial 10',height=2)
total_cases_text.place(x=300,y=130)

new_cases=Label(root,text='New Cases',font=('arial 20'),bg='purple',fg='black')
new_cases.place(x=90,y=180)

new_cases_text=Text(root,font='arial 10',height=2)
new_cases_text.place(x=300,y=180)

Total_death=Label(root,text='Total Deaths',font=('arial 20'),bg='purple',fg='black')
Total_death.place(x=90,y=230)

total_death_text=Text(root,font='arial 10',height=2)
total_death_text.place(x=300,y=230)

total_recovered=Label(root,text='Total Recovered',font=('arial 20'),bg='purple',fg='black')
total_recovered.place(x=90,y=280)

total_recovered_text=Text(root,font='arial 10',height=2)
total_recovered_text.place(x=300,y=280)

active_cases=Label(root,text='Active Cases',font=('arial 20'),bg='purple',fg='black')
active_cases.place(x=90,y=330)

active_cases_text=Text(root,font='arial 10',height=2)
active_cases_text.place(x=300,y=330)

# submit button
submit=Button(root,text='SUBMIT',font='arial 15 bold',bg='green',
              fg='blue', activebackground='red',command=get_cases)
submit.place(x=320,y=420)

# reset button
reset=Button(root,text='RESET',font='arial 15 bold',bg='green',
              fg='blue', activebackground='red',command=reset_data)
reset.place(x=150,y=420)

status_bar=Label(root,text='Created by: Bhagyawanth_Avantagi',
                 font=('arial',10,'bold'),bg='sky blue')
status_bar.pack(side=BOTTOM,fill=BOTH)

root.mainloop()


