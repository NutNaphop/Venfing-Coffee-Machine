#import
from gtts import gTTS
import playsound

#Function
def menu ():
    print("---Choose the menu---")
    print("1. Espresso")
    print("2. Cappucino")
    print("3. Latte")

def menuTH ():
    print("---เลือกเมนู---")
    print("1. เอสเปรสโซ่")
    print("2. คาปูชิโน่")
    print("3. ลาเต้")


    
def HotorCold():
    print("---Choose the type of the coffee---")
    print("1. Hot")
    print("2. Cold ")

def HotorColdTH():
    print("---แบบร้อนหรือแบบเย็น?---")
    print("1. ร้อน")
    print("2. เย็น ")    

def space():
    print("")

def size():
    print("---Size of Cup---")
    print("1. Small for 20 bath")
    print("2. medium for 30 bath")
    print("3. Big for 40 bath")

def sizeTH():
    print("---แก้วขนาดเท่าไหร่?---")
    print("1. เล็ก ราคา 20 บาท")
    print("2. กลาง ราคา 30 บาท")
    print("3. ใหญ่ ราคา 40 บาท")

def lang():
    print("---Select your language---")
    print("1. English")
    print("2. Thai")

#Global Var

Hot = 55
Cold = 60
es = "Espresso"
cp = "Cappucino"

lt = "Latte"
h = "hot"
c = "cold"
h_th = "ร้อน"
c_th = "เย็น"

Type_Menu = ""
Type_HC = ""
Type_Cup = ""

sm = "small"
m = "medium"
b = "big"

sm_th = "เล็ก"
m_th = "กลาง"
b_th = "ใหญ่"

es_th = "เอสเปรโซ่"
cp_th = "คาปูชิโน่"
lt_th = "ลาเต้"

