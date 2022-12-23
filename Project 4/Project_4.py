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


def main():
    window= tk.Tk()
    window.title("Show Label and Button Widgets")
    window.geometry("400x200")

   
    
    
    # create an Entry and a label with some text 
    entry1 = tk.Entry(window)
    label1 = tk.Label(window, text="I am here")
    #name_Tf= tk.Entry(window)
    #name = entry1.get()



    assert (entry1.get()=="")
        #print(" entry created passed")

    assert (label1.cget("text")=="I am here")
        #print("Label has been passed")


    
    
    # place entry and label in window at position x,y 
    entry1.place(x= 130, y=20)
    label1.place(x=130,y=50)
    #txt = entry1.get()

    def btn1_click():
        label1.configure(text = entry1.get())

    # create a button with text Button 1
    btn1 = tk.Button(window, text="Click Me", command=btn1_click)
    # place this button in window at position x,y 
    btn1.place(x=150,y=100)
    window.mainloop()
    

main()
