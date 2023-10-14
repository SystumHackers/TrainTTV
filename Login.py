from tkinter import *


def saveToFile():
    saveFirstName = firstNameEntry.get()
    saveLastName = lastNameEntry.get()
    saveEmail  = email.get()
    savePhone = phone.get()
    


    file = open(r"C:\Users\Akarshan\Python App\Data.txt","a+")
    file.write(saveFirstName)
    file.write(',')
    file.write(saveLastName)
    file.write(',')
    pass
    file.write(',')
    file.write(saveEmail)
    file.write(',')
    file.write(savePhone)
    file.write(',')
  


    file.close()

    firstNameEntry.delete(0,END)
    lastNameEntry.delete(0,END)
    email.delete(0,END)
    phone.delete(0,END)
    




root = Tk()
root.geometry("270x300")

firstName = Label(root, text='First Name: ', fg='black')
firstName.grid(row=0,sticky='E')
lastName = Label(root,text='Last Name: ', fg='black')
lastName.grid(row=1,sticky='E')
email = Label(root,text='Email: ',fg='black')
email.grid(row=4,sticky='E')
phone = Label(root, text='Phone No: ', fg='black')
phone.grid(row=5,sticky='E')

firstNameEntry = Entry()
lastNameEntry = Entry()
email = Entry()
phone = Entry()



firstNameEntry.grid(row=0,column=1)
lastNameEntry.grid(row=1,column=1)
email.grid(row=4,column=1)
phone.grid(row=5,column=1)

submitButton = Button(root,text='Submit ',command=saveToFile,bg='orange',fg='black')
submitButton.place(x=60,y=220,width=150)
#submitButton.grid(row=8,column=1,ipadx=40,ipady=10)
root.quit

quitButton = Button(root, text='Quit',bg='orange',fg='black' ,command=root.quit)
quitButton.place(x=60,y=260,width=150)


root.mainloop()