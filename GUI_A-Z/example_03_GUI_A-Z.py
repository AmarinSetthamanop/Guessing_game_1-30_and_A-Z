# ทุกอย่างที่เกี่ยวกับ tkinter(Frame)
from tkinter import *
# เกี่ยวกับการสุ่ม
import random



# function สำหรับการแปลงค่า rgb ให้สามารถใช้ใน tkinter
def _random_rgb():
    """translates an rgb tuple of int to a tkinter friendly color code"""
    min = 80
    max = 140
    r = random.randint(min, max) # สุ่มเลขตั้งแต่ 80 - 140
    g = random.randint(min, max)
    b = random.randint(min, max)
    rgb = r,g,b
    return "#%02x%02x%02x" % rgb

# function สำหรับปิดหน้าต่างเกม...
def close_mainFrame():
    # quit() คือ ลบ object ทั้งหมด
    # destroy() คือ ลบ เฉพาะ object นั้นๆ
    mainFrame.quit()

# function สำหรับกลับไปที่หน้า menuFrame เมื่อตอนนี้อยู่หน้า modeFrame
def back_to_menuFrame():
    # ก่อนอื่นลบหน้า modeFrame ออกก่อน
    modeFrame.destroy()
    # จากนั้นสร้างหน้า menuFrame
    create_menuFrame_start_exit()

# function สำหรับกลับไปที่หน้า modeFrame เมื่อตอนนี้อยู่หน้า gameFrame
def back_to_modeFrame():
    # ก่อนอื่นลบหน้า gameFrame ออกก่อน
    gameFrame.destroy()
    # จากนั้นสร้างหน้า modeFrame
    create_modeFrame_easy_nomal_hard_back()

# function สำหรับกลับไปที่หน้า modeFrame เมื่อตอนนี้อยู่หน้า endFrame
def on_endFrame_back_to_modeFrame():
    # ก่อนอื่นลบหน้า endFrame ออกก่อน
    endFrame.destroy()
    # จากนั้นสร้างหน้า modeFrame
    create_modeFrame_easy_nomal_hard_back()



################################################################## Menu Frame
def create_menuFrame_start_exit():

    # กำหนดให้ตัวแปลต่างๆนี้ สามารถเรียกใช้งานได้จาก function อื่นๆ
    global menuFrame

    # สร้างหน้าต่าง Menu โดยนำไปใส่ไว้ใน mainFrame
    menuFrame = LabelFrame(mainFrame,
                        width=800/2,
                        height=600/1.5,
                        bd=5)
    menuFrame.place(relx=0.5 , rely=0.5, anchor=CENTER) # ใช้ place() แล้วกำหนดให้อยู่กลางหน้าจอ 
    menuFrame.pack_propagate(False) # ไม่ให้ menuFrame มีขนาด กว้าง*ยาว ที่พอดีกับ Lable อื่นๆ ที่อยู่ข้างใขตัวมัน
    # สร้างข้อความเพื่อแสดงบน menuFrame
    text_show = Label(menuFrame,
                        text="Random Guessing A-Z Game",
                        fg = _random_rgb(), # function ไหนที่มีการ return... ไม่ว่า function นั้นจะไม่มี paramiter ก็ตาม ถ้าเรียกใช้ function นั้นต้องใส่ ()
                        font=50)
    text_show.pack(pady=40) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 40*40
    # สร้างปุ่มเริ่มเกมเพื่อแสดงบน menuFrame
    startGame_btn = Button(menuFrame,
                        text="Start",
                        font=50,
                        width=10,
                        bg="chartreuse4",
                        #    ถ้า function ไหนไม่มีการ return เมื่อเรียกใช้ function นั้นอาจไม่จำเป็นต้องใส่ () 
                        command = create_modeFrame_easy_nomal_hard_back) # เมื่อกดปุ่ม Start จะไปทำงานที่ create_modes_btn()
    startGame_btn.pack(pady=40) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 40*40
    # สร้างปุ่มออกจากเกมเพื่อแสดงบน menuFrame
    exit_btn = Button(menuFrame,
                    text="Exit",
                    font=50,
                    width=10,
                    bg="coral4",
                    #   ถ้า function ไหนไม่มีการ return เมื่อเรียกใช้ function นั้นอาจไม่จำเป็นต้องใส่ ()
                    command = close_mainFrame) # เมื่อกดปุ่ม Exit จะไปทำงานที่ close_mainFrame()
    exit_btn.pack(pady=40) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 40*40




