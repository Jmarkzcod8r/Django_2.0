
from django.shortcuts import render, redirect, HttpResponse
from gtts import gTTS
import string
import random
import os
import shutil
from datetime import datetime
from .models import * # Product, Section, Post
import os
from django.conf import settings

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from random import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from shutil import copyfile
import random
import sys
from time import sleep
from selenium.webdriver.chrome.service import Service
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import threading
from tkinter import filedialog
import undetected_chromedriver as uc
import selenium
import json
from .forms import *


def tts_page(request):
    print("hi")
    if request.method == "POST":
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
        letters = string.ascii_lowercase

        file_name = f"{dt_string}{''.join(random.choice(letters) for i in range(10))}.mp3"

        text = request.POST['text']
        tdl = request.POST['tdl']
        lang = request.POST['lang']

        tts = gTTS(text, lang=lang, tld=tdl)
        print(file_name)
        tts.save(file_name)
        tts.save('okay.mp3')

        os.system("mpg321 okay.mp3")
        dir = os.getcwd()
        print('this is dir :', dir)
        full_dir = os.path.join(dir, file_name)
        print('this is full_dir :', full_dir)
        dest = shutil.move(full_dir, os.path.join(dir, "mainapp/static/sound_file"))
        print('this is dest: ', dest)

        data = {"loc" :file_name}
        # return render(request,'download.html',data)
        return render(request, 'index.html', {'loc':text})

        # return render(request, 'index.html', {'loc':text})
    return render(request, 'index.html', {'loc':''})
    # return None



def about_page(request):
    print("this is about page")
    sections = Section.objects.all()
    return render(request, 'about.html',{'sections':sections})

def test_page(request):
    print("this is test page")
    return render(request, 'test.html')

def testimony1(request):
    print("this is test page")
    return render(request, 'testimony1.html')


# def todo_page(request):
#     print("this is todo page")
#     return render(request, 'todo.html')

def todo_page(request):
# def createpost(request):
    if request.method == 'POST':
        print('received')
        if request.POST.get('title') and request.POST.get('content'): # are true:
            post=Post()
            post.title= request.POST.get('title')
            post.content= request.POST.get('content')
            post.save()
            # return render(request,'todo.html')

    Posts = Post.objects.all()
    # sections = Section.objects.all()

    # return render(request, 'todo.html', {'sections':sections} )
    return render(request, 'todo.html', {'Posts':Posts} )


        # else:
        #         return render(request,'todo.html')


