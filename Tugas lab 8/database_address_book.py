import os
# Clearing the Screen
os.system('cls')
import mysql.connector
from mysql.connector import errorcode

import tkinter as tk
from tkinter import font, messagebox, simpledialog, Label


#connect the python to the host and database 
cnx = mysql.connector.connect(
    host="127.0.0.1", #localhost
    user="root",
    password=""
    )
cursor = cnx.cursor(buffered=True)

# create table columns
address_book = 'address_book'

TABLES = {}
TABLES['address_book'] = (
    "CREATE TABLE `address_book` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `full_name` varchar(25) NOT NULL,"
    "  `address` varchar(200) NOT NULL,"
    "  `number` varchar(30) NOT NULL,"
    "  `email` varchar(20) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

#create the table in the database
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(address_book))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(address_book))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(address_book))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(address_book))
        cnx.database = address_book
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

print("\nIni yang belum di update")
query = ("SELECT id,full_name,address,number FROM `address_book`")
cursor.execute(query)
for (id,full_name,address,number) in cursor:
  print("{}, lives in {}. To Contact the person, this is their number :{}".format(
    full_name,address,number))
  
update_old_address = (
  "UPDATE address_book SET address = 'Esc. 165 Grupo Dorotea Pulido 3, Santander, Mad 44135', number = '45678911'"
  "WHERE id = 1")



#create the tkinter window ============================================================================
# Create the main tkinter window
# root = Tk()
# root.title("Address Book")
# root.geometry('500x500')

