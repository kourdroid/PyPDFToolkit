import os
import math
import img2pdf
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from PIL import Image
import PyPDF2
import io
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2 import PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter

from reportlab.pdfgen import canvas


def merge_pdfs(input_paths, output_path):
    
    pdf_merger = PyPDF2.PdfMerger()
    total_pages = 0

    # Get the total number of pages in all the input PDFs
    for path in input_paths:
        with open(path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            total_pages += pdf_reader.getNumPages()

    # Merge the PDFs while updating the progress bar
    current_page = 0
    with open(output_path, 'wb') as output_file:
        for path in input_paths:
            with open(path, 'rb') as pdf_file:
                pdf_merger.append(pdf_file)

                # Update progress after each PDF is appended
                current_page += PyPDF2.PdfFileReader(pdf_file).getNumPages()
                progress_value = int((current_page / total_pages) * 100)
                progress['value'] = progress_value
                progress.update()

        pdf_merger.write(output_file)

def merge_files():
    global entry, pdf_list, progress
    # Get the selected PDF file paths from the listbox
    selected_paths = pdf_list.get(0, tk.END)
    print("Selected PDFs:", selected_paths)

    # Get the destination PDF file path from the entry widget
    destination_path = filedialog.asksaveasfilename(
        defaultextension='.pdf', filetypes=[("PDF files", "*.pdf")]
    )
    # If destination path is empty or contains unwanted characters, ask the user for a valid path
    if not destination_path or "\n" in destination_path:
        destination_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("PDF files", "*.pdf")])
        print("Chosen destination path:", destination_path)

    # Call the merge_pdfs function with the selected PDFs and destination path
    if destination_path:
        merge_pdfs(selected_paths, destination_path)
        print("PDFs merged successfully.")

    # Call the merge_pdfs function with the selected PDFs and destination path
    if destination_path:
        merge_pdfs(selected_paths, destination_path)

def open_pdf_merger():
    global progress
    global entry
    global pdf_list
    merger_window = ttk.Toplevel()
    merger_window.title('PDF MERGER')
    merger_window.geometry('300x500')
    merger_window.resizable(False, False)
    label = ttk.Label(merger_window, text='PDF\nMERGER', foreground='#FF2525' ,font=('Montserrat', 28,'bold'),anchor='center',justify='center')
    label.pack(pady=10)

    DestLabel=ttk.Label(merger_window, text='DESTINATION:', foreground='#232323' ,font=('Montserrat', 10,'bold'),anchor='center',justify='center')
    DestLabel.pack(pady=10)
    DestLabel.place(x=85,y=114,width=130,height=36)

    entry = ttk.Entry(merger_window)
    entry.pack(pady=10)
    entry.place(x=23, y=151, width=255, height=39)
    style = ttk.Style()
    style.configure('TEntry', fieldbackground='#D9D9D9')
    
    style = ttk.Style()
    style.configure('Custom.TButton', font=('Montserrat', 18, 'bold'), foreground='white', background='#FF2525')
    style.map('Custom.TFrame',
          background=[('selected', '#D9D9D9'), ('active', '#D9D9D9')])

    button1 = ttk.Button(merger_window, text='CHOOSE',style='Custom.TButton',compound='center',takefocus=False,command=custom_choose)
    button1.pack(pady=25)
    button1.place(x=81, y=216,width=139,height=39)

    pdf_frame = ttk.Frame(merger_window, style='Custom.TFrame')  # Add style for the frame
    pdf_frame.pack(pady=10, padx=10)
    pdf_frame.place(x=24, y=277, width=252, height=94)

    pdf_list = tk.Listbox(pdf_frame, selectmode=tk.EXTENDED)
    pdf_list.pack(fill=tk.BOTH, expand=True)

    button2 = ttk.Button(merger_window, text='MERGE',style='Custom.TButton',compound='center',takefocus=False, command=merge_files)
    button2.pack(pady=25)
    button2.place(x=81, y=395,width=139,height=39)

    # Assuming you have a root window defined as "window"
    progress = ttk.Progressbar(merger_window, mode='determinate')
    progress.pack(pady=10)
    progress.place(x=23, y=455, width=255, height=18)
    style.configure('TProgressbar', background='#D9D9D9')

def custom_choose():
    # Function for the custom "CHOOSE" button
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if file_paths:
        entry.delete(0, tk.END)  # Clear the current entry value
        for file_path in file_paths:
            if file_path.strip():  # Check if the file_path is not empty after stripping
                entry.insert(tk.END, file_path.strip() + "\n")
                pdf_list.insert(tk.END, file_path.strip())

def check_clipboard():
    data = window.clipboard_get()
    if data and is_image(data):
        entry.delete(0, tk.END)
        entry.insert(tk.END, data + "\n")
        pdf_list.insert(tk.END, data)
    window.after(1000, check_clipboard)