def goUpload():
    root = tk.Tk()
    root.title('My Red Bubble Uploader')
    # root.iconbitmap('C:/Users/macni/Pictures/Screenshots/asdasd.PNG')
    root.geometry("1120x490")

    path_pics_list = []

    image_list=[]

    Tag_list = []

    Desc_list = []

    path_pics_list=[]

    list_shuffled_desc=[]

    list_shuffled_tags=[]

    temp_save=[]

    img_num=[0]

    # print("File location using os.getcwd():", os.getcwd())
    # cwd = os.getcwd()

    def Get_pics():
        initial_path='/home/jmarkz08/'
        # initial_path=os.getcwd()
        info_title.delete('0',END)
        info_title.insert(0, 'Uploading...')
        global path_pics
        path_pics = filedialog.askdirectory(initialdir = initial_path, title="Select image")
        file_dir_box.delete('1',END)
        file_dir_box.insert(0, path_pics)


        # global path_pics
        # path_pics = file_dir_box.get() + "/"
        global path_pics_list
        path_pics_list = os.listdir(path_pics)
        print('path_pics_list: ',path_pics_list)

        # Making initial list for image_list
        for x in range(0, len (path_pics_list)):
            image_list.append(str(x))
            # to_append = 'my_img'+str(x+1)
            # image_list.append(to_append)

        # # #make initial path_pics_list
        # for x in range (0, len (path_pics_list)):
        #     path_pics_list.append(str(x))
        #make initial Tag_list
        for x in range (0, len (path_pics_list)):
            Tag_list.append(str(x))

        #make initial Desc_list
        for x in range (0, len (path_pics_list)):
            Desc_list.append(str(x))

        #make list_shuffle_des
        for x in range (0, len (path_pics_list)):
            list_shuffled_desc.append(str(x))

        #make list_shuffle_tags
        for x in range (0, len (path_pics_list)):
            list_shuffled_tags.append(str(x))



        for x in range(0, len (path_pics_list)):
            image_list[x] =  ImageTk.PhotoImage((Image.open(path_pics + '/' + path_pics_list[x])).resize((480,270), Image.Resampling.LANCZOS) )






        global my_label
        my_label = Label(image=image_list[0], bg="gray" , borderwidth=2, relief="groove")
        my_label.grid(row=0, rowspan = 10, column=0, columnspan=3, sticky = "nesw")


        image_number=2
        flag = True
        while(flag):

            try:
                root.bind('<Return>', lambda event: forward(image_number))
                ttk.Label(root, text='1' + ' of ' + str(len (path_pics_list)), font=("Times New Roman", 12)).grid(column=1, row=11)
                break
            except Exception as e:
                print (e, 'okay')


        # Title_label = ttk.Label(root, text=path_pics_list[image_number-2], font=("Bold", 12)).grid(column=0,  columnspan =1 ,row=13)

        info_title.delete(0, END)
        info_title.insert(0, 'Note, Do not input anything here. For display only. Go above to edit title.')

        # Desc_area.insert(INSERT, 0)
        # Tags_area.insert(INSERT, 0)

    def Thread_orig_code():
        threading.Thread(target=orig_code).start()

    def Thread_Get_pics():
        threading.Thread(target=Get_pics).start()





    def forward(image_number):
        global my_label
        global button_forward
        global button_back
        global path_pics_list


        # Get the input new Title
        Title = ntry1.get()
        ntry1.delete(0, END)



        def save_entries():

            # print(f'This is image_number = {image_number}')
            # path_pics_list[image_number-2]= Title
            # print(f'This is path_pics_list = {path_pics_list}')


            # print(str(path_pics_list)+ 'this is path_pics_list')

            Desc_get = Desc_area.get('1.0',END)

            # print(f'This is image_number = {image_number}')
            # print(list_shuffled_desc)
            list_shuffled_desc[image_number-2]= Desc_get.strip()
            # print(f'This is list_shuffle_desc = {list_shuffled_desc}')


            Tags_get = Tags_area.get('1.0',END)
            if Tags_get=='':
                print('sorry, no change applied to Title')

            else:
                print(f'This is image_number = {image_number}')
                list_shuffled_tags[image_number-2]= Tags_get.strip()
            # print(f'This is list_shuffle_tags = {list_shuffled_tags}')

        save_entries()
        sleep(0.2)

        if Title=='':
            print('sorry, no change applied to Title')

        else:
            path_pics_list[image_number-2]= Title


        my_label.grid_forget()
        my_label = Label(image=image_list[image_number-1], bg="gray", borderwidth=2, relief="groove")
        my_label.grid(row=0, rowspan = 10, column=0, columnspan=3, sticky = "nesw")
        my_label.pack_propagate(0)


        #setting new value for function forward() with new value of (image_number+1)
        button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
        root.bind('<Return>', lambda event: forward(image_number+1))
        button_back = Button(root, text="<<", command=lambda: back(image_number-1))


        if image_number == len(path_pics_list):


            # button_forward = Button(root, text=">>", command=save_entries)
            button_forward = Button(root, text=">>", state=DISABLED)
            root.unbind('<Return>')
        my_label.grid(row=0, rowspan = 10, column=0, columnspan=3, sticky = "nesw")
        button_back.grid(row=10, column=0)
        button_forward.grid(row=10 , column=2)

        ttk.Label(root, text=str(image_number) + ' of ' + str(len (path_pics_list)), font=("Times New Roman", 12)).grid(column=1, row=11)

        global for_outside_img_nmbr
        for_outside_img_nmbr = str(image_number)

        info_title.delete(0, END)
        # info_title.insert(0, path_pics_list[image_number-1])
        info_title.insert(0, path_pics_list[image_number-1])

        img_num[0]=int(image_number)

        # temp_save[0]=(image_number-1)


        # Clear the Tags box
        Tags_area.delete('1.0',END)


        # CLear the Desc box
        Desc_area.delete('1.0', END)

        Desc_area.insert(INSERT, list_shuffled_desc[image_number-1])
        Tags_area.insert(INSERT, list_shuffled_tags[image_number-1])



    def Thread_forward(image_number):
        threading.Thread(target=forward(image_number)).start()



    def back(image_number):
        global my_label
        global button_forward
        global button_back
        global path_pics_list



        Title = ntry1.get()
        ntry1.delete(0, END)
        # Text_title=True
        # while(Text_title):
        #     if len(ntry1.get()) == 0:
        #         break
        #     else:
        #          path_pics_list[image_number]= Title
        #          break

        def save_entries_back():

            if Title=='':
                print('sorry, no change applied')

            else:
                path_pics_list[image_number]= Title

            Tags_get = Tags_area.get('1.0',END)
            if Tags_get=='':
                print('sorry, no change applied to Title')

            else:
                print(f'This is image_number = {image_number}')
                list_shuffled_tags[image_number]= Tags_get.strip()
            print(f'This is list_shuffle_tags = {list_shuffled_tags}')


            Desc_get = Desc_area.get('1.0',END)
            if Desc_get=='':
                # print(f'This is image_number = {image_number}')
                # print(list_shuffled_desc)
                print('sorry, no change applied to Title')
            else:
                list_shuffled_desc[image_number]= Desc_get.strip()
            print(f'This is list_shuffle_desc = {list_shuffled_desc}')


            Tags_get = Tags_area.get('1.0',END)
            if Tags_get=='':
                print('sorry, no change applied to Title')

            else:
                print(f'This is image_number = {image_number}')
                list_shuffled_tags[image_number]= Tags_get.strip()
            print(f'This is list_shuffle_tags = {list_shuffled_tags}')

        save_entries_back()
        sleep(0.2)






        my_label.grid_forget()
        my_label = Label(image=image_list[image_number-1], bg="gray" , borderwidth=2, relief="groove")
        button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
        button_back = Button(root, text="<<", command=lambda: back(image_number-1))
        print(image_number)

        root.bind('<Return>', lambda event: forward(image_number+1))

        if image_number == 1:
            button_back = Button(root, text="<<", state=DISABLED)


        my_label.grid(row=0, rowspan = 10, column=0, columnspan=3, sticky = "nesw")
        button_back.grid(row=10, column=0)
        button_forward.grid(row=10 , column=2)

        ttk.Label(root, text=str(image_number) + ' of ' + str(len (path_pics_list)), font=("Times New Roman", 12)).grid(column=1, row=11)

        # global for_outside_img_nmbr
        # for_outside_img_nmbr = str(image_number)

        info_title.delete(0, END)
        # info_title.insert(0, path_pics_list[image_number-1])
        info_title.insert(0, path_pics_list[image_number-1])

        # Clear the Tags box
        Tags_area.delete('1.0',END)


        # CLear the Desc box
        Desc_area.delete('1.0', END)

        Desc_area.insert(INSERT, list_shuffled_desc[image_number-1])
        Tags_area.insert(INSERT, list_shuffled_tags[image_number-1])

        print(f'This is path_pics_list = {path_pics_list}')





    def Print_path_pics_list():

        print(f'This is path_pics_list           = {path_pics_list}')
        # print(for_outside_img_nmbr)
        # print(image_list)
        print(f'This is list_shuffled_tags   = {list_shuffled_tags}')
        print(f'This is list_shuffled_desc   = {list_shuffled_desc}')




    temp=[]
    def Get_randomized_tags():
            initial_path = '/home/jmarkz08/'
            tags_path = filedialog.askopenfilename( initialdir = initial_path,title="Select image")
            print(tags_path)

            f = open(tags_path, 'r')
            content = f. read()
            convert_to_list = content.split (",")
            ctl = convert_to_list
            for x in range(len(path_pics_list)):
                random.shuffle(ctl)
                joined_string = ",".join(ctl)
                js = joined_string
                # temp.append(js)
                # print(temp[0])
                list_shuffled_tags[x]=js
            Tags_area.insert(INSERT, list_shuffled_tags[0])



    global ask_desc_path


    temp2=[]
    def Get_random_desc():
            initial_path = '/home/jmarkz08/'
            global ask_desc_path
            ask_desc_path = filedialog.askdirectory(initialdir = initial_path, title="Select image")
            # temp.append(ask_desc_path)

            global path
            path = ask_desc_path
            print(path)
            temp2.append(path)
            path=temp2[0]
            desc_list = os.listdir(path)
            print(desc_list)
            for j in range(0,len(path_pics_list)):
                x = random.randint(0,len(desc_list)-1)
                y = open(path +"/" +desc_list[x],'r')
                global f
                f = y.read()
                print(f)
                list_shuffled_desc[j]=f
            Desc_area.insert(INSERT, list_shuffled_desc[0])



    def orig_code():

        if img_num[0]==len (path_pics_list):
            def save_entries_proceed():


                # print(f'This is image_number = {image_number}')
                # path_pics_list[image_number-2]= Title
                # print(f'This is path_pics_list = {path_pics_list}')


                # print(str(path_pics_list)+ 'this is path_pics_list')

                Desc_get = Desc_area.get('1.0',END)

                # print(f'This is image_number = {image_number}')
                # print(list_shuffled_desc)
                list_shuffled_desc[img_num[0]-1]= Desc_get.strip()
                # print(f'This is list_shuffle_desc = {list_shuffled_desc}')


                Tags_get = Tags_area.get('1.0',END)
                if Tags_get=='':
                    print('sorry, no change applied to Title')

                else:
                    # print(f'This is image_number = {image_number}')
                    list_shuffled_tags[img_num[0]-1]= Tags_get.strip()
                # print(f'This is list_shuffle_tags = {list_shuffled_tags}')
                Title = ntry1.get()
                ntry1.delete(0, END)

                if Title=='':
                    print('sorry, no change applied to Title')

                else:
                    path_pics_list[img_num[0]-1]= Title

            save_entries_proceed()
            sleep(0.2)
        Print_path_pics_list()


        counter = 0
        z = counter

        # chrome_options = Options()
        # chrome_options.add_argument('--deny-permission-prompts')
        # chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
        # driver = webdriver.Chrome(options=chrome_options,  executable_path=ChromeDriverManager().install())
        # driver.get("https://www.redbubble.com/auth/login")

        options = uc.ChromeOptions()
        # options.headless = True
        driver = uc.Chrome(use_subprocess=True, options=options, version_main=108,executable_path=ChromeDriverManager().install())
        driver.get("https://www.redbubble.com/auth/login")

        def send_randomized_tags():

            tag_text = driver.find_element(By.XPATH, '//*[@id="work_tag_field_en"]')
            tag_text.send_keys('hi')
            tag_text.clear()
            tag_text.send_keys(list_shuffled_tags[z] + ", " +name_of_work)

        def kill_session():
            #assuming we are logged in
            driver.get('https://www.redbubble.com/auth/logout?ref=account-nav-dropdown')
            logging_out_button = driver.find_element(By.XPATH,'//*[@id="logout-form"]/form/input[3]')
            logging_out_button.click()
            driver.quit()
            # close the program
            sys.exit()

        def send_desc_redbubble():

            description_text = driver.find_element(By.XPATH,'//*[@id="work_description_en"]')
            description_text.send_keys('hi')
            description_text.clear()
            description_text.send_keys(list_shuffled_desc[z] +" "+name_of_work)

        image_directory_plus_file_excluding_file_type = path_pics + '/'

        def Log_in_confirmaton_box():
            MsgBox = tk.messagebox.askquestion ('Log In Confirmation','Logged in yet? Click to continue',icon = 'info')
            if MsgBox == 'yes':
            #    root.destroy()
                print('yes..continue')
            else:

                print('okay')
                # wait=input('Hmmmm:')
                # tk.messagebox.showinfo('Return','You will now return to the application screen')
        Log_in_confirmaton_box()


        print("we're here")
        print('image_directory_plus_file_excluding_file_type: ',image_directory_plus_file_excluding_file_type)
        print('os.list: ',os.listdir(image_directory_plus_file_excluding_file_type))
        list_of_files = os.listdir(image_directory_plus_file_excluding_file_type)
        # for index in range(0,len(list_of_files)):
        for index in range(0,len(list_of_files)):
            print('start')
            file_with_ending = list_of_files[index]

            file = file_with_ending
            flag = True
            while(flag):

                    counter += 1

                    if counter > 60:
                        # redbubble has a limit of 60 works per day - if we have gone pass that sign out and exit page
                        kill_session()
                    try:
                        # after login
                        # driver.get('https://www.redbubble.com/portfolio/images/new')
                        copy_settings_string = copy_set_box.get()
                        driver.get(copy_settings_string)
                        # this is so the leaving page popup is disabled
                        driver.execute_script("window.onbeforeunload = function() {};")
                        # uploading_an_image
                        time.sleep(5)

                        replace_image = driver.find_element(By.XPATH,'//*[@id="select-image-base"]')
                        replace_image.send_keys(image_directory_plus_file_excluding_file_type+file)

                        time.sleep(3)

                        name_of_work_text_box = driver.find_element(By.XPATH,'//*[@id="work_title_en"]')
                        name_of_work_text_box.clear()

                        name_of_work = path_pics_list[(counter-1)]
                        name_of_work_text_box.send_keys(name_of_work.title())
                        time.sleep(0.5)

                        #1.1
                        send_randomized_tags()

                        send_desc_redbubble()

                        time.sleep(2)


                        flag_1 = True
                        while(flag_1):
                            progress_bar = driver.find_element(By.XPATH,'//*[@id="add-new-work"]/div/div[1]/div[1]/div[1]')
                            # time.sleep(20)
                            progress_bar_value = int(progress_bar.get_attribute("data-value"))
                            if (progress_bar_value == 100 or progress_bar_value == 0):
                                break
                            time.sleep(0.2)

                        flag_3 = True
                        while(flag_3):
                            try:
                                check_box_have_rights = driver.find_element(By.XPATH, '//*[@id="rightsDeclaration"]')
                                check_box_have_rights.click()
                                submit_button_work = driver.find_element(By.XPATH,'//*[@id="submit-work"]')
                                submit_button_work.click()
                                time.sleep(2)
                                print(str(counter + 1) + "/60") #----------> This makes us know how many times we uploaded
                                break
                            except Exception as e:
                                print('sumbmit button has been pressed')

                        # manage_your_work_button = None

                        time.sleep(4)

                        flag_4 = True
                        while(flag_4):
                            try:
                                manage_your_work_button = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/a/p')
                                break
                            except Exception as e:
                                print("item not found yet")
                                '''
                                working with error whilst uploading, if error is too big retry upload from start
                                '''
                                try:
                                    element_for_server_error_500 = driver.find_element(By.XPATH, '//*[@id="wrap"]/h1')
                                    message = element_for_server_error_500.text
                                    if "Computer says 'No'." in message:
                                        print("we have been signed out or the page has crashed")
                                        driver.get("https://www.redbubble.com/")
                                        driver.get("https://www.redbubble.com/portfolio/images")
                                        break
                                except Exception as e:
                                    print(e, " this means the we are still waiting for the work to be uploaded")

                                time.sleep(2)
                        try:
                            manage_your_work_button.click()

                            break
                        except Exception as e:
                            print("exception")

                    except Exception as e:
                        print(e, "error, try task again")
                        # exit_wait=input("There is an error, might need to restart, input anything and click 'Enter' to try again:")
                        #kill_session()
                        MsgBox2 = tk.messagebox.askquestion ('Oopss.. An error occurred. Click `Yes` to try again',icon = 'info')
                        if MsgBox2 == 'yes':
                        #    root.destroy()
                            print('yes..continue')
                        else:

                            print('okay')
                            break
                            # wait=input('Hmmmm:')
                        counter -= 1

        print(counter)
        wait = input("Input anything to close: ")

    # ----------------------------------------- orig code -----------------------------------------------


    my_label = Label(bg="gray" , borderwidth=2, relief="groove", height = 18)
    my_label.grid(row=0, rowspan = 10, column=0, columnspan=3, sticky = "nesw")

    button_back = Button(root, text='<<', command=back, state = DISABLED)
    button_exit = Button(root, text='Exit', command=root.quit)
    button_forward = Button(root, text='>>', command=lambda:forward(2) )

    button_back.grid(row=10, column=0)
    button_exit.grid(row=10, column=1)
    button_forward.grid(row=10 , column=2)

    # Print_list = Button(root, text='Print', command = Print_path_pics_list )
    Proceed_rb = Button(root, text='Proceed', command = Thread_orig_code )

    # Print_list.grid(row=10, column=4)
    Proceed_rb.grid(row=10, column=5)

    Tag_dir = Button(root, text='*\.' , command= Get_randomized_tags )
    Desc_dir = Button(root, text='*\.', command= Get_random_desc)

    Tag_dir.grid(row=2, column=7)
    Desc_dir.grid(row=6, column=7)

    ttk.Label(root, text="Tags", font=("Times New Roman", 15)).grid(column=4, columnspan =1 ,row=3)
    ttk.Label(root, text="Title", font=("Bold", 12)).grid(column=4,  columnspan =1 ,row=1)
    ttk.Label(root, text="Description", font=("Bold", 12)).grid(column=4,  columnspan =1 ,row=7)

    ntry1 = Entry(root, width=50, )
    ntry1.grid(row=0, column=3, columnspan = 4)

    ttk.Label(root, text=' ', font=("Times New Roman", 12)).grid(column=1, row=11)

    # Tags Text area
    Tags_area = scrolledtext.ScrolledText(root, wrap=tk.WORD,width=40, height=3, font=("Bold", 12))
    # Tags_area.insert(0,'some text')
    Tags_area.grid(column=3, columnspan =3,row=2, pady=1, padx=1)
    # Description Text area
    Desc_area = scrolledtext.ScrolledText(root, wrap=tk.WORD,width=40, height=3, font=("Bold", 12))
    Desc_area.grid(column=3, columnspan =3,row=6, pady=1, padx=1)
    # Log Text area
    # Log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD,width=30, height=3, font=("Bold", 12))
    # Log_area.grid(column=4, columnspan =3,row=14, rowspan=3)



    ttk.Label(root, text="       ", font=("Bold", 12)).grid(column=0,  columnspan =1 ,row=12)

    ttk.Label(root, text="Info Title:", font=("Bold", 12)).grid(column=0,row=13)

    # This info title box
    info_title = Entry(root, width=62, justify = 'center')
    info_title.grid(row=13, column=1, columnspan = 2, sticky = 'W' )

    # This entry box is file directory
    file_dir_box = Entry(root, width=62, justify = 'center' )
    file_dir_box.grid(row=14, column=1, columnspan = 2)

    # This is Get Pics button
    Get_pics_btn = Button(root, text='Get Pics', command = Thread_Get_pics)
    Get_pics_btn.grid(row=14, column=3)

    # This entry for copy settings
    copy_set_box = Entry(root, width=62, justify = 'center' )
    copy_set_box.grid(row=15, column=1, columnspan = 2)

    ttk.Label(root, text="File Directory:", font=("Bold", 12)).grid(column=0,row=14)

    ttk.Label(root, text="Copy Settings:", font=("Bold", 12)).grid(column=0,row=15)

    root.mainloop()

