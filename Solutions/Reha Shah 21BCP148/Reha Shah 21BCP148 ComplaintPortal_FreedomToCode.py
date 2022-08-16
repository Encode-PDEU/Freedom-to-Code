import pygame
import mysql.connector as m

mo=m.connect(host='localhost',user='root',password='reha',database='compl_port')
co=mo.cursor()
co.execute("use compl_port")
#co.execute("create table user_data(u_no integer primary key,name char(100) not null,aadhar_no integer unique,password char(40) not null")
#co.execute("create table complaint_log(c_no integer primary key,logged_by_u_no integer,comp_type char(100),description varchar(1000) not null,solution varchar(1000) default 'in process',status char(15) default 'unresolved')")
#co.execute("create table feedback(f_no integer primary key, given_by_u_no integer,feedback char(200) not null,status char(20))")

pygame.init()
dis=pygame.display.set_mode((1200,680))
t=pygame.time.Clock()
pygame.display.set_caption('Complaint Portal')

#to display text
def txt_dis(t,xy,size=25,rbg=(255,255,255)):
    global dis
    fo=pygame.font.SysFont('Agency FB',size)
    tx=fo.render(t,1,rbg)
    dis.blit(tx,xy)
  
#to take text as input
def txt_inp(t,key):
    keys=pygame.key.get_pressed()
    if len(key)==1:
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            t+=key.upper()
        else:
            t+=key
    elif key=='backspace':
        t=t[:len(t)-1]
    elif key=='space':
        t+=' '
    return t