def open_pdf_compress():
    global entry
    global pdf_list
    global progress
    compress_window = tk.Toplevel(window)
    compress_window.title('PDF Compress')
    compress_window.geometry('300x500')
    compress_window.resizable(False, False)
    label = ttk.Label(compress_window, text='PDF\nCOMPRESS', foreground='#FF2525' ,font=('Montserrat', 28,'bold'),anchor='center',justify='center')
    label.pack(pady=10)

    DestLabel=ttk.Label(compress_window, text='DESTINATION:', foreground='#232323' ,font=('Montserrat', 10,'bold'),anchor='center',justify='center')
    DestLabel.pack(pady=10)
    DestLabel.place(x=85,y=114,width=130,height=36)

    entry = ttk.Entry(compress_window)
    entry.pack(pady=10)
    entry.place(x=23, y=151, width=255, height=39)
    style = ttk.Style()
    style.configure('TEntry', fieldbackground='#D9D9D9')
    
    style = ttk.Style()
    style.configure('Custom.TButton', font=('Montserrat', 18, 'bold'), foreground='white', background='#FF2525')
    style.map('Custom.TFrame',
          background=[('selected', '#D9D9D9'), ('active', '#D9D9D9')])

    button1 = ttk.Button(compress_window, text='CHOOSE',style='Custom.TButton',compound='center',takefocus=False,command=custom_choose)
    button1.pack(pady=25)
    button1.place(x=81, y=216,width=139,height=39)

    pdf_frame = ttk.Frame(compress_window, style='Custom.TFrame')  # Add style for the frame
    pdf_frame.pack(pady=10, padx=10)
    pdf_frame.place(x=24, y=277, width=252, height=94)

    pdf_list = tk.Listbox(pdf_frame, selectmode=tk.EXTENDED)
    pdf_list.pack(fill=tk.BOTH, expand=True)

    button2 = ttk.Button(compress_window, text='COMPRESS', style='Custom.TButton', compound='center', takefocus=False, command=compress_files)
    button2.pack(pady=25)
    button2.place(x=60, y=395,width=180,height=39)

    # Assuming you have a root window defined as "window"
    progress = ttk.Progressbar(compress_window, mode='determinate')
    progress.pack(pady=10)
    progress.place(x=23, y=455, width=255, height=18)
    style.configure('TProgressbar', background='#D9D9D9')

def validate_image_extension(P):
    valid_extensions = ('.png', '.jpg', '.jpeg', '.webp')
    ext = P.lower().strip()
    if ext.endswith(valid_extensions):
        return True
    else:
        return False  

def is_image(file_path):
    try:
        with Image.open(file_path):
            return True
    except:
        return False       

def custom_imgchoose(entry, pdf_list):
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        entry.delete(0, tk.END)
        for file_path in file_paths:
            if file_path not in pdf_list.get(0, tk.END):
                entry.insert(tk.END, file_path + "\n")
                pdf_list.insert(tk.END, file_path)

def convert_images_to_pdf(input_paths, output_path, progress_variable, total_images=None):
    total_images = len(input_paths)

    # Initialize the PDF canvas
    c = canvas.Canvas(output_path)

    for i, image_path in enumerate(input_paths, start=1):
        # Open the image using Pillow
        img = Image.open(image_path)

        # Get the size of the image in pixels
        img_width, img_height = img.size

        # Calculate the aspect ratio to fit the image within the PDF page
        aspect_ratio = img_width / img_height
        if aspect_ratio > 1:
            page_width = 800
            page_height = 800 / aspect_ratio
        else:
            page_height = 800
            page_width = 800 * aspect_ratio

        # Scale the image down to fit the entire image within the PDF page
        scale_factor = min(page_width / img_width, page_height / img_height)
        img_width *= scale_factor
        img_height *= scale_factor

        # Calculate the position to center the image on the page
        x_offset = (page_width - img_width) / 2
        y_offset = (page_height - img_height) / 2

        # Set the PDF page size based on the image size
        c.setPageSize((page_width, page_height))

        # Add the image to the PDF canvas
        c.drawImage(image_path, x_offset, y_offset, width=img_width, height=img_height)

        # Save the page and move to the next image
        c.showPage()


        # Update progress after each image is converted
        progress_value = int((i / total_images) * 100)
        progress['value'] = progress_value
        progress.update() # Update the progress bar widget

    c.save()    