################################################################## Modes Button
# function สำหรับสร้างปุ่มเลือก Mode การเล่น Hard, Nomal, Easy เพื่อแสดงบน menuFrame
def create_modeFrame_easy_nomal_hard_back():

    # กำหนดให้ตัวแปลต่างๆนี้ สามารถเรียกใช้งานได้จาก function อื่นๆ
    global modeFrame

    # ก่อนอื่นต้องลบ menuFrame ออจาก mainFrame ก่อนจากนั้นสร้าง modeFrame และปุ่มอื่นๆ เพื่อให้แสดงอยู่ใน mainFrame
    menuFrame.destroy()

    # สร้างหน้าต่างเลือก Mode Frame ความยากง่าย โดยนำไปใส่ไว้ใน mainFrame
    modeFrame = LabelFrame(mainFrame,
                        width=800/2,
                        height=600/1.5,
                        bd=5)
    modeFrame.place(relx=0.5 , rely=0.5, anchor=CENTER) # ใช้ place() แล้วกำหนดให้อยู่กลางหน้าจอ 
    modeFrame.pack_propagate(False) # ไม่ให้ modeFrame มีขนาด กว้าง*ยาว ที่พอดีกับ Lable อื่นๆ ที่อยู่ข้างใขตัวมัน
    # สร้างข้อความเพื่อแสดงบน modeFrame
    text_show = Label(modeFrame,
                        text="Select game mode",
                        fg = _random_rgb(), # function ไหนที่มีการ return... ไม่ว่า function นั้นจะไม่มี paramiter ก็ตาม ถ้าเรียกใช้ function นั้นต้องใส่ ()
                        font=50)
    text_show.pack(pady=15) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 15*15
    # สร้างปุ่ม Easy mode เพื่อแสดงบน menuFrame
    easyMode_btn = Button(modeFrame,
                        text="EASY",
                        font=50,
                        width=10,
                        bg="chartreuse4",
                        #     เมื่อกดปุ่มแล้วต้องการให้ไปทำงาน function ที่ต้องส่ง paramiter ไปด้วน --> จะต้องใช้ lambda เพื่อกำหนดว่า function นี้สามารถส่ง paramiter ไปได้
                        command = lambda: create_gameFrame(1)) # เมื่อกดปุ่ม EASY จะไปทำงานที่ createGame_frame()
    easyMode_btn.pack(pady=15) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 15*15
    # สร้างปุ่ม nomal mode เพื่อแสดงบน menuFrame
    nomalMode_btn = Button(modeFrame,
                        text="Nomal",
                        font=50,
                        width=10,
                        bg="yellow",
                        #     เมื่อกดปุ่มแล้วต้องการให้ไปทำงาน function ที่ต้องส่ง paramiter ไปด้วน --> จะต้องใช้ lambda เพื่อกำหนดว่า function นี้สามารถส่ง paramiter ไปได้
                        command = lambda: create_gameFrame(2)) # เมื่อกดปุ่ม EASY จะไปทำงานที่ createGame_frame()
    nomalMode_btn.pack(pady=15) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 15*15
    # สร้างปุ่ม Hard เพื่อแสดงบน menuFrame
    hardMode_btn = Button(modeFrame,
                    text="HARD",
                    font=50,
                    width=10,
                    bg="coral4",
                    #     เมื่อกดปุ่มแล้วต้องการให้ไปทำงาน function ที่ต้องส่ง paramiter ไปด้วน --> จะต้องใช้ lambda เพื่อกำหนดว่า function นี้สามารถส่ง paramiter ไปได้
                    command = lambda: create_gameFrame(3)) # เมื่อกดปุ่ม HART จะไปทำงานที่ createGame_frame() 
    hardMode_btn.pack(pady=15) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 15*15
    # สร้างปุ่ม กลับไปที่หน้า menuFrame เพื่อแล้วบนหน้า menuFrame
    back_btn = Button(modeFrame,
                      text="< Back",
                      font=50,
                      width=10,
                      bg="darkslategray4",
                      command = back_to_menuFrame) # เมื่อกดปุ่ม back จำไปทำงานที่ back_to_menuFrame()
    back_btn.pack(pady=15) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 15*15



