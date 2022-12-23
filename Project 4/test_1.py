import tkinter as tk
import pytest



#root = tk.Tk()

#my_label = tk.Label(root, text = "Howfar")
#my_entry = tk.Entry(root)
#my_button = tk.Label(root, text = "Touch me")

#my_label.pack()
#my_entry.pack()
#my_button.pack()

#root.mainloop()
prev_lowest = -500


def main():
    window= tk.Tk()
    window.title("Show Label and Button Widgets")
    window.geometry("400x200")

   
    
    
    # create an Entry and a label with some text 
    entry1 = tk.Entry(window)
    label1 = tk.Label(window, text="I am here")
    #name_Tf= tk.Entry(window)
    #name = entry1.get()
    entry2 = tk.Entry(window) 
    entry3 = tk.Entry(window)
    entry4 = tk.Entry(window)
    entry5 = tk.Entry(window)
    entry6 = tk.Entry(window)
    entry7 = tk.Entry(window)
    entry8 = tk.Entry(window)
    entry9 = tk.Entry(window)
    entry10 = tk.Entry(window)



    assert (entry1.get()=="")
        #print(" entry created passed")

    assert (label1.cget("text")=="I am here")
        #print("Label has been passed")

       

    
    
    # place entry and label in window at position x,y 
    entry1.place(x= 130, y=20)
    label1.place(x=130,y=50)
    entry2.place(x=230, y=20)
    entry3.place(x=330, y=20)
    entry4.place(x=430, y=20)
    entry5.place(x=530, y=20)
    entry6.place(x=630, y=20)
    entry7.place(x=730, y=20)
    entry8.place(x=830, y=20)
    entry9.place(x=930, y=20)
    entry10.place(x=1030, y=20)
    #txt = entry1.get()
    #entry1.place(x=150, y=20

    def btn1_click():
        array = []
        array.append(entry1.get())
        array.append(entry2.get())
        array.append(entry3.get())
        array.append(entry4.get())
        array.append(entry5.get())
        array.append(entry6.get())
        array.append(entry7.get())
        array.append(entry8.get())
        array.append(entry9.get())
        array.append(entry10.get())
        lowest = int(array[0])

        for element in array:
            if int(element)<lowest and int(element)>btn1_click.prev_lowest:
                lowest = int(element)
        
        btn1_click.prev_lowest = lowest
        label1.configure(text = lowest)
    btn1_click.prev_lowest = -500

    # create a button with text Button 1
    btn1 = tk.Button(window, text="Click Me", command=btn1_click)
    # place this button in window at position x,y 
    btn1.place(x=150,y=100)
    window.mainloop()
    

main()