class Welcome(tk.Tk) :
    def __init__(self):
        super().__init__()
        self.title("Address Book")
        self.welcome_text() 
        self.seeButton()
        self.addButton()
        self.updateButton()
        self.deleteButton()
        self.closeButton()
    

    #what to do when button is clicked
    def button_clicked_see(self):
        self.show_data()
        # self.destroy()
    def button_clicked_add(self):
        self.addNewAddress("Add new Address Book List")
        # self.destroy()
    def button_clicked_update(self):
        print("ini yg update button")
        self.updateAddress("Update An Address In The Book List")
        # self.destroy()
    def button_clicked_delete(self):
        print("Deleted!")
        self.deleteAddress("Delete An Address Book")
        # self.destroy()

    def button_clicked_close(self):
        print("Closed!")
        cursor.close()
        cnx.close()
        self.destroy()


    def addNewAddress(self, title):
        new_win = tk.Toplevel(self)
        new_win.title(title)
        new_win.geometry("500x500")

        label = tk.Label(new_win, text=f"{title}", font=("Arial", 12))
        label.pack(pady=10)

        # first_id_label = Label(new_win, text="ID Number:")
        # first_id_label.pack()
        # self.id_entry = tk.Entry(new_win, width=30)
        # self.id_entry.pack(pady=5)
        # self.id_entry.insert(0, "Id")

        # self.id_entry = tk.simpledialog.askinteger("ID Input", "Enter the ID:", minvalue=0)
        # self.id_entry.pack(pady=5)

        first_name_label = Label(new_win, text="Full Name:")
        first_name_label.pack()
        self.name_entry = tk.Entry(new_win, width=30)
        self.name_entry.pack(pady=5)
        self.name_entry.insert(0, "")

        first_address_label = Label(new_win, text="Address:")
        first_address_label.pack()
        self.address_entry = tk.Entry(new_win, width=30)
        self.address_entry.pack(pady=5)
        self.address_entry.insert(0, "")

        
        first_phone_label = Label(new_win, text="Phone number:")
        first_phone_label.pack()
        self.phone_entry = tk.Entry(new_win, width=30)
        self.phone_entry.pack(pady=5)
        self.phone_entry.insert(0, "")

        first_email_label = Label(new_win, text="Email:")
        first_email_label.pack()
        self.email_entry = tk.Entry(new_win, width=30)
        self.email_entry.pack(pady=5)
        self.email_entry.insert(0, "")

        # entry = tk.Entry(new_win, width=30)
        # entry.pack(pady=10)

        submit_button = tk.Button(new_win, text="Submit", command=lambda: self.process_input(title))
        submit_button.pack(pady=10)

    def deleteAddress(self, title):
        new_win = tk.Toplevel(self)
        new_win.title(title)
        new_win.geometry("500x200")

        first_phone_label = Label(new_win, text="Phone number:")
        first_phone_label.pack()
        self.phone_entry = tk.Entry(new_win, width=30)
        self.phone_entry.pack(pady=5)
        self.phone_entry.insert(0, "")

        first_email_label = Label(new_win, text="Email:")
        first_email_label.pack()
        self.email_entry = tk.Entry(new_win, width=30)
        self.email_entry.pack(pady=5)
        self.email_entry.insert(0, "")

        submit_button = tk.Button(new_win, text="Submit", command=lambda: self.process_input(title))
        submit_button.pack(pady=10)

    def updateAddress(self, title):
        new_win = tk.Toplevel(self)
        new_win.title(title)
        new_win.geometry("500x500")

        label = tk.Label(new_win, text=f"{title}", font=("Arial", 12))
        label.pack(pady=10)

        old_phone_label = Label(new_win, text="Old Phone number:")
        old_phone_label.pack()
        self.old_phone_entry = tk.Entry(new_win, width=30)
        self.old_phone_entry.pack(pady=5)
        self.old_phone_entry.insert(0, "")

        old_email_label = Label(new_win, text="Old Email:")
        old_email_label.pack()
        self.old_email_entry = tk.Entry(new_win, width=30)
        self.old_email_entry.pack(pady=5)
        self.old_email_entry.insert(0, "")

        new_name_label = Label(new_win, text="New Full Name:")
        new_name_label.pack()
        self.new_name_entry = tk.Entry(new_win, width=30)
        self.new_name_entry.pack(pady=5)
        self.new_name_entry.insert(0, "")

        new_address_label = Label(new_win, text="New Address:")
        new_address_label.pack()
        self.new_address_entry = tk.Entry(new_win, width=30)
        self.new_address_entry.pack(pady=5)
        self.new_address_entry.insert(0, "")
        
        new_phone_label = Label(new_win, text="New Phone number:")
        new_phone_label.pack()
        self.new_phone_entry = tk.Entry(new_win, width=30)
        self.new_phone_entry.pack(pady=5)
        self.new_phone_entry.insert(0, "")

        new_email_label = Label(new_win, text="New Email:")
        new_email_label.pack()
        self.new_email_entry = tk.Entry(new_win, width=30)
        self.new_email_entry.pack(pady=5)
        self.new_email_entry.insert(0, "")

        # entry = tk.Entry(new_win, width=30)
        # entry.pack(pady=10)

        submit_button = tk.Button(new_win, text="Submit", command=lambda: self.process_input(title))
        submit_button.pack(pady=10)

    def show_data(self):
        new_win = tk.Toplevel(self)
        new_win.title("Address Book List")
        new_win.geometry("800x800")
        
        query = ("SELECT id,full_name,address,number FROM `address_book`")
        cursor.execute(query)
        for (id,full_name,address,number) in cursor :
            label_data =tk.Label(new_win, text="{}, lives in {}. To Contact the person, this is their number :{}".format(full_name,address,number))
            label_data.pack()

        # cursor.execute("SELECT * FROM address_book")
        rows = cursor.fetchall()
        # cursor.close()

        for row in rows:
            label = tk.Label(new_win, text=f"ID: {row[0]}, Name: {row[1]}, Address: {row[2]}, Phone: {row[3]}")
            label.pack()

    def welcome_text(self):
        welcome_frame = tk.Frame(master=self)
        welcome_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=welcome_frame,
            text="Address Book",
            font=font.Font(size=14, weight="bold"),
        )
        self.display.pack()

    def seeButton(self):
        # Creating a button with specified options
        self.buttonSee = tk.Button(self, 
                        text="See Address Book List", 
                        command=self.button_clicked_see,
                        activebackground="blue", 
                        activeforeground="white",
                        anchor="center",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        disabledforeground="gray",
                        fg="black",
                        font=("Arial", 12),
                        height=2,
                        highlightbackground="black",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="center",
                        overrelief="raised",
                        padx=10,
                        pady=5,
                        width=15,
                        wraplength=100)
        self.buttonSee.pack(padx=20, pady=20)

    def addButton(self):
        self.buttonAdd = tk.Button(self, 
                        text="Add new Address Book List", 
                        command=self.button_clicked_add,
                        activebackground="blue", 
                        activeforeground="white",
                        anchor="center",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        disabledforeground="gray",
                        fg="black",
                        font=("Arial", 12),
                        height=2,
                        highlightbackground="black",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="center",
                        overrelief="raised",
                        padx=10,
                        pady=5,
                        width=15,
                        wraplength=100)
        self.buttonAdd.pack(padx=20, pady=20)

    def updateButton(self):
        self.buttonUpdate = tk.Button(self, 
                        text="Update An Address In The Book List", 
                        command=self.button_clicked_update,
                        activebackground="blue", 
                        activeforeground="white",
                        anchor="center",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        disabledforeground="gray",
                        fg="black",
                        font=("Arial", 12),
                        height=2,
                        highlightbackground="black",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="center",
                        overrelief="raised",
                        padx=10,
                        pady=5,
                        width=15,
                        wraplength=100)
        self.buttonUpdate.pack(padx=20, pady=20)
    
    def deleteButton(self):
        self.buttonDelete = tk.Button(self, 
                        text="Delete An Address Book", 
                        command=self.button_clicked_delete,
                        activebackground="blue", 
                        activeforeground="white",
                        anchor="center",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        disabledforeground="gray",
                        fg="black",
                        font=("Arial", 12),
                        height=2,
                        highlightbackground="black",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="center",
                        overrelief="raised",
                        padx=10,
                        pady=5,
                        width=15,
                        wraplength=100)
        self.buttonDelete.pack(padx=20, pady=20)

    def closeButton(self):
        self.buttonClose = tk.Button(self, 
                        text="Close The App", 
                        command=self.button_clicked_close,
                        activebackground="blue", 
                        activeforeground="white",
                        anchor="center",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        disabledforeground="gray",
                        fg="black",
                        font=("Arial", 12),
                        height=2,
                        highlightbackground="black",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="center",
                        overrelief="raised",
                        padx=10,
                        pady=5,
                        width=15,
                        wraplength=100)
        self.buttonClose.pack(padx=20, pady=20)

    def process_input(self, title):
        if title == "Add new Address Book List":
            name = self.name_entry.get()
            address = self.address_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()

            try:
                insert_data = ("INSERT INTO address_book (full_name, address, number, email) VALUES (%s, %s, %s, %s)")
                cursor.execute(insert_data, (name, address, phone, email))
                cnx.commit()
                print(f"Data Added: {name}, {address}, {phone}, {email}")
                messagebox.showinfo("Success", "Data Successfully Added")
                # self.destroy()
            except mysql.connector.Error as e:
                print(f"Error: {e}")
                messagebox.showerror("Something went wrong", "Input the data again")

        elif title == "Update An Address In The Book List":
            old_phone = self.old_phone_entry.get()
            old_email = self.old_email_entry.get()

            new_name = self.new_name_entry.get()
            new_address = self.new_address_entry.get()
            new_phone = self.new_phone_entry.get()
            new_email = self.new_email_entry.get()

            try:
                update_data = ("UPDATE address_book SET full_name=%s, address=%s, number=%s, email=%s WHERE number=%s AND email=%s")
                cursor.execute(update_data, (new_name, new_address, new_phone, new_email, old_phone, old_email))
                cnx.commit()
                if cursor.rowcount > 0:
                    print(f"Data Updated: {new_name}, {new_address}, {new_phone}, {new_email}")
                    messagebox.showinfo("Success", "Data Successfully Updated")
                else:
                    print(f"No matching record found for update: {old_phone}, {old_email}")
                    messagebox.showwarning("Warning", "No matching record found")
            except mysql.connector.Error as e:
                print(f"Error: {e}")
                messagebox.showerror("Something went wrong", "Input the data again")

        elif title == "Delete An Address Book":
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            print("Delete Request - Phone:", phone, "Email:", email)

            try:
                if cnx.is_connected():
                    print("Connected to database")
                    delete_data = "DELETE FROM address_book WHERE number=%s AND email=%s"
                    cursor.execute(delete_data, (phone, email))
                    cnx.commit()

                    # Verify deletion
                    cursor.execute("SELECT * FROM address_book WHERE number = %s AND email = %s", (phone, email))
                    result = cursor.fetchall()
                    if not result:
                        print(f"Data Successfully Deleted: {phone}, {email}")
                        messagebox.showinfo("Success", "Data Successfully Deleted")
                    else:
                        print(f"Failed to Delete Data: {phone}, {email}")
                        messagebox.showerror("Error", "Failed to delete data. Please try again.")
                else:
                    print("Error connecting to database")
                    messagebox.showerror("Error", "Failed to connect to database.")
            except mysql.connector.Error as e:
                print(f"Error: {e}")
                messagebox.showerror("Something went wrong", "Input the data again")