#code
lang()
tts = gTTS (text = "เลือกภาษาที่ต้องการใช้" , lang = "th")
tts.save("sound_th/lang.mp3")
playsound.playsound("sound_th/lang.mp3")
lang = int(input("What lauguage did you want to use: "))
if lang == 1:
    print("---Welcome to Nut's Coffee---")
    tts = gTTS (text = "please type 1 to show our menu" , lang = "en")
    tts.save("sound_eng/Wel_eng.mp3")
    playsound.playsound("sound_eng/Wel_eng.mp3")
    select_type = (int(input("please type 1 to show our menu : ")))
    space()
    if select_type == 1:
        menu()
        tts = gTTS (text = "Select coffee" , lang = "en")
        tts.save("sound_eng/Select_eng.mp3")
        playsound.playsound("sound_eng/Select_eng.mp3")
        select_menu = int(input("Select coffee: "))
        space()
        if select_menu >0 and select_menu <=3:
            if select_menu == 1:
                Type_Menu += es
            elif select_menu == 2:
                Type_Menu  += cp
            elif select_menu == 3:
                Type_Menu  += lt
        else:
            space()
            print("---Type 1 or 2 or 3 only please try again---")
            tts = gTTS (text = "Type 1 or 2 or 3 only please try again" , lang = "en")
            tts.save("sound_eng/123try_eng.mp3")
            playsound.playsound("sound_eng/123try_eng.mp3")
        
        if es in Type_Menu or cp in Type_Menu or lt in Type_Menu:
            HotorCold()
            tts = gTTS (text = "Hot or cold" , lang = "en")
            tts.save("sound_eng/sctype_eng.mp3")
            playsound.playsound("sound_eng/sctype_eng.mp3")
            select_HC = int(input("Select type :"))
            space()
            if select_HC >=0 and select_HC <=2:
                size()
                tts = gTTS (text = "What Size of Cup of Coffee did you want" , lang = "en")
                tts.save("sound_eng/size_eng.mp3")
                playsound.playsound("sound_eng/size_eng.mp3")
                size_c = int(input("What Size did you want: "))
                if size_c == 1:
                    Type_Cup += sm
                elif size_c == 2:
                    Type_Cup += m
                elif size_c == 3:
                    Type_Cup += b
                else:
                    space()
                    print("---Type 1 or 2 or 3 please try again---")
                    tts = gTTS (text = "Type 1 or 2 or 3 only please try again" , lang = "en")
                    tts.save("sound_eng/123try_eng.mp3")
                    playsound.playsound("sound_eng/123try_eng.mp3")
            else:
                space()
                print("------Type 1 or 2 only please try again------")
                tts = gTTS (text = "Type 1 or 2 only please try again" , lang = "en")
                tts.save("sound_eng/12try_eng.mp3")
                playsound.playsound("sound_eng/12try_eng.mp3")
                
            if select_HC>0 and select_HC <=2 :
                if select_HC == 1 and size_c == 1:
                    Type_HC += h
                    space()
                    print("---You choose %s hot %s 20 bath---"%(Type_Cup,Type_Menu))
                    tts = gTTS (text = "you choose %s hot %s for 20 bath"%(Type_Cup,Type_Menu) , lang = "en")
                    tts.save("sound_eng/h_small_eng.mp3")
                    playsound.playsound("sound_eng/h_small_eng.mp3")
                elif select_HC == 1 and size_c == 2:
                    Type_HC += h 
                    space() 
                    print("---You choose %s hot %s 30 bath---"%(Type_Cup,Type_Menu))
                    tts = gTTS (text = "you choose %s hot %s for 30 bath"%(Type_Cup,Type_Menu) , lang = "en")
                    tts.save("sound_eng/h_medium_eng.mp3")
                    playsound.playsound("sound_eng/h_medium_eng.mp3")
                    
                elif select_HC == 1 and size_c == 3:
                    Type_HC += h  
                    space()
                    print("---You choose %s hot %s 40 bath---"%(Type_Cup,Type_Menu))
                    tts = gTTS (text = "you choose %s hot %s for 40 bath"%(Type_Cup,Type_Menu) , lang = "en")
                    tts.save("sound_eng/h_big_eng.mp3")
                    playsound.playsound("sound_eng/h_big_eng.mp3")
                elif select_HC == 2 and size_c == 1:
                    Type_HC += c  
                    space() 
                    print("---You choose %s cold %s 20 bath---"%(Type_Cup,Type_Menu))
                    tts = gTTS (text = "you choose %s cold %s for 20 bath"%(Type_Cup,Type_Menu) , lang = "en")
                    tts.save("sound_eng/c_small_eng.mp3")
                    playsound.playsound("sound_eng/c_small_eng.mp3")
                    
                elif select_HC == 2 and size_c == 2:
                    Type_HC += c  
                    space()
                    print("---You choose %s cold %s 30 bath---"%(Type_Cup,Type_Menu))
                    tts = gTTS (text = "you choose %s cold %s for 30 bath"%(Type_Cup,Type_Menu) , lang = "en")
                    tts.save("sound_eng/c_medium_eng.mp3")
                    playsound.playsound("sound_eng/c_medium_eng.mp3")
                elif select_HC == 2 and size_c ==3:
                    Type_HC += c  
                    space()
                    print("---You choose %s cold %s 40 bath---"%(Type_Cup,Type_Menu))
                    tts = gTTS (text = "you choose %s cold %s for 40 bath"%(Type_Cup,Type_Menu) , lang = "en")
                    tts.save("sound_eng/c_big_eng.mp3")
                    playsound.playsound("sound_eng/c_big_eng.mp3")
                                         
        
            
        if "hot" in Type_HC or "cold" in Type_HC :
            tts = gTTS (text = "Please Insert your money" , lang = "en")
            tts.save("sound_eng/insert_eng.mp3")
            playsound.playsound("sound_eng/insert_eng.mp3")
            money = int(input("Insert your money: "))
            if money == 20 or money == 30 or money == 40:
                if money == 20 and Type_HC == h and Type_Cup == sm:
                    space()
                    print("---Please wait---")
                    tts = gTTS (text = "please wait" , lang = "en")
                    tts.save("sound_eng/pls_eng.mp3")
                    playsound.playsound("sound_eng/pls_eng.mp3")
                    print("---Thank you---")
                    print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
                    tts = gTTS (text = "Thank you Your %s %s %s is here enjoy with us coffee "%(Type_Cup,Type_HC,Type_Menu) , lang = "en")
                    tts.save("sound_eng/h_sm_eng.mp3")
                    playsound.playsound("sound_eng/h_sm_eng.mp3")
                
                        
                elif money == 30 and Type_HC == h and Type_Cup == m:
                    space()
                    print("---Please wait---")
                    tts = gTTS (text = "please wait" , lang = "en")
                    tts.save("sound_eng/pls_eng.mp3")
                    playsound.playsound("sound_eng/pls_eng.mp3")
                    print("---Thank you---")
                    print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
                    tts = gTTS (text = "Thank you Your %s %s %s is here enjoy with us coffee "%(Type_Cup,Type_HC,Type_Menu) , lang = "en")
                    tts.save("sound_eng/h_m_eng.mp3")
                    playsound.playsound("sound_eng/h_m_eng.mp3")
                                       
                        
                elif money ==40 and Type_HC == h and Type_Cup == b:
                    space()
                    print("---Please wait---")
                    tts = gTTS (text = "please wait" , lang = "en")
                    tts.save("sound_eng/pls_eng.mp3")
                    playsound.playsound("sound_eng/pls_eng.mp3")
                    print("---Thank you---")
                    print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
                    tts = gTTS (text = "Thank you Your %s %s %s is here enjoy with us coffee "%(Type_Cup,Type_HC,Type_Menu) , lang = "en")
                    tts.save("sound_eng/h_b_eng.mp3")
                    playsound.playsound("sound_eng/h_b_eng.mp3")
                    
                
                elif money == 20 and Type_HC == c and Type_Cup == sm:
                    space()
                    print("---Please wait---")
                    tts = gTTS (text = "please wait" , lang = "en")
                    tts.save("sound_eng/pls_eng.mp3")
                    playsound.playsound("sound_eng/pls_eng.mp3")
                    print("---Thank you---")
                    print("---our %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
                    tts = gTTS (text = "Thank you Your %s %s %s is here enjoy with us coffee "%(Type_Cup,Type_HC,Type_Menu) , lang = "en")
                    tts.save("sound_eng/c_sm_eng.mp3")
                    playsound.playsound("sound_eng/c_sm_eng.mp3")
                
                        
                elif money == 30 and Type_HC == c and Type_Cup == m:
                    space()
                    print("---Please wait---")
                    tts = gTTS (text = "please wait" , lang = "en")
                    tts.save("sound_eng/pls_eng.mp3")
                    playsound.playsound("sound_eng/pls_eng.mp3")
                    print("---Thank you---")
                    print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
                    tts = gTTS (text = "Thank you Your %s %s %s is here enjoy with us coffee "%(Type_Cup,Type_HC,Type_Menu) , lang = "en")
                    tts.save("sound_eng/c_m_eng.mp3")
                    playsound.playsound("sound_eng/c_m_eng.mp3")
                    
                                       
                        
                elif money ==40 and Type_HC == c and Type_Cup == b:
                    space()
                    print("---Please wait---")
                    tts = gTTS (text = "please wait" , lang = "en")
                    tts.save("sound_eng/pls_eng.mp3")
                    playsound.playsound("sound_eng/pls_eng.mp3")
                    print("---Thank you---")
                    print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
                    tts = gTTS (text = "Thank you Your %s %s %s is here enjoy with us coffee "%(Type_Cup,Type_HC,Type_Menu) , lang = "en")
                    tts.save("sound_eng/c_b_eng.mp3")
                    playsound.playsound("sound_eng/c_b_eng.mp3")
                
                else:
                    space()
                    print("---Your money isn't true with this order please contact the Owner ---")
                    tts = gTTS (text = "Your money isn't true with this order please contact the Owner", lang = "en")
                    tts.save("sound_eng/conOwn1_eng.mp3")
                    playsound.playsound("sound_eng/conOwn1_eng.mp3")                                    
            else: 
                space()
                print("---Please Insert your money follow the order please contact the Owner ---")
                tts = gTTS (text = "Please Insert your money follow the order please contact the Owner", lang = "en")
                tts.save("sound_eng/conOwn2_eng.mp3")
                playsound.playsound("sound_eng/conOwn2_eng.mp3")     
    
    else: 
        space()
        print("---Type 1 only please try again---")
        tts = gTTS (text = "Type 1 only please try again" , lang = "en")
        tts.save("sound_eng/1try_eng.mp3")
        playsound.playsound("sound_eng/1try_eng.mp3")

elif lang == 2:
    print("--ยินดีต้อนรับสู่ร้านกาแฟของณัช---")
    tts = gTTS (text = "กด 1 เพื่อดูเมนูของเรา" , lang = "th")
    tts.save("sound_th/Wel_th.mp3")
    playsound.playsound("sound_th/Wel_th.mp3")
    select_type = (int(input("กด 1 เพื่อดูเมนูของเรา : ")))
    space()
    if select_type == 1:
        menuTH()
        tts = gTTS (text = "เมนุที่ต้องการเลือก" , lang = "th")
        tts.save("sound_th/Menu_th.mp3")
        playsound.playsound("sound_th/Menu_th.mp3")
        select_menu = int(input("เมนูที่ต้องการเลือก?: "))
        space()
        if select_menu >0 and select_menu <=3:
            if select_menu == 1:
                Type_Menu += es_th
            elif select_menu == 2:
                Type_Menu  += cp_th
            elif select_menu == 3:
                Type_Menu  += lt_th
        else:
            space()
            print("---กด 1 หรือ 2 หรือ 3 เท่านั้น ลองใหม่อีกครั้ง---")
            tts = gTTS (text = "กด1หรือ2หรือ3เท่านั้นลองใหม่อีกครั้ง" , lang = "th")
            tts.save("sound_th/123try_th.mp3")
            playsound.playsound("sound_th/123try_th.mp3")
        
        if es_th in Type_Menu or cp_th in Type_Menu or lt_th in Type_Menu:
            HotorColdTH()
            tts = gTTS (text = "แบบร้อนหรือแบบเย็น" , lang = "th")
            tts.save("sound_th/HC_th.mp3")
            playsound.playsound("sound_th/HC_th.mp3")
            select_HC = int(input("แบบร้อนหรือแบบเย็น?: "))
            space()
            if select_HC >=0 and select_HC <=2:
                sizeTH()
                tts = gTTS (text = "เอาแก้วขนาดไหน?" , lang = "th")
                tts.save("sound_th/size_th.mp3")
                playsound.playsound("sound_th/size_th.mp3")
                size_c = int(input("เอาแก้วขนาดไหน?: "))
                if size_c == 1:
                    Type_Cup += sm_th
                elif size_c == 2:
                    Type_Cup += m_th 
                elif size_c == 3:
                    Type_Cup += b_th
                else:
                    space()
                    print("---กด 1 หรือ 2 หรือ 3 เท่านั้น ลองใหม่อีกครั้ง---")
                    tts = gTTS (text = "กด1หรือ2หรือ3เท่านั้นลองใหม่อีกครั้ง" , lang = "th")
                    tts.save("sound_th/123try_th.mp3")
                    playsound.playsound("sound_th/123try_th.mp3")
            else:
                space()
                print("------กด 1 หรือ 2 เท่านั้น ลองใหม่อีกครั้ง------")
                tts = gTTS (text = "กด1หรือ2เท่านั้น ลองใหม่อีกครั้ง" , lang = "th")
                tts.save("sound_th/12try_th.mp3")
                playsound.playsound("sound_th/12try_th.mp3")
                
            if select_HC>0 and select_HC <=2 :
                if select_HC == 1 and size_c == 1:
                    Type_HC += h_th
                    space()
                    print("---คุณได้เลือก %sร้อน แก้ว%s ราคา 20 บาท---"%(Type_Menu,Type_Cup))
                    tts = gTTS (text = "คุณได้เลือก %sร้อน แก้ว%s ราคา 20 บาท"%(Type_Menu,Type_Cup) , lang = "th")
                    tts.save("sound_th/coffee_hot_small_th.mp3")
                    playsound.playsound("sound_th/coffee_hot_small_th.mp3")
                elif select_HC == 1 and size_c == 2:
                    Type_HC += h_th 
                    space() 
                    print("---คุณได้เลือก %sร้อน แก้ว%s ราคา 30 บาท---"%(Type_Menu,Type_Cup))
                    tts = gTTS (text = "คุณได้เลือก %sร้อน แก้ว%s ราคา 30 บาท"%(Type_Menu,Type_Cup) , lang = "th")
                    tts.save("sound_th/coffee_hot_medium_th.mp3")
                    playsound.playsound("sound_th/coffee_hot_medium_th.mp3")
                    
                elif select_HC == 1 and size_c == 3:
                    Type_HC += h_th  
                    space()
                    print("---คุณได้เลือก %sร้อน แก้ว%s ราคา 40 บาท---"%(Type_Menu,Type_Cup))
                    tts = gTTS (text = "คุณได้เลือก %sร้อน แก้ว%s ราคา 40 บาท"%(Type_Menu,Type_Cup) , lang = "th")
                    tts.save("sound_th/coffee_hot_big_th.mp3")
                    playsound.playsound("sound_th/coffee_hot_big_th.mp3")
                    
                elif select_HC == 2 and size_c == 1:
                    Type_HC += c_th  
                    space() 
                    print("---คุณได้เลือก %sเย็น แก้ว%s ราคา 20 บาท---"%(Type_Menu,Type_Cup))
                    tts = gTTS (text = "คุณได้เลือก %sเย็น แก้ว%s ราคา 20 บาท"%(Type_Menu,Type_Cup) , lang = "th")
                    tts.save("sound_th/coffee_cold_small_th.mp3")
                    playsound.playsound("sound_th/coffee_cold_small_th.mp3")
                    
                elif select_HC == 2 and size_c == 2:
                    Type_HC += c_th  
                    space()
                    print("---คุณได้เลือก %sเย็น แก้ว%s ราคา 30 บาท---"%(Type_Menu,Type_Cup))
                    tts = gTTS (text = "คุณได้เลือก %sเย็น แก้ว%s ราคา 30 บาท"%(Type_Menu,Type_Cup) , lang = "th")
                    tts.save("sound_th/coffee_cold_medium_th.mp3")
                    playsound.playsound("sound_th/coffee_cold_medium_th.mp3")
                     
                elif select_HC == 2 and size_c ==3:
                    Type_HC += c_th  
                    space()
                    print("---คุณได้เลือก %sเย็น แก้ว%s ราคา 40 บาท---"%(Type_Menu,Type_Cup))
                    tts = gTTS (text = "คุณได้เลือก %sเย็น แก้ว%s ราคา 40 บาท"%(Type_Menu,Type_Cup) , lang = "th")
                    tts.save("sound_th/coffee_cold_big_th.mp3")
                    playsound.playsound("sound_th/coffee_cold_big_th.mp3")
                                         
        
            
        if "ร้อน" in Type_HC or "เย็น" in Type_HC :
            tts = gTTS (text = "โปรดใส่เงินของคุณ", lang = "th")
            tts.save("sound_th/money.mp3")
            playsound.playsound("sound_th/money.mp3")
            money = int(input("ใส่เงินของคุณ : "))
            if money == 20 or money == 30 or money == 40:
                if money == 20 and Type_HC == h_th and Type_Cup == sm_th:
                    space()
                    tts = gTTS (text = "รอสักครู", lang = "th")
                    tts.save("sound_th/wait_th.mp3")
                    playsound.playsound("sound_th/wait_th.mp3")
                    print("---รอสักครู่---")
                    print("---ขอบคุณ---")
                    print("---เมนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา---"%(Type_Menu,Type_HC,Type_Cup))
                    tts = gTTS (text = "ขอบคุณที่ใช้บริการ เมนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา "%(Type_Menu,Type_HC,Type_Cup), lang = "th")
                    tts.save("sound_th/thank_h_small.mp3")
                    playsound.playsound("sound_th/thank_h_small.mp3")
                
                        
                elif money == 30 and Type_HC == h_th and Type_Cup == m_th:
                    space()
                    tts = gTTS (text = "รอสักครู", lang = "th")
                    tts.save("sound_th/wait_th.mp3")
                    playsound.playsound("sound_th/wait_th.mp3")
                    print("---รอสักครู่---")
                    print("---ขอบคุณ---")
                    print("---เมนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา---"%(Type_Menu,Type_HC,Type_Cup))
                    tts = gTTS (text = "ขอบคุณที่ใช้บริการ เมนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา "%(Type_Menu,Type_HC,Type_Cup), lang = "th")
                    tts.save("sound_th/thank_h_medium.mp3")
                    playsound.playsound("sound_th/thank_h_medium.mp3")
                                       
                        
                elif money ==40 and Type_HC == h_th and Type_Cup == b_th:
                    space()
                    tts = gTTS (text = "รอสักครู", lang = "th")
                    tts.save("sound_th/wait_th.mp3")
                    playsound.playsound("sound_th/wait_th.mp3")
                    print("---รอสักครู่---")
                    print("---ขอบคุณ---")
                    print("---เมนู %s%s แก้ว%s อยู่ตรงนี้แล้วข้อให้อร่อยกับกาแฟของเรา---"%(Type_Menu,Type_HC,Type_Cup))
                    tts = gTTS (text = "ขอบคุณที่ใช้บริการ เมนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา "%(Type_Menu,Type_HC,Type_Cup), lang = "th")
                    tts.save("sound_th/thank_h_big.mp3")
                    playsound.playsound("sound_th/thank_h_big.mp3")
                
                elif money == 20 and Type_HC == c_th and Type_Cup == sm_th:
                    space()
                    tts = gTTS (text = "รอสักครู", lang = "th")
                    tts.save("sound_th/wait_th.mp3")
                    playsound.playsound("sound_th/wait_th.mp3")
                    print("---รอสักครู่---")
                    print("---ขอบคุณ---")
                    print("---มนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา---"%(Type_Menu,Type_HC,Type_Cup))
                    tts = gTTS (text = "ขอบคุณที่ใช้บริการ เมนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา "%(Type_Menu,Type_HC,Type_Cup), lang = "th")
                    tts.save("sound_th/thank_c_small.mp3")
                    playsound.playsound("sound_th/thank_c_small.mp3")
                
                        
                elif money == 30 and Type_HC == c_th and Type_Cup == m_th:
                    space()
                    tts = gTTS (text = "รอสักครู", lang = "th")
                    tts.save("sound_th/wait_th.mp3")
                    playsound.playsound("sound_th/wait_th.mp3")
                    print("---รอสักครู่---")
                    print("---ขอบคุณ---")
                    print("---มนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา---"%(Type_Menu,Type_HC,Type_Cup))
                    tts = gTTS (text = "ขอบคุณที่ใช้บริการ เมนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา "%(Type_Menu,Type_HC,Type_Cup), lang = "th")
                    tts.save("sound_th/thank_c_medium.mp3")
                    playsound.playsound("sound_th/thank_c_medium.mp3")
                                       
                        
                elif money ==40 and Type_HC == c_th and Type_Cup == b_th:
                    space()
                    tts = gTTS (text = "รอสักครู", lang = "th")
                    tts.save("sound_th/wait_th.mp3")
                    playsound.playsound("sound_th/wait_th.mp3")
                    print("---รอสักครู่---")
                    print("---ขอบคุณ---")
                    print("---เมนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา---"%(Type_Menu,Type_HC,Type_Cup))
                    tts = gTTS (text = "ขอบคุณที่ใช้บริการ เมนู %s%s แก้ว%s อยู่ตรงนี้แล้ว ขอให้อร่อยกับกาแฟของเรา "%(Type_Menu,Type_HC,Type_Cup), lang = "th")
                    tts.save("sound_th/thank_c_big.mp3")
                    playsound.playsound("sound_th/thank_c_big.mp3")                
                else:
                    space()
                    print("---คุณป้อนเงินไม่ถูกตามจํานวน โปรดติดต่อเจ้าของร้าน ---")
                    tts = gTTS (text = "คุณป้อนเงินไม่ถูกตามจํานวน โปรดติดต่อเจ้าของร้าน", lang = "th")
                    tts.save("sound_th/contactOwn.mp3")
                    playsound.playsound("sound_th/contactOwn.mp3")                                    
            else: 
                space()
                print("---คุณไม่ได้ใส่เงินตามจํานวนที่คุณได้สั่งไว้ โปรดติดต่อเจ้าของร้าน ---")
                tts = gTTS (text = "คุณไม่ได้ใส่เงินตามจํานวนที่คุณได้สั่งไว้ โปรดติดต่อเจ้าของร้าน", lang = "th")
                tts.save("sound_th/contactOwn2.mp3")
                playsound.playsound("sound_th/contactOwn2.mp3") 
    
    else: 
        space()
        print("---กด 1 เท่านั้น โปรดลองอีกครั้ง ---")
        tts = gTTS (text = "กด 1 เท่านั้น โปรดลองอีกครั้ง", lang = "th")
        tts.save("sound_th/1try.mp3")
        playsound.playsound("sound_th/1try.mp3")     

else:
    print("---กด 1 หรือ 2 เท่านั้น โปรดลองอีกครั้ง---")
    tts = gTTS (text = "กด1หรือ2เท่านั้น ลองใหม่อีกครั้ง" , lang = "th")
    tts.save("sound_th/12try_th.mp3")
    playsound.playsound("sound_th/12try_th.mp3") 