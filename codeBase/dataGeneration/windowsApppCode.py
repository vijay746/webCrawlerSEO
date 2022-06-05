import tkinter as tk

#import webDataGeneration

# def open_file():
#     """Open a file for editing."""
#     filepath = askopenfilename(
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete(1.0, tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     window.title(f"Simple Text Editor - {filepath}")
#
# def save_file():
#     """Save the current file as a new file."""
#     filepath = asksaveasfilename(
#         defaultextension=".txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get(1.0, tk.END)
#         output_file.write(text)
#     window.title(f"Simple Text Editor - {filepath}")
#
# window = tk.Tk()
# window.title("Vijay : WebPage Crawler & Insights Reviews. - V0.1")
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)
#
# txt_edit = tk.Text(window)
# fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
# btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
# btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
#
# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)
#
# fr_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")
#
# window.mainloop()
#from webDataGeneration import getCurrentTime
import webbrowser

import webDataGeneration

urlreceivedFrmAPP = ""


def show_entered_urls():
    urlreceivedFrmAPP = url_entry_box_data.get()
    url_output_box_data.delete(0, 'end')
    url_output_box_data.insert(0, "Your Entered URL Is   : " + urlreceivedFrmAPP)
    webDataGeneration.setUrl(urlreceivedFrmAPP)
    print("url enetered : ", urlreceivedFrmAPP )
    webDataGeneration.setUrl(urlreceivedFrmAPP)
    return urlreceivedFrmAPP


# def getLinksDataFromwebDataGeneration():
#     webDataGeneration.getAllLinks()


# Set-up the window
window = tk.Tk()
window.title("Vijay : WebCrawler & WebPage Insights. V0.1")
window.resizable(width=True, height=True)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
url_entry_box = tk.Frame(master=window,width=200, height=300,  bg="")
url_entry_box_data = tk.Entry(master=url_entry_box, width=80, bg="white")

urlEntered_data_box = tk.Entry(master=url_entry_box, width=80, bg="green", fg="red")



url_output_box = tk.Frame(master=window, width=200, height=300,  bg="green")
url_output_box_data = tk.Entry(master=url_output_box, width=100)
url_output_box_data.insert(0, "Msg : Thanks for using this tool. For more information contact 4466vijay@gmail.com "+urlreceivedFrmAPP)






# Create the conversion Button and result display Label
btn_generateLinks = tk.Button(
    master=window,
    text="Generate Links Data",
    command=webDataGeneration.getAllLinksInSoup,
)

btn_generateJs = tk.Button(
    master=window,
    text=" Generate Js Data",
    command=webDataGeneration.getJsLinksInSoup
)

btn_generateCss = tk.Button(
    master=window,
    text=" Generate Css Data",
    command=webDataGeneration.getCssLinksInSoup
)

btn_generateImages = tk.Button(
    master=window,
    text=" Generate Images Data",
    command=webDataGeneration.getImageLinksInSoup
)


btn_generateBadLinks = tk.Button(
    master=window,
    text="Generate Bad Links",
    command=webDataGeneration.getBadLinksInSoup
)

btn_generateAllLinkStatus = tk.Button(
    master=window,
    text="Generate All Link Status",
    command=webDataGeneration.getAllLinkStatus
)

btn_generateDuplicate = tk.Button(
    master=window,
    text=" Generate Duplicate Data",
    command= webDataGeneration.getDuplicateLinks
)


btn_getTextFromPage = tk.Button(
    master=window,
    text="Get Page Text",
    command= webDataGeneration.getPageText
)

btn_showEntrdUrl = tk.Button(
    master=window,
    text="Show Entered URL",
    command=show_entered_urls
)


# lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

lbl_enterUrl = tk.Label(
    master=window,
    text="Enter URL :- ",
    foreground = "black",  # Set the text color to white
    background = "white"  # Set the background color to black
)



lbl_outPutData = tk.Label(
    master=window,
    text="YourData is saved at :- ",
    foreground = "black",  # Set the text color to white
    background = "white"  # Set the background color to black
)

empty_lable = tk.Label(window,bg="#A569BD")


sugestionUrl = "https://forms.gle/ePbpsid1uxaLARJ19"
readMeUrl = "https://docs.google.com/document/d/1zrntbHHBbC4mEANxyt5GzFF7z2p8LoGlnHAbGkjbFJ8/edit?usp=sharing"

new = 1
def openweb_Suggestion():
    webbrowser.open(sugestionUrl,new=new)

new = 1
def openweb_readMe():
    webbrowser.open(readMeUrl,new=new)


btn_openSuggestionPage = tk.Button(
    master=window,
    text="Open Suggestion Page",
    command=openweb_Suggestion
)


btn_openReadMePage = tk.Button(
    master=window,
    text="Open Read Me Page",
    command=openweb_readMe
)



# Set-up the layout using the .grid() geometry manager
empty_lable.grid(row=1, column=0, padx=60)

lbl_enterUrl.grid(row=2, column=0, padx=60)
url_entry_box.grid(row=2, column=1, padx=10)

url_output_box.grid(row=3, column=1, padx=10)

url_entry_box_data.grid(row=4, column=0, sticky="e")
url_output_box_data.grid(row=10, column=0)  #in progress

btn_showEntrdUrl.grid(row=3, column=0, pady=20)

btn_generateLinks.grid(row=4, column=0, pady=10)
btn_generateCss.grid(row=4, column=1, pady=10)
btn_generateImages.grid(row=4, column=2, pady=10)

btn_generateBadLinks.grid(row=5, column=0, pady=10)
btn_generateAllLinkStatus.grid(row=5, column=1, pady=10)

btn_generateJs.grid(row=6, column=0, pady=40)
btn_getTextFromPage.grid(row=6, column=1, pady=40)
btn_generateDuplicate.grid(row=6, column=2, pady=10)

btn_openSuggestionPage.grid(row=7, column=0, pady=40)
btn_openReadMePage.grid(row=7, column=1, pady=40)






# Run the application
window.mainloop()