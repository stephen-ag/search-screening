from tkinter import filedialog
from PIL import ImageTk,Image
import PIL.Image
import os
import io
import xlsxwriter
from tkinter import simpledialog
import pandas as pd

from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("1600x750+20+40")
#root.attributes('-fullscreen', True)
#root['bg']='SlateGray3'
root['bg']='#D3D3D3'
root['bd']= 3
# image resizing


#panel = Label(root)
#panel.place(x=1000, y=350)

root.title('Profile Search ')
Label(root,text = "Profile Searching Tool  ", bg="#535386",height ="2",\
      width = "800", fg ="white",
      font = ("Calibri",40)).pack()
Label(root,text = "Note: This tool is specific to a requirement, check the requirement of this tool for process and input data.",
      height ="3",
      width = "400",
      font = ("Calibri",12)).pack()
#--------------------------------------------------------------------------------------

global frame,name

#e1=Entry(root, width =20, font=('Arial 14'),borderwidth = 5)
#e1.pack(padx=10, pady=70)
#Label(root, text="Search String :",font = ("Calibri",13)).place(x = 502, y = 275)
#name= e1.get()
#print(name)

def clearframe():
    print("entering clear function")
        #my_label1.pack_forget()
    root.my_label1.destroy()

def openfile():
    global fpath,name

    fpath = filedialog.askopenfilename()

    if os.path.isfile(fpath)==True:
      location= os.path.basename(fpath)
      print("File selected")
    else:
      print("File not selected        ")
      location= "File not selected"
    frame = Frame(root, width=300, height=50,highlightthickness=2)
    frame.place(x=60, y=375)
    my_label1 = Label(frame, text=location,font=("Arial", 12)).pack()
    print("file OPEN Process completed")

    #my_label1=""
    print(input)
    return(fpath)

global fpath,name

#def sel():
#   name= str(e1.get())
#   return(name)

global tv1
def search():
    global my_label1
    global fpath,name
    greet=openfile
    #input=sel
    # reading the source file which has column name as Resource
    df2 = pd.read_excel(fpath, skiprows=0)
    df2 = df2[df2.filter(regex='^(?!Unnamed)').columns]
    print(df2.shape)
    print(df2.columns)
    #execute(fpath)
    print(fpath)
    print("dataframe created")
    
    dfp=df2.copy()
#filter column name as Resource
    dfa=dfp.filter(['Resource'])
    df4=dfa.values.tolist() 
    ser= pd.Series(df4)
    dfff=pd.DataFrame(ser)

    #collecting all names in one column
    sort_df =dfa.explode('Resource') 
    print(sort_df)
    print("  compilation complete !!")

# collect pdf file names  of candidated from the folder
    dirr=os.path.dirname(fpath)
    files_pdf = [i for i in os.listdir(dirr) if i.endswith('.pdf')]

# remove the prefix of Naukri_ fromthe resume list

    dfs = pd.DataFrame(files_pdf, columns=['Names'])
    dfss=dfs['Names'].str.removeprefix('Naukri_')
    dfss.to_excel("sorted.xlsx")
    print(dfss)
#---------------------------------
    #clear_data()
    name=simpledialog.askstring(title=" Input ", prompt="Input String =")

    result=df2[df2.apply(lambda row: row.astype(str).str.contains(name, case=False).any(), axis=1)]
    #if result.any()==True:
    print(result)
    frame = LabelFrame(root, text="Filtered data")
    frame.place(x=360, y=300)
    #frame.place(height=250, width=500)
    my_label1 = Label(frame, text=result,font=("Arial", 12)).pack()  
    #tree views

    tv1=ttk.Treeview(frame)
    tv1.place(relheight=1,relwidth=1) 
 
    treescrolly=ttk.Scrollbar(frame, orient ="vertical",command=tv1.yview)  
    treescrollx=ttk.Scrollbar(frame, orient ="horizontal",command=tv1.xview)  
    tv1.configure(yscrollcommand = treescrolly.set, xscrollcommand = treescrollx.set)

    treescrolly.pack(side="right", fill="y")
    treescrollx.pack(side="bottom", fill="x")

 
    tv1["columns"]=list(result.columns)
    tv1["show"] ="headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)
    df_rows=result.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("","end", values = row)

def clear_data():
    tv1.delete(*tv1.get_children())

def close():

    root.destroy()

print("entering button controls")
#---------------------------------

button1 = Button(root,text = "  Select i/p Excel File", height ="2", width = "25",\
                 font = ("Calibri",13),bg="#A4A4D3",fg ="black", command = openfile)
button1.place(x = 60, y = 307)

#---------------------------------
#---------------------------------

button2 = Button(root,text = "  Search ",height ="2", width = "25",\
                 font = ("Calibri",13),bg="#B0B0E2",fg ="black", command =search)
button2.place(x = 60, y = 520)

#--------------------------------
button6 = Button(root,text = " Close ",height ="2", width = "25",\
                 font = ("Calibri",13),bg="#BBBBFF",fg ="black", command = close)
button6.place(x = 60, y = 600)
#--------------------------------

#-------------------------------

label = Label(root)
label.pack()
root.mainloop()



	