def index_page(request):
    # print("this is tts page")
    # sections = Section.objects.all()
    # goUpload()
    # kid = 0
    photos = Photo.objects.all()
    photoskid = Photo.objects.last()
    photoget = Photo.objects.all().first()
    print("this is photos ",photoskid)
    # print("this is photos length: ",len(photos))
    print("this is photoget: ",photoget)
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        tag = request.POST['tag']
        photo = request.FILES['photo']
        directory = os.path.dirname(os.path.abspath(photo.name))
        print("Photo: ",photo)
        print("File directory:", directory)
        photo = Photo(kid=datetime.timestamp(datetime.now()), title=title, description=description, tag=tag, photo=photo)
        # photo = Photo(kid=len(photos) + 1, title=title, description=description, tag=tag, photo=photo)
        photo.save()
    photos = Photo.objects.all()
        # return render(request, 'Uploader.html',{'photos':photos} )
    # kid += 1
    # photos.delete()
    return render(request, 'Uploader.html',{'photos':photos} )

def delete_post(request, id):
    print("commencing delete_post with ", id)
    delphoto= Photo.objects.get(pk=id)
    # context = {'photos': photos}
    os.remove(os.path.join(settings.MEDIA_ROOT, str(delphoto.photo)))

    # if request.method == 'GET':
    #     return render(request, 'blog/post_confirm_delete.html',context)
    # if request.method == 'POST':
    print("commencing delete_post ...POST method")
    delphoto.delete()
    photos = Photo.objects.all()
        # messages.success(request,  'The post has been deleted successfully.')
        # return redirect('posts')
    return render(request, 'Uploader.html',{'photos':photos} )