#loop so that we can log in and out without restarting the program
l=1
k=1
while k and l:
    a=1
    u=u1=1
    #input for whether it is a user or administrator
    while a and l:
        event=pygame.event.poll()
        keys=pygame.key.get_pressed()
        if event.type==pygame.QUIT:
            l=0
        if event.type==pygame.MOUSEBUTTONDOWN:
            cur=pygame.mouse.get_pos()
            if 300<cur[0]<900 and 305<cur[1]<355:
                a=0
            elif 300<cur[0]<900 and 390<cur[1]<440:
                u=a=0
        dis.fill((26,159,174))
        pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,305,600,50))
        pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,390,600,50))
        txt_dis("Which User Interface do you want to use ?",(255,160),50)
        txt_dis("USER (to log complaints)",(305,315),30)
        txt_dis("ADMINISTRATOR (need authorization)",(305,400),30)
        pygame.display.update()
        
    #if it is user
    if u and u1:
        b=z=1
        #to choose log in or sign in
        while b and l:
            event=pygame.event.poll()
            keys=pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                l=0
            if event.type==pygame.MOUSEBUTTONDOWN:
                cur=pygame.mouse.get_pos()
                if 45<cur[0]<90 and 40<cur[1]<80:
                    b=z=0
                    
                elif 300<cur[0]<900 and 305<cur[1]<355:
                    #log in page
                    b1=1
                    b2=0
                    adr=pas=''
                    while b1 and l:
                        event=pygame.event.poll()
                        keys=pygame.key.get_pressed()
                        if event.type==pygame.QUIT:
                            l=0
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            cur=pygame.mouse.get_pos()
                            if 300<cur[0]<900 and 300<cur[1]<345:
                                b2=1
                            elif 300<cur[0]<900 and 425<cur[1]<470:
                                b2=2
                            elif 45<cur[0]<90 and 40<cur[1]<80:
                                b1=0
                            elif 550<cur[0]<650 and 550<cur[1]<595:
                                if adr.isdigit():
                                    ins='select * from user_data where aadhar_no = %s'
                                    par=(int(adr),0)
                                    co.execute(ins,par[0:1])
                                    data=co.fetchone()
                                    if data==None or data[3]!=pas:
                                        adr=pas=''
                                    else:
                                        b1=b=0
                                else:
                                    adr=pas=''
                        if b2==1:
                            if event.type==pygame.KEYDOWN:
                                key=pygame.key.name(event.key)
                                adr=txt_inp(adr,key)
                        elif b2==2:
                            if event.type==pygame.KEYDOWN:
                                key=pygame.key.name(event.key)
                                pas=txt_inp(pas,key)
                        dis.fill((30,180,70))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,300,600,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,425,600,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(550,550,100,45))
                        txt_dis("BACK",(50,50),20)
                        txt_dis("LOG IN",(305,140),50)
                        txt_dis("Enter Aadhar Number",(305,250),30)
                        txt_dis(adr,(305,310))
                        txt_dis("Enter Password",(305,375),30)
                        txt_dis(pas,(305,435))
                        txt_dis("ENTER",(575,560))
                        pygame.display.update()
                        
                elif 300<cur[0]<900 and 390<cur[1]<440:
                    #sign in page
                    b1=1
                    b2=0
                    adr=pas=nam=''
                    while b1 and l:
                        event=pygame.event.poll()
                        keys=pygame.key.get_pressed()
                        if event.type==pygame.QUIT:
                            l=0
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            cur=pygame.mouse.get_pos()
                            if 300<cur[0]<900 and 255<cur[1]<300:
                                b2=1
                            elif 300<cur[0]<900 and 375<cur[1]<420:
                                b2=2
                            elif 300<cur[0]<900 and 495<cur[1]<540:
                                b2=3
                            elif 45<cur[0]<90 and 40<cur[1]<80:
                                b1=0
                            elif 550<cur[0]<650 and 580<cur[1]<625:
                                if adr.isdigit() and len(adr)==12 and 0<len(nam)<100 and 0<len(pas)<40:
                                    ins='select * from user_data where aadhar_no = %s'
                                    par=(int(adr),0)
                                    co.execute(ins,par[0:1])
                                    data=co.fetchone()
                                    if data==None:
                                        co.execute("select max(u_no) from user_data")
                                        luno=co.fetchone()
                                        if luno[0]==None:
                                            muno=1
                                        else:
                                            muno=luno[0]+1
                                        ins='insert into user_data values(%s,%s,%s,%s)'
                                        par=(muno,nam,int(adr),pas)
                                        co.execute(ins,par)
                                        mo.commit()
                                        data=par
                                        b1=b=0
                                    else:
                                        adr=''
                                else:
                                    adr=nam=pas=''
                        if b2==1:
                            if event.type==pygame.KEYDOWN:
                                key=pygame.key.name(event.key)
                                nam=txt_inp(nam,key)
                        elif b2==2:
                            if event.type==pygame.KEYDOWN:
                                key=pygame.key.name(event.key)
                                adr=txt_inp(adr,key)
                        elif b2==3:
                            if event.type==pygame.KEYDOWN:
                                key=pygame.key.name(event.key)
                                pas=txt_inp(pas,key)
                        dis.fill((30,180,70))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,255,600,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,375,600,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,495,600,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(550,580,100,45))
                        txt_dis("BACK",(50,50),20)
                        txt_dis("SIGN IN",(305,100),50)
                        txt_dis("Enter Name (max.length 99)",(305,210),30)
                        txt_dis(nam,(305,265))
                        txt_dis("Enter Aadhar Number (12 digits)",(305,330),30)
                        txt_dis(adr,(405,385))
                        txt_dis("Enter Password (max.length 39)",(305,450),30)
                        txt_dis(pas,(305,505))
                        txt_dis("ENTER",(575,590))
                        pygame.display.update()
                        
            dis.fill((200,100,30))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,305,600,50))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,390,600,50))
            txt_dis("BACK",(50,50),20)
            txt_dis("Already existing user or new user ?",(305,160),50)
            txt_dis("LOG IN (for already existing users)",(305,315),30)
            txt_dis("SIGN IN (for new user)",(305,400),30)
            pygame.display.update()
            
        #user home page
        while z and l:
            event=pygame.event.poll()
            keys=pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                l=0
            if event.type==pygame.MOUSEBUTTONDOWN:
                cur=pygame.mouse.get_pos()
                if 1100<cur[0]<1160 and 600<cur[1]<640:
                    z=0
                    
                elif 150<cur[0]<550 and 250<cur[1]<350:
                    #user profile page
                    z1=1
                    while z1 and l:
                        event=pygame.event.poll()
                        keys=pygame.key.get_pressed()
                        if event.type==pygame.QUIT:
                            l=0
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            cur=pygame.mouse.get_pos()
                            if 45<cur[0]<90 and 40<cur[1]<80:
                                z1=0
                        dis.fill((130,80,20))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                        txt_dis("BACK",(50,50),20)
                        txt_dis("USER PROFILE",(100,100),50)
                        txt_dis("Name: "+data[1],(200,200),30)
                        txt_dis("Aadhar Number: "+str(data[2]),(200,290),30)
                        txt_dis("Password: "+data[3],(200,380),30)
                        co.execute('select count(*) from complaint_log where logged_by_u_no=%s',(data[0],))
                        tnc=co.fetchone()
                        txt_dis("Number of complaints logged: "+str(tnc[0]),(200,470),30)
                        co.execute("select count(*) from complaint_log where logged_by_u_no=%s and status='resolved'",(data[0],))
                        rnc=co.fetchone()
                        txt_dis("Number of complaints resolved: "+str(rnc[0]),(200,560),30)
                        pygame.display.update()
                        
                elif 650<cur[0]<1050 and 250<cur[1]<350:
                    #Complaint Log Page
                    z1=1
                    cno=''
                    while z1 and l:
                        event=pygame.event.poll()
                        keys=pygame.key.get_pressed()
                        if event.type==pygame.QUIT:
                            l=0
                        if event.type==pygame.KEYDOWN:
                            key=pygame.key.name(event.key)
                            cno=txt_inp(cno,key)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            cur=pygame.mouse.get_pos()
                            if 45<cur[0]<90 and 40<cur[1]<80:
                                z1=0
                                
                            elif 1065<cur[0]<1150 and 120<cur[1]<165:
                                co.execute("select c_no from complaint_log where logged_by_u_no=%s order by c_no",(data[0],))
                                lcno=co.fetchmany(10)
                                tcno=(int(cno),)
                                if cno.isdigit():
                                    if tcno in lcno:
                                        #individual complaint details page
                                        co.execute('select * from complaint_log where c_no=%s',tcno)
                                        datac=co.fetchone()
                                        cmt=datac[2]
                                        des=datac[3]
                                        z2=1
                                        z4=0
                                        while z2 and l:
                                            event=pygame.event.poll()
                                            keys=pygame.key.get_pressed()
                                            if event.type==pygame.QUIT:
                                                l=0
                                            if event.type==pygame.MOUSEBUTTONDOWN:
                                                cur=pygame.mouse.get_pos()
                                                if 45<cur[0]<90 and 40<cur[1]<80:
                                                    z2=0
                                                    cno=''
                                                elif 50<cur[0]<1050 and 195<cur[1]<240:
                                                    z4=1
                                                elif 50<cur[0]<1150 and 300<cur[1]<600:
                                                    z4=2
                                                elif 915<cur[0]<1165 and 140<cur[1]<185:
                                                    co.execute('update complaint_log set comp_type=%s where c_no=%s',(cmt,datac[0]))
                                                    co.execute('update complaint_log set description=%s where c_no=%s',(des,datac[0]))
                                                    co.execute('update complaint_log set status=%s where c_no=%s',('unresolved',datac[0]))
                                                    mo.commit()
                                                    co.execute('select * from complaint_log where c_no=%s',tcno)
                                                    datac=co.fetchone()
                                                    z2=0
                                                    cno=''
                                                    
                                                elif 900<cur[0]<1110 and 65<cur[1]<110:
                                                    #Solution and Status display Page
                                                    z3=1
                                                    sol=datac[4]
                                                    while z3 and l:
                                                        event=pygame.event.poll()
                                                        keys=pygame.key.get_pressed()
                                                        if event.type==pygame.QUIT:
                                                            l=0
                                                        if event.type==pygame.MOUSEBUTTONDOWN:
                                                            cur=pygame.mouse.get_pos()
                                                            if 45<cur[0]<90 and 40<cur[1]<80:
                                                                z3=0
                                                        dis.fill((45,90,105))
                                                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                                                        txt_dis("BACK",(50,50),20)
                                                        txt_dis("SOLUTION FOR COMPLAINT "+cno,(100,100),50)
                                                        for i in range((len(sol)//100)+1):
                                                            txt_dis(sol[i*100:(i*100)+100],(55,210+(i*35)))
                                                        txt_dis("STATUS: "+datac[5],(100,605),30)
                                                        pygame.display.update()
                                            if z4==1:
                                                if event.type==pygame.KEYDOWN:
                                                    key=pygame.key.name(event.key)
                                                    cmt=txt_inp(cmt,key)
                                            elif z4==2:
                                                if event.type==pygame.KEYDOWN:
                                                    key=pygame.key.name(event.key)
                                                    if len(des)<=1000:
                                                        des=txt_inp(des,key)
                                            dis.fill((218,165,32))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(915,140,250,45))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(900,65,210,45))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(50,195,1000,45))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(50,300,1100,360))
                                            txt_dis("COMPLAINT "+cno,(100,90),50)
                                            txt_dis("BACK",(50,50),20)
                                            txt_dis("click here to see Solution",(905,75))
                                            txt_dis("Complaint Type (can update if want to)",(55,155),30)
                                            txt_dis(cmt,(55,205))
                                            txt_dis("Description of the complaint (can update if you want to)",(55,260),30)
                                            for i in range((len(des)//100)+1):
                                                txt_dis(des[i*100:(i*100)+100],(55,310+(i*35)))
                                            txt_dis("UPDATE (status - unresolved)",(920,150))
                                            pygame.display.update()
                                            
                                    else:
                                        cno=''
                                else:
                                    cno=''
                        dis.fill((12,120,44))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(700,50,475,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(1065,120,85,45))
                        txt_dis("BACK",(50,50),20)
                        txt_dis("Enter Complaint Number to view complaint details: "+cno,(705,60))
                        txt_dis("ENTER",(1085,130))
                        txt_dis("YOUR RECENT COMPLAINTS",(100,100),50)
                        txt_dis("Complaint No.    Complaint Type"+" "*145+"Status",(50,200))
                        co.execute("select * from complaint_log where logged_by_u_no=%s order by c_no",(data[0],))
                        unl=co.fetchmany(10)
                        x=0
                        for i in unl:
                            txt_dis(str(i[0]).ljust(25,' ')+(i[2]),(50,260+(40*x)))
                            txt_dis(i[5],(1000,260+(40*x)))
                            x+=1
                        pygame.display.update()
                        
                elif 150<cur[0]<550 and 450<cur[1]<550:
                    #Feedback Input Page
                    z1=1
                    z2=0
                    fed=''
                    while z1 and l:
                        event=pygame.event.poll()
                        keys=pygame.key.get_pressed()
                        if event.type==pygame.QUIT:
                            l=0
                        elif event.type==pygame.MOUSEBUTTONDOWN:
                            cur=pygame.mouse.get_pos()
                            if 45<cur[0]<90 and 40<cur[1]<80:
                                z1=0
                            if 50<cur[0]<1150 and 250<cur[1]<350:
                                z2=1
                            if 1050<cur[0]<1100 and 65<cur[1]<110:
                                if 0<len(fed)<200:
                                    co.execute('select max(f_no) from feedback')
                                    mfn=co.fetchone()
                                    if mfn[0]==None:
                                        mfno=1
                                    else:
                                        mfno=mfn[0]+1
                                    ins='insert into feedback values(%s,%s,%s,%s)'
                                    par=(mfno,data[0],fed,'unseen')
                                    co.execute(ins,par)
                                    mo.commit()
                                    z1=0
                        if z2==1:
                            if event.type==pygame.KEYDOWN:
                                key=pygame.key.name(event.key)
                                fed=txt_inp(fed,key)
                        dis.fill((230,180,20))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(1050,65,50,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(50,250,1100,100))
                        txt_dis("BACK",(50,50),20)
                        txt_dis("POST",(1055,75))
                        txt_dis("GIVE FEEDBACK",(100,100),50)
                        txt_dis("Enter feedback (max.length 199)",(55,200),30)
                        for i in range((len(fed)//100)+1):
                            txt_dis(fed[i*100:(i*100)+100],(55,260+(i*35)))
                        pygame.display.update()
                        
                elif 650<cur[0]<1050 and 450<cur[1]<550:
                    #New Complaint Page
                    z1=1
                    z2=0
                    cmt=des=''
                    while z1 and l:
                        event=pygame.event.poll()
                        keys=pygame.key.get_pressed()
                        if event.type==pygame.QUIT:
                            l=0
                        elif event.type==pygame.MOUSEBUTTONDOWN:
                            cur=pygame.mouse.get_pos()
                            if 45<cur[0]<90 and 40<cur[1]<80:
                                z1=0
                            if 50<cur[0]<1050 and 195<cur[1]<240:
                                z2=1
                            if 50<cur[0]<1150 and 300<cur[1]<660:
                                z2=2
                            if 1050<cur[0]<1100 and 65<cur[1]<110:
                                if 0<len(cmt)<100 and 0<len(des)<1000:
                                    co.execute('select max(c_no) from complaint_log')
                                    mcn=co.fetchone()
                                    if mcn[0]==None:
                                        mcno=1
                                    else:
                                        mcno=mcn[0]+1
                                    ins='insert into complaint_log(c_no,logged_by_u_no,comp_type,description) values(%s,%s,%s,%s)'
                                    par=(mcno,data[0],cmt,des)
                                    co.execute(ins,par)
                                    mo.commit()
                                    z1=0
                        if z2==1:
                            if event.type==pygame.KEYDOWN:
                                key=pygame.key.name(event.key)
                                cmt=txt_inp(cmt,key)
                        elif z2==2:
                            if event.type==pygame.KEYDOWN:
                                key=pygame.key.name(event.key)
                                if len(des)<=1000:
                                    des=txt_inp(des,key)
                        dis.fill((205,92,92))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(1050,65,50,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(50,195,1000,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(50,300,1100,360))
                        txt_dis("BACK",(50,50),20)
                        txt_dis("POST",(1055,75))
                        txt_dis("NEW COMPLAINT",(100,90),50)
                        txt_dis("Enter Complaint Type (max.length 99)",(55,155),30)
                        txt_dis(cmt,(55,205))
                        txt_dis("Enter a description of the complaint (max.length 999)",(55,260),30)
                        for i in range((len(des)//100)+1):
                            txt_dis(des[i*100:(i*100)+100],(55,310+(i*35)))
                        pygame.display.update()
                    
            dis.fill((240,10,40))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(1100,600,60,40))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(150,250,400,100))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(650,250,400,100))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(150,450,400,100))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(650,450,400,100))
            txt_dis("HOME PAGE",(100,100),50)
            txt_dis(" See User Profile: "+data[1],(185,290),35)
            txt_dis("See Complaint Log (Recent)",(685,290),35)
            txt_dis("Write New Complaint Here",(685,490),35)
            txt_dis("Give Feedback Here",(185,490),35)
            txt_dis("LOG OUT",(1105,610),20)
            pygame.display.update()
            
    #if it is administrator
    elif u1:
        b=z=1
        uk=''
        ut='1123581321'
        
        #administrator key input page
        while b and l:
            event=pygame.event.poll()
            keys=pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                l=0
            if event.type==pygame.KEYDOWN:
                key=pygame.key.name(event.key)
                uk=txt_inp(uk,key)
            if event.type==pygame.MOUSEBUTTONDOWN:
                cur=pygame.mouse.get_pos()
                if 45<cur[0]<90 and 40<cur[1]<80:
                    b=z=0
                elif 550<cur[0]<650 and 510<cur[1]<555:
                    if uk==ut:
                        b=0
                    else:
                        uk=''
            dis.fill((200,100,30))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(300,315,600,45))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(550,510,100,45))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
            txt_dis("BACK",(50,50),20)
            txt_dis(uk,(305,325))
            txt_dis("Enter Administrator Key",(395,200),50)
            txt_dis("ENTER",(575,520))
            pygame.display.update() 
            
        #administrator home page
        while z and l:
            event=pygame.event.poll()
            keys=pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                l=0
            if event.type==pygame.MOUSEBUTTONDOWN:
                cur=pygame.mouse.get_pos()
                if 1100<cur[0]<1160 and 600<cur[1]<640:
                    z=0
                    
                if 675<cur[0]<1050 and 200<cur[1]<300:
                    #Complaint Log page
                    z1=1
                    cno=''
                    while z1 and l:
                        event=pygame.event.poll()
                        keys=pygame.key.get_pressed()
                        if event.type==pygame.QUIT:
                            l=0
                        if event.type==pygame.KEYDOWN:
                            key=pygame.key.name(event.key)
                            cno=txt_inp(cno,key)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            cur=pygame.mouse.get_pos()
                            if 45<cur[0]<90 and 40<cur[1]<80:
                                z1=0
                                
                            elif 1065<cur[0]<1150 and 120<cur[1]<165:
                                co.execute("select c_no from complaint_log where status='unresolved' order by c_no")
                                lcno=co.fetchmany(10)
                                tcno=(int(cno),)
                                if cno.isdigit():
                                    if tcno in lcno:
                                        #individual complaint viewing page
                                        z2=1
                                        co.execute('select * from complaint_log where c_no=%s',tcno)
                                        datac=co.fetchone()
                                        cmt=datac[2]
                                        des=datac[3]
                                        while z2 and l:
                                            event=pygame.event.poll()
                                            keys=pygame.key.get_pressed()
                                            if event.type==pygame.QUIT:
                                                l=0
                                            if event.type==pygame.MOUSEBUTTONDOWN:
                                                cur=pygame.mouse.get_pos()
                                                if 45<cur[0]<90 and 40<cur[1]<80:
                                                    z2=0
                                                    cno=''
                                                    
                                                if 900<cur[0]<1110 and 65<cur[1]<110:
                                                    #Page to provide solution and update status
                                                    z3=1
                                                    z4=0
                                                    sol=datac[4]
                                                    while z3 and l:
                                                        event=pygame.event.poll()
                                                        keys=pygame.key.get_pressed()
                                                        if event.type==pygame.QUIT:
                                                            l=0
                                                        if event.type==pygame.MOUSEBUTTONDOWN:
                                                            cur=pygame.mouse.get_pos()
                                                            if 45<cur[0]<90 and 40<cur[1]<80:
                                                                z3=0
                                                            elif 50<cur[0]<1100 and 200<cur[1]<560:
                                                                z4=1
                                                            elif 645<cur[0]<745 and 595<cur[1]<640:
                                                                res='resolved'
                                                                z4=2
                                                            elif 795<cur[0]<895 and 595<cur[1]<640:
                                                                res='unresolved'
                                                                z4=2
                                                        if z4==1:
                                                            if event.type==pygame.KEYDOWN:
                                                                key=pygame.key.name(event.key)
                                                                sol=txt_inp(sol,key)
                                                        if z4==2:
                                                            if len(sol)<1000:
                                                                co.execute('update complaint_log set solution=%s where c_no=%s',(sol,cno))
                                                                co.execute("update complaint_log set status=%s where c_no=%s",(res,cno))
                                                                co.execute('select * from complaint_log where c_no=%s',tcno)
                                                                datac=co.fetchone()
                                                                mo.commit()
                                                                z3=0
                                                        dis.fill((95,158,160))
                                                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                                                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(50,200,1100,360))
                                                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(645,595,100,45))
                                                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(795,595,100,45))
                                                        txt_dis("BACK",(50,50),20)
                                                        txt_dis("SOLUTION FOR COMPLAINT "+cno+" (max.length 999)",(100,100),50)
                                                        for i in range((len(sol)//100)+1):
                                                            txt_dis(sol[i*100:(i*100)+100],(55,210+(i*35)))
                                                        txt_dis("STATUS (click one of these buttons to post solution): ",(100,605),30)
                                                        txt_dis("resolved",(650,605))
                                                        txt_dis("unresolved",(800,605))
                                                        pygame.display.update()
                                                        
                                            dis.fill((12,120,44))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(900,65,210,45))
                                            txt_dis("COMPLAINT "+cno,(100,90),50)
                                            txt_dis("BACK",(50,50),20)
                                            txt_dis("click here to give Solution",(905,75))
                                            txt_dis("Complaint Type",(55,155),30)
                                            txt_dis(cmt,(55,205))
                                            txt_dis("Description of the complaint",(55,260),30)
                                            for i in range((len(des)//100)+1):
                                                txt_dis(des[i*100:(i*100)+100],(55,310+(i*35)))
                                            pygame.display.update()
                                            
                                    else:
                                        cno=''
                                else:
                                    cno=''
                        dis.fill((102,0,0))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(700,50,475,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(1065,120,85,45))
                        txt_dis("BACK",(50,50),20)
                        txt_dis("UNRESOLVED COMPLAINT QUEUE",(100,100),50)
                        txt_dis("Enter Complaint Number to view complaint details: "+cno,(705,60))
                        txt_dis("ENTER",(1085,130))
                        txt_dis("Complaint No.    User No.    Complaint Type",(50,200))
                        co.execute("select * from complaint_log where status='unresolved' order by c_no")
                        unl=co.fetchmany(10)
                        x=0
                        for i in unl:
                            txt_dis(str(i[0]).ljust(25,' ')+str(i[1]).ljust(20,' ')+str(i[2]),(50,260+(40*x)))
                            x+=1
                        pygame.display.update()
                        
                if 675<cur[0]<1050 and 350<cur[1]<450:
                    #Feedback Log Page
                    z1=1
                    fno=''
                    while z1 and l:
                        event=pygame.event.poll()
                        keys=pygame.key.get_pressed()
                        if event.type==pygame.QUIT:
                            l=0
                        if event.type==pygame.KEYDOWN:
                            key=pygame.key.name(event.key)
                            fno=txt_inp(fno,key)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            cur=pygame.mouse.get_pos()
                            if 45<cur[0]<90 and 40<cur[1]<80:
                                z1=0
                                
                            elif 1065<cur[0]<1150 and 120<cur[1]<165:
                                co.execute("select f_no from feedback where status='unseen' order by f_no")
                                lfno=co.fetchmany(10)
                                tfno=(int(fno),)
                                if fno.isdigit():
                                    if tfno in lfno:
                                        #individual feedback viewing page
                                        z2=1
                                        co.execute('select * from feedback where f_no=%s',tfno)
                                        dataf=co.fetchone()
                                        fed=dataf[2]
                                        while z2 and l:
                                            event=pygame.event.poll()
                                            keys=pygame.key.get_pressed()
                                            if event.type==pygame.QUIT:
                                                l=0
                                            if event.type==pygame.MOUSEBUTTONDOWN:
                                                cur=pygame.mouse.get_pos()
                                                if (45<cur[0]<90 and 40<cur[1]<80) or (495<cur[0]<565 and 540<cur[1]<595):
                                                    z2=0
                                                    fno=''
                                                elif 695<cur[0]<845 and 540<cur[1]<595:
                                                    co.execute("update feedback set status='seen' where f_no=%s",tfno)
                                                    mo.commit()
                                                    z2=0
                                                    fno=''
                                            dis.fill((255,128,0))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(495,540,70,45))
                                            pygame.draw.rect(dis,(0,0,0),pygame.Rect(695,540,150,45))
                                            txt_dis("BACK",(50,50),20)
                                            txt_dis("FEEDBACK "+str(fno),(100,100),50)
                                            for i in range((len(fed)//100)+1):
                                                txt_dis(fed[i*100:(i*100)+100],(55,260+(i*35)))
                                            txt_dis("STATUS (select either one):",(200,550),30)
                                            txt_dis("unseen",(500,550))
                                            txt_dis("or",(630,550))
                                            txt_dis("seen and noted",(700,550))
                                            pygame.display.update()
                                    else:
                                        fno=''
                                else:
                                    fno=''
                                    
                        dis.fill((102,0,51))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(45,40,45,40))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(700,50,475,45))
                        pygame.draw.rect(dis,(0,0,0),pygame.Rect(1065,120,85,45))
                        txt_dis("BACK",(50,50),20)
                        txt_dis("UNSEEN FEEDBACK QUEUE",(100,100),50)
                        txt_dis("Enter Feedback Number to view feedback details: "+fno,(705,60))
                        txt_dis("ENTER",(1085,130))
                        txt_dis("Feedback No.     User No.        Feedback sneak peak",(50,200))
                        co.execute("select * from feedback where status='unseen' order by f_no")
                        unl=co.fetchmany(10)
                        x=0
                        for i in unl:
                            if len(i[2])>40:
                                sp=i[2][:40]
                            else:
                                sp=i[2]
                            txt_dis(str(i[0]).ljust(25,' ')+str(i[1]).ljust(25,' ')+sp+'...',(50,260+(40*x)))
                            x+=1
                        pygame.display.update()
                        
            dis.fill((240,10,40))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(1100,600,60,40))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(675,200,375,100))
            pygame.draw.rect(dis,(0,0,0),pygame.Rect(675,350,375,100))
            txt_dis("HOME PAGE",(100,100),50)
            co.execute("select count(*) from complaint_log")
            coc=co.fetchone()
            txt_dis("Total Complaints Logged: "+str(coc[0]),(200,250),30)
            co.execute("select count(*) from complaint_log where status='resolved'")
            cor=co.fetchone()
            txt_dis("Complaints resolved: "+str(cor[0]),(200,350),30)
            txt_dis("Complaint Log (Unresolved, Queue)",(690,230),30)
            txt_dis("Feedback Log (Unseen,Queue)",(690,380),30)
            txt_dis("LOG OUT",(1105,610),20)
            pygame.display.update()
            
co.close()
mo.close()
pygame.quit()