################################################################## Game Frame
# function สำหรับสร้างหน้าเล่นเกมสุ่มเลข โดยรับ mode เข้ามาว่า ง่าย(1), ปานกลาง(2) หรือ ยาก(3)
def create_gameFrame(mode):
    # กำหนดให้ตัวแปลต่างๆนี้ สามารถเรียกใช้งานได้จาก function อื่นๆ
    global number_of_times_to_play, traget, max_answer_btn

    # ก่อนอื่นต้องลบหน้า modeFrame ออกจากหน้า mainFrame ก่อน
    modeFrame.destroy()
    
    # ถ้าเลือก gmae mode ง่าย
    if mode == 1:
        # ปุ่มคำตอบสูงสุดที่จะสร้างได้ (J)
        max_answer_btn = 74
        # สุ่มตัวเลขจำนวนเต็ม 65-74 (A-J)
        traget = random.randint(65, 74)
        # กำหนดให้จำนวนครั้งที่สามารถเล่นอกมได้
        number_of_times_to_play = 10
        # ส่งค่าตัวเลขที่สุ่มได้ , ข้อความที่จะนำไปแสดง game(), จำนวนแถวที่ต้องสร้างปุ่มกด --> เพื่อสร้าง Object ต่างๆ สำหรับเล่นเกม
        game("A-J", 2)


    elif mode == 2:
        # ปุ่มคำตอบสูงสุดที่จะสร้างได้ (N)
        max_answer_btn = 78
        # สุ่มตัวเลขจำนวนเต็ม 65-78 (A-N)
        traget = random.randint(65, 78)
        # กำหนดให้จำนวนครั้งที่สามารถเล่นอกมได้
        number_of_times_to_play = 6
        # ส่งค่าตัวเลขที่สุ่มได้ , ข้อความที่จะนำไปแสดง game(), จำนวนแถวที่ต้องสร้างปุ่มกด --> เพื่อสร้าง Object ต่างๆ สำหรับเล่นเกม
        game("A-N", 3)

    
    # ถ้าเลือก gmae mode ยาก
    elif mode == 3:
        # ปุ่มคำตอบสูงสุดที่จะสร้างได้ (Z)
        max_answer_btn = 90
        # สุ่มตัวเลขจำนวนเต็ม 65-90 (A-Z)
        traget = random.randint(65, 90)
        # กำหนดให้จำนวนครั้งที่สามารถเล่นเกมได้
        number_of_times_to_play = 3
        # ส่งค่าตัวเลขที่สุ่มได้ , ข้อความที่จะนำไปแสดง game(), จำนวนแถวที่ต้องสร้างปุ่มกด --> เพื่อสร้าง Object ต่างๆ สำหรับเล่นเกม
        game("A-Z", 6)