def main():
    start = Welcome()
    start.mainloop()

if __name__ == "__main__":
    main()

# # Create labels and entry fields for each input
# first_name_label = Label(root, text="First Name:")
# first_name_label.pack()
# first_name_entry = Entry(root)
# first_name_entry.pack()

# Last_name_label = Label(root, text="Last Name:")
# Last_name_label.pack()
# Last_name_entry = Entry(root)
# Last_name_entry.pack()

# email_label = Label(root, text="Email:")
# email_label.pack()
# email_entry = Entry(root)
# email_entry.pack()

# Mobile_label = Label(root, text="Mobile:")
# Mobile_label.pack()
# Mobile_entry = Entry(root)
# Mobile_entry.pack()

# # Update the old and insert the new salary
# cursor.execute(update_old_address)

# print("\nIni yang setelah di update")

# #loop print the result
# cursor.execute(query)
# for (id,full_name,address,number) in cursor:
#   print("{}, lives in {}. To Contact the person, this is their number :{}".format(
#     full_name,address,number))
  
# #delete a person in the database
# delete = "DELETE FROM address_book WHERE id = '2'"
# cursor.execute(delete)

# # Commit the changes
# cnx.commit()

# print("\nIni yang setelah ada orang yang dihapus")

# #loop print the result
# cursor.execute(query)
# for (id,full_name,address,number) in cursor:
#   print("id : {} | {}, lives in {}. To Contact the person, this is their number :{}".format(
#     id,full_name,address,number))

# cursor.close()
# cnx.close()