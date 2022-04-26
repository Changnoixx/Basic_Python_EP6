import random
import time


a = b =c =d = random.randint(0,9)
correct = location = 0
gameover = giveup = 0
print ('*********************')
print ('***** เกมทายตัวเลข *****')
print ('*********************')
print ('<<<<<<   วิธีเล่น   >>>>>')
print (' ทายตัวเลข 4 ตัว ที่ไม่ซ้ำกัน จาก 0 -9 ให้ถูกตามตำแหน่ง')
print (' หากถูกตำแหน่ง จะได้ +1 correct\n หากตัวเลขถูก แต่ไม่ถูกตำแหน่ง จะได้ +1 location\n หากต้องการยอมแพ้ กด 0000\n\n')
while a == b or a == c or a == d or b == c or b == d or c == d:
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)

print (a , b , c ,d ,' อันนี้เฉลย เอาไว้ทดสอบโปรแกรม' )  ###########คำตอบ

print ('$$$$$$ เริ่มเกมส์ $$$$$\n')
start_time = time.time()
while gameover == 0:
    ans = int(input('Your Answer => '))
    a_ans = ans // 1000
    b_ans = ((ans - (ans // 1000) * 1000)) // 100
    c_ans = ((ans - (ans // 100) * 100)) // 10
    d_ans = ((ans - (ans // 10) *10))

    #check a
    if a_ans == a:
        correct = correct+1
    elif a_ans == b or a_ans == c or a_ans == d:
        location = location+1
    #check b
    if b_ans == b:
        correct = correct+1
    elif b_ans == a or b_ans == c or b_ans == d:
        location = location+1
    #check c
    if c_ans == c:
        correct = correct+1
    elif c_ans == a or c_ans == b or c_ans == d:
        location = location+1
    #check d
    if d_ans == d:
        correct = correct+1
    elif d_ans == a or d_ans == b or d_ans == c:
        location = location+1
    #check give up
    if a_ans == b_ans == c_ans == d_ans == 0:
        giveup =1
    print (a_ans , b_ans , c_ans ,d_ans , ':>',correct ,'correct' , location , 'location')
    if correct == 4 or giveup==1:
        gameover =1
        finish_time=int(time.time()-start_time)
    correct = location = 0

if gameover==1 and giveup==0:
    
    print('********************')
    print('** CONGRATULATION **')
    print('********************')
    print(finish_time//3600 ,'hr',finish_time // 60 ,'min',finish_time %60,'sec' )
    print('*******************')
else:   
    print('********************')
    print('Answer is ',a,b,c,d)
    print('Try again next game')
    print('********************')
    print(finish_time//3600 ,'hr',finish_time // 60 ,'min',finish_time %60,'sec' )
    print('*******************')