# function สำหรับสร้าง Object ต่างๆ เพื่อเล่นเกม
def game(txt, number_of_rows_of_button):

    # กำหนดให้ตัวแปลต่างๆนี้ สามารถเรียกใช้งานได้จาก function อื่นๆ
    global gameFrame, text_show_2, text_show_3

    # สร้างหน้าต่าง gameFrame สำหรับเก็บ Object ต่างๆสำหรับเล่นเกม แล้วแสดงบน mainFrame
    gameFrame = LabelFrame(mainFrame,
                           width=800/1.1,
                           height=800/1.5,
                           bd=5)
    gameFrame.place(relx=0.5, rely=0.5, anchor=CENTER) # ใช้ place() แล้วกำหนดให้อยู่กลางหน้าจอ 
    gameFrame.pack_propagate(False) # ไม่ให้ gameFrame มีขนาด กว้าง*ยาว ที่พอดีกับ Lable อื่นๆ ที่อยู่ข้างใขตัวมัน
    # สร้างปุ่มสำหรับกลับไปที่หน้า modeFrame เพื่อแสดงบน gameFrame
    back_btn = Button(gameFrame,
                      text="< Back",
                      font=50,
                      width=10,
                      bg="darkslategray4",
                      command = back_to_modeFrame) # เมื่อกดปุ่ม back จำไปทำงานที่ back_to_modeFrame()
    back_btn.grid(row=0, column=0, columnspan=5, sticky=W) # ใช้ columnspan เพื่อรวมเซลล์ทั้ง 5 column(นับตั้งแต่ column ที่มันกำหลังอยู่ไป 5 ตัว คือ 0,1,2,3,4), sticky เพื่อทำให้แสดงในทิศตะวันตก(West)
    # สร้างข้อความเพื่อแสดงบน gameFrame
    text_show_1 = Label(gameFrame,
                      text="เลือกตัวอักษรที่คุณคิดว่าถูดต้องในระหว่าง " + txt,
                      fg = _random_rgb(), # function ไหนที่มีการ return... ไม่ว่า function นั้นจะไม่มี paramiter ก็ตาม ถ้าเรียกใช้ function นั้นต้องใส่ ()
                      font=50)
    text_show_1.grid(row=1, column=0, columnspan=5, pady=5) # ใช้ columnspan เพื่อรวมเซลล์ทั้ง 5 column(นับตั้งแต่ column ที่มันกำหลังอยู่ไป 5 ตัว คือ 0,1,2,3,4)
    # ตัวอักษรสำหรับแสดงบนปุ่มคำตอบ (เริ่มที่ A)
    answer_number = 65
    # for สำหรับสร้างปุ่มในการกดตัวอักษรตั้งแต่ A-J(65-74), A-N(65-78) และ A-Z(65-90) เพื่อแสดงบน gameFrame
    # จำนวน row ที่ต้องสร้าง โดยเริ่มต้นตั้งแต่แถวที่ 2 ไปจนถึงแถวที่ ... + 2 (ถ้าเป็นอักษร A-j จะมี 2 แถว ,ถ้าเป็นอักษร A-N จะมี 3 แถว, ถ้าเป็น A-Z จะมี 6 แถว และทุกแถวจะมี 5 column)
    for r in range(2, number_of_rows_of_button+2, 1):
        # for สำหรับสร้างปุ่มตามจำนวน column 0-4
        for c in range(0, 5, 1):

            # ไม่ให้สร้าง ปุ่มคำตอบ มากกว่า คำตอบจริงๆ
            if answer_number > max_answer_btn:
                break

            # สร้างปุ่ม และแสดงบน gameFrame
            Button(gameFrame,
                   text = chr(answer_number),
                   font=10,
                   width=5,
                   bg = _random_rgb(),
                   #     เมื่อกดปุ่มแล้วต้องการให้ไปทำงาน function ที่ต้องส่ง paramiter ไปด้วน --> จะต้องใช้ lambda เพื่อกำหนดว่า function นี้สามารถส่ง paramiter ไปได้
                #    เมื่อกดปุ่มคำตอบ จะไปทำงานที่ answer_processing() โดยส่ง ตัวเลขที่ผู้ใช้เลือกตอบไป
                #    สร้างตัวแปล ans ชนิด lambda เพื่อเก็บค่าที่แสดงบนปุ่ม ของแต่ละปุ่ม (ในกรณีที่ปุ่มถูกสร้างด้วย for loop) เพื่อกำหนดให้ค่าข้อมูล ณ เวลลานั้น เป็นของปุ่มนั้นๆ
                #    ปุ่มแต่ละปุ่มจะมี ตัวแปล ans เป็นของตัวเอง ในทุกปุ่ม (และค่าข้อมูลไม่เหมือนกัน)
                   command = lambda ans = answer_number : answer_processing(ans)).grid(row=r, column=c, ipadx=3, ipady=3, padx=7, pady=7) # เพิ่ม padding ในแกน x,y ดว้ย padx,pady // เพิ่ม margin ในแกน x,y ดว้ย ipadx,ipady
            # เพิ่มเตัวเลขที่ละ 1
            answer_number += 1
    # สร้างข้อความเพื่อแสดงบน gameFrame
    text_show_2 = Label(gameFrame,
                      text="จำนวนครั้งที่สามารถตอบได้คือ " + str(number_of_times_to_play) + " ครั้ง",
                      fg = _random_rgb(), # function ไหนที่มีการ return... ไม่ว่า function นั้นจะไม่มี paramiter ก็ตาม ถ้าเรียกใช้ function นั้นต้องใส่ ()
                      font=50)
    text_show_2.grid(row = number_of_rows_of_button + 2, column=0, columnspan=5, pady=5) # ใช้ columnspan เพื่อรวมเซลล์ทั้ง 5 column(นับตั้งแต่ column ที่มันกำหลังอยู่ไป 5 ตัว คือ 0,1,2,3,4)
    # สร้างข้อความสำหรับแสดงรายละเอียดเมื่อตอบ แล้วแสดงบน gameFrame
    text_show_3 = Label(gameFrame,
                      text="...",
                      fg = _random_rgb(), # function ไหนที่มีการ return... ไม่ว่า function นั้นจะไม่มี paramiter ก็ตาม ถ้าเรียกใช้ function นั้นต้องใส่ ()
                      font=50)
    text_show_3.grid(row = number_of_rows_of_button + 3, column=0, columnspan=5, pady=5) # ใช้ columnspan เพื่อรวมเซลล์ทั้ง 5 column(นับตั้งแต่ column ที่มันกำหลังอยู่ไป 5 ตัว คือ 0,1,2,3,4)