def open_image_to_pdf():
    global pdf_list
    global progress
    

    image_to_pdf_window = tk.Toplevel(window)
    image_to_pdf_window.title('Image to PDF')
    image_to_pdf_window.geometry('300x500')
    image_to_pdf_window.resizable(False, False)
    label = ttk.Label(image_to_pdf_window, text='IMAGE\nTO PDF', foreground='#FF2525', font=('Montserrat', 28, 'bold'), anchor='center', justify='center')
    label.pack(pady=10)

    DestLabel = ttk.Label(image_to_pdf_window, text='DESTINATION:', foreground='#232323', font=('Montserrat', 10, 'bold'), anchor='center', justify='center')
    DestLabel.pack(pady=10)
    DestLabel.place(x=85, y=114, width=130, height=36)

    # Entry widget with background color #D9D9D9 and image file validation
    entry = ttk.Entry(image_to_pdf_window, validate='key')
    entry['validatecommand'] = (image_to_pdf_window.register(validate_image_extension), '%P')
    entry.pack(pady=10)
    entry.place(x=23, y=151, width=255, height=39)
    style = ttk.Style()
    style.configure('TEntry', fieldbackground='#D9D9D9')

    style = ttk.Style()
    style.configure('Custom.TButton', font=('Montserrat', 18, 'bold'), foreground='white', background='#FF2525')
    style.map('Custom.TFrame',
              background=[('selected', '#D9D9D9'), ('active', '#D9D9D9')])

    button1 = ttk.Button(image_to_pdf_window, text='CHOOSE', style='Custom.TButton', compound='center', takefocus=False, command=lambda: custom_imgchoose(entry, pdf_list))
    button1.pack(pady=25)
    button1.place(x=81, y=216, width=139, height=39)

    pdf_frame = ttk.Frame(image_to_pdf_window, style='Custom.TFrame')  # Add style for the frame
    pdf_frame.pack(pady=10, padx=10)
    pdf_frame.place(x=24, y=277, width=252, height=94)

    pdf_list = tk.Listbox(pdf_frame, selectmode=tk.EXTENDED)
    pdf_list.pack(fill=tk.BOTH, expand=True)
    progress_var = tk.IntVar()

    def convert_images():
        global entry, progress
        # Get the selected image file paths from the listbox
        selected_paths = pdf_list.get(0, tk.END)
        print("Selected images:", selected_paths)

        # Get the destination PDF file path from the entry widget
        destination_path = filedialog.asksaveasfilename(
            defaultextension='.pdf', filetypes=[("PDF files", "*.pdf")]
        )

        # If destination path is empty or contains unwanted characters, ask the user for a valid path
        if not destination_path or "\n" in destination_path:
            destination_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("PDF files", "*.pdf")])
            print("Chosen destination path:", destination_path)

        # Call the convert_images_to_pdf function with the selected images and destination path
        if destination_path:
            total_images = len(selected_paths)  # Calculate the total number of images
            progress_var.set(0)  # Reset the progress bar
            convert_images_to_pdf(selected_paths, destination_path, progress_var, total_images)


    button2 = ttk.Button(image_to_pdf_window, text='CONVERT', style='Custom.TButton', compound='center', takefocus=False, command=convert_images)
    button2.pack(pady=25)
    button2.place(x=70, y=395, width=160, height=39)

    # Assuming you have a root window defined as "window"
    progress = ttk.Progressbar(image_to_pdf_window, mode='determinate')
    progress.pack(pady=10)
    progress.place(x=23, y=455, width=255, height=18)
    style.configure('TProgressbar', background='#D9D9D9')

window = ttk.Window(themename='simplex')
window.title('Main window')
window.geometry('300x500')
window.resizable(False, False)
window.after(1000, check_clipboard)



label = ttk.Label(window, text='PDF\nORGANIZER', foreground='#FF2525' ,font=('Montserrat', 28,'bold'),anchor='center',justify='center')
label.pack(pady=10)

custom_style = ttk.Style()
custom_font = 'Montserrat', 25, 'bold'
custom_style.configure('Custom.TButton', font=custom_font, foreground='white', background='#FF2525', anchor='center',highlightthickness=50, highlightcolor='black',relief=tk.RAISED, highlightbackground='#FF2525')
custom_style.map('Custom.TButton',
                 foreground=[('active', 'white')],
                 background=[('active', '#272727')])

button1 = ttk.Button(window, text='   PDF\nMERGER',style='Custom.TButton',compound='center',takefocus=False,command=open_pdf_merger)
button1.pack(pady=25)
button1.place(x=31, y=128,width=238,height=100)

button2 = ttk.Button(window, text='     PDF\nCOMPRESS',style='Custom.TButton',compound='center',takefocus=False,command=open_pdf_compress)
button2.pack(pady=18)
button2.place(x=31, y=246,width=238,height=100)


button3 = ttk.Button(window, text=' IMAGE\nTO PDF',style='Custom.TButton',compound='center',takefocus=False,command=open_image_to_pdf)
button3.pack()
button3.place(x=31, y=370,width=238,height=100)




#run
window.mainloop()