def delete_all(request):
    photos = Photo.objects.all()
    for photo in photos:
        os.remove(os.path.join(settings.MEDIA_ROOT, str(photo.photo)))
    photos.delete()
    return render(request, 'Uploader.html',{'photos':photos} )

def edit_item(request, id):
    photo = Photo.objects.get( pk=id)

    if request.method == 'POST':
        photo.title = request.POST['title']
        photo.description = request.POST['description']
        photo.tag = request.POST['tag']
        photo.save()
        return redirect('uploader')

    return render(request, 'edit_item.html', {'photo': photo})

def Publish (request):
    photos = Photo.objects.all()
    print(os.getcwd())
    for photo in photos:
        print("------------------------------ ")
        print("this is photos_title ", photo.title)
        print("this is photos_tag ", photo.tag)
        print("this is photos_description ", photo.description)
        print("this is photos_url ", photo.photo.url)

    options = uc.ChromeOptions()
    # options.headless = True
    driver = uc.Chrome(use_subprocess=True, options=options, version_main=108,executable_path=ChromeDriverManager().install())
    # options = selenium.webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #could also do options.headless = True
    # options.add_argument('--window-size=1920x1080')
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://www.redbubble.com/auth/login")

    def send_randomized_tags():

            tag_text = driver.find_element(By.XPATH, '//*[@id="work_tag_field_en"]')
            tag_text.send_keys(os.getcwd() + photo[0].tag)
            # tag_text.clear()
            # tag_text.send_keys(list_shuffled_tags[z] + ", " +name_of_work)
    con = input("continue?")
    # send_randomized_tags()
    driver.get("https://www.redbubble.com/portfolio/images/new?ref=account-nav-dropdown")

    def send_image():
        try:
            # replace_image = driver.find_element(By.XPATH, '//*[@id="select-image-base"]')
            replace_image = driver.find_element(By.XPATH, '//*[@id="select-image-single"]')
            replace_image.send_keys(os.getcwd() +photos[0].photo.url)
        except Exception as e:
            print('Image element not found, retrying in 7 seconds...')
            time.sleep(7)
            send_image()
    send_image()



    return render(request, 'Uploader.html',{'photos':photos} )

def Sample_selenium(request):
    photos = Photo.objects.all()

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)
    # try:
    browser.get("https://www.google.com")
    con = input('h?')
        # print("Page title was '{}'".format(browser.title))
    # finally:
    #     browser.quit()

    return render(request, 'Uploader.html',{'photos':photos} )
# def hotel_image_view(request):

#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = HotelForm()
#     return render(request, 'hotel_image_form.html', {'form': form})


# def success(request):
#     return HttpResponse('successfully uploaded')

# def display_hotel_images(request):

#     if request.method == 'GET':

#         # getting all the objects of hotel.
#         Hotels = Hotel.objects.all()
#         return render((request, 'display_hotel_images.html',
#                        {'hotel_images': Hotels}))