# function เมื่อมีการกดเลือกคำตอบ โดยรับ คำตอบที่ถูกเลือก
def answer_processing(answer_number):

    # ถ้าจะทำการเปลี่ยนแปลงค่าในตัวแปล จะต้องกำหนดให้ตัวแปลนั้นเป็น globle ด้วย เพื่อบอกให้ function อื่นๆทราบว่า ตัวแปลนี้มีการเปรี่ยนแปลงค่าแล้ว
    global number_of_times_to_play
    # ถ้าจำนวนการตอบมากกว่า 0 ครั้ง ก็สามารถเล่นเกมได้ต่อไปได้
    if number_of_times_to_play > 0:

        # เมื่อมีการกดปุ่มตัวเลขเพื่อเลือกคำตอบ จะทำการลดจำนวนการเล่นลง
        number_of_times_to_play -= 1
        # เปลี่ยนข้อความที่แสดงบนหน้าจอ
        text_show_2.config(text="จำนวนครั้งที่สามารถตอบได้คือ " + str(number_of_times_to_play) + " ครั้ง")

        # ถ้าทายถูก
        if answer_number == traget:
            text_show_3.config(text="คุณตอบถูก")
            # ไปทำงานที่ endFrame()
            create_endFrame(True, answer_number)
        # ถ้าทายตัวเลขที่ มากเกินไป
        elif answer_number > traget:
            # เปลี่ยนข้อความที่แสดงบนหน้าจอ
            text_show_3.config(text="ตัวอักษร " + chr(answer_number) + " มาก เกินไป")
        # ถ้าทายตัวเลขที่ น้ายเกินไป
        elif answer_number < traget:
            # เปลี่ยนข้อความที่แสดงบนหน้าจอ
            text_show_3.config(text="ตัวอักษร " + chr(answer_number) + " น้อย เกินไป")
        
        # ถ้าตอบไม่ถูกซักที
        if answer_number > traget and number_of_times_to_play < 1 or answer_number < traget and number_of_times_to_play < 1:
            # ไปทำงานที่ endFrame()
            create_endFrame(False, answer_number)
    # ถ้าจำนวนการเล่น เป็น 0
    else:
        # ไปทำงานที่ endFrame()
        create_endFrame(False, answer_number)

