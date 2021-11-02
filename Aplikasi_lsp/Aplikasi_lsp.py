
from tkinter import *
import mysql.connector as mysqlc
data = []
lsp = Tk()
#memusatkan window saat pertama kali dipanggil
def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

#object
class db:

    def check_connect():
        mydb = mysqlc.connect(
        host = "127.0.0.1",
        user = "root",
        password = '',
        database="xyz"           
        )
        read_db = mydb.cursor()
        print("ok")

    def read():
        mydb = mysqlc.connect(
        host = "127.0.0.1",
        user = "root",
        password = '',
        database="xyz" 
        )
        read_db = mydb.cursor()
        query = ("select * from buku")

        read_db.execute(query)
        
        for i in read_db:
            data.append(i)
        return data

    def update(n,d,k,p,s,h):
        mydb = mysqlc.connect(
        host = "127.0.0.1",
        user = "root",
        password = '',
        database="xyz" 
        )
        read_db = mydb.cursor()
        query = ("INSERT INTO buku (n_buku,deskripsi, kategori, penerbit, stok, harga) VALUES ('%s','%s','%s','%s','%i','%i') ")
        read_db.execute(query %(n,d,k,p,int(s),int(h)))
        mydb.commit()
        
class pembelian:

    pembeli = Tk()
    pembeli.title("XYZ")
    pembeli.geometry("1000x900")


#judul window form awal
lsp.title("XYZ")
#window form tidak bisa diubah ukurannya
lsp.resizable(False,False)

#kumpulan fungsi


def masuk():

    def buku():
        home.deiconify()
        buku = Tk()
        buku.title("XYZ")
        buku.geometry("1000x900")
        center(buku)

        def tambah():
            buku.deiconify()
            tmbh = Tk()

            tmbh.resizable(False,False)

            #kumpulan widget
            l_frame = LabelFrame(tmbh)
            l_frame.pack(fill="none", expand=True)
            n_b = Label(l_frame,text='Nama Buku')
            n_b.pack(fill="none", expand=True)
            en_n = Entry(l_frame)
            en_n.pack(fill="none", expand=True)
            n_d = Label(l_frame,text='deskripsi')
            n_d.pack(fill="none", expand=True)
            en_d = Entry(l_frame)
            en_d.pack(fill="none", expand=True)
            n_k = Label(l_frame,text='Kategori')
            n_k.pack(fill="none", expand=True)
            en_k = Entry(l_frame)
            en_k.pack(fill="none", expand=True)            
            n_p = Label(l_frame,text='penerbit')
            n_p.pack(fill="none", expand=True)
            en_p = Entry(l_frame)
            en_p.pack(fill="none", expand=True) 
            n_s = Label(l_frame,text='stok')
            n_s.pack(fill="none", expand=True)
            en_s = Entry(l_frame)
            en_s.pack(fill="none", expand=True) 
            n_h = Label(l_frame,text='harga')
            n_h.pack(fill="none", expand=True)
            en_h = Entry(l_frame)
            en_h.pack(fill="none", expand=True) 

            subm = Button(l_frame,text="submit",command= lambda: db.update(en_n.get(),en_d.get(),en_k.get(),en_p.get(),en_s.get(),en_h.get()))
            subm.pack(fill="none", expand=True)

            tmbh.geometry("1000x900")
            center(tmbh)
            tmbh.mainloop()




        db.read()
        label = {}
        submit= {}
        j = 0
        for i in data:
            while j < len(data):

                label[i] =Label(buku,text=data[j][1] +"\n"+ data[j][2] +"\n"+ data[j][3]+"\n"+ str(data[j][4])+"\n"+ str(data[j][5])+"\n"+ str(data[j][6]))
                label[i].pack(fill="none", expand=True)

                j+=1


        submit= Button(buku,text='tambah stok',height=2,width=20,command=lambda : tambah())
        submit.pack(fill="none",expand=True)

        update= Button(buku,text='refresh',height=2,width=20,command=lambda : buku.update())
        update.pack(fill="none",expand=True)

        buku.resizable(False,False)
        buku.mainloop()

    lsp.deiconify()
    home = Tk()
    home.title("XYZ")
    home.geometry("1000x900")
    center(home)
    
    buku = Button(home, text="buku",width=20,height=2,command=buku)
    buku.pack(fill="none", expand=True)

    transaksi = Button(home, text="transaksi",width=20,height=2)
    transaksi.pack(fill="none", expand=True)

    pembelian = Button(home, text="pembelian",width=20,height=2)#,command=db.check_connect)
    pembelian.pack(fill="none", expand=True)

    home.mainloop()





#label
lbl1 = Label(lsp,height=2,width=20,text="Toko XYZ")
lbl1.pack(fill="none",expand=True)

#button

masuk = Button(lsp,height=2,width=20,text="masuk",command=masuk)
masuk.pack(fill="none",expand=True)





lsp.geometry("1000x900")

center(lsp)




lsp.mainloop()