# function ที่ทำการแสดงหน้าต่าง เมื่อผู้เล่นตอบ ถูก หรือ เฉลยคำตอบที่ถูกต้อง(ถ้าผู้เล่นตอบไม่ถูกเลยตามจำนวนครั้งที่กำหนดให้)
# โดยรับค่าที่บอกว่าผู้เล่น ชนะ หรือไม่ และ คำตอบที่ผู้เล่นเลือกตอบ
def create_endFrame(isWin, answer_number):

    # กำหนดให้ตัวแปลต่างๆนี้ สามารถเรียกใช้งานได้จาก function อื่นๆ
    global endFrame

    # ก่อนอื่นต้องลย gameFrame ออกจาก mainFrame
    gameFrame.destroy()
    # สร้าง endFrame เพื่อแสดงรายละเอียดผลลัพท์ แล้วแสดงบน mainFrame
    endFrame = LabelFrame(mainFrame,
                           width=800/2.5,
                           height=800/4,
                           bd=5)
    endFrame.place(relx=0.5, rely=0.5, anchor=CENTER) # ใช้ place() แล้วกำหนดให้อยู่กลางหน้าจอ 
    endFrame.pack_propagate(False) # ไม่ให้ gameFrame มีขนาด กว้าง*ยาว ที่พอดีกับ Lable อื่นๆ ที่อยู่ข้างใขตัวมัน
    # สร้างข้อความเพื่อแสดงบน endFrame
    end_text_show_1 = Label(endFrame,
                        text="",
                        font=50)
    end_text_show_1.pack(pady=10) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 30*30
    # สร้างข้อความเพื่อแสดงบน endFrame
    end_text_show_2 = Label(endFrame,
                        text="",
                        font=50)
    end_text_show_2.pack(pady=10) # แสดงบนหน้าจอโดยเว้นระยะห่าง บน*ล่าง 30*30

    # ถ้าผู้เล่นทายเลขถูก จะแสดงข้อความ
    if isWin:
        end_text_show_1.config(text="YOU WIN!!",
                               bg="chartreuse3")
        end_text_show_2.config(text="ตัวอักษร " + chr(answer_number) + " เป็นคำตอบที่ถูกต้อง")
    # ถ้าผู้เล่นทายเลขไม่ถูกเลย จะแสดงข้อความ
    else:
        end_text_show_1.config(text="YOU LOSE!!",
                               fg = "gainsboro",
                               bg = "firebrick1")
        end_text_show_2.config(text="ตัวอักษรที่ถูกต้องคือ " + chr(traget))

    # แุ่มสำหรับกลับไปหน้าเลือก game mode
    goToModeFrame_btn = Button(endFrame,
                               text="Back To The Game Mode Page",
                               font=50,
                               bg="darkslategray4",
                               command = on_endFrame_back_to_modeFrame) # เมื่อกดปุ่ม back จำไปทำงานที่ back_to_modeFrame())
    goToModeFrame_btn.pack(pady=10)

    print("end")


################################################################## Main Frame
# สร้าง หน้าต่างการทำงานหลัก
mainFrame = Tk()
mainFrame.title("Random Guessing Game") # กำหนดชื่อของ หน้าต่างการทำงานหลัก
mainFrame.geometry("800x600+200+100") # กำหนดขนาดของ หน้าต่างการทำงานหลัก กว้าง*ยาว(800x600), ในตำแหน่ง x y (+200+100)
# function ไหนที่มีการ return... ไม่ว่า function นั้นจะไม่มี paramiter ก็ตาม ถ้าเรียกใช้ function นั้นต้องใส่ ()
mainFrame.configure(bg = _random_rgb()) # ใส่สีพื้นหลังให้ หน้าต่างการทำงานหลัก




# เปิด program มาครั้งแรก จะสร้างหน้า Menu
create_menuFrame_start_exit()




# สั่งให้ หน้าต่างการทำงานหลัก แสดงผลตลอดเวลา
mainFrame.mainloop()