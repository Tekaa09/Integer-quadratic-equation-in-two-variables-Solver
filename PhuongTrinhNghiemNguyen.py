import tkinter as tk
from os import path
import math
import sys
def delta(a,b,c):
  D=b**2-4*a*c
  return D

def x1(a,b,c):
  result = (-a-b**(1/2))/(2*c)
  return result 
# Hàm tính nghiệm đầu của phương trình 

def x2(a,b,c):
  result = (-a+b**(1/2))/(2*c)
  return result 
# Hàm tính nghiệm sau của phương trình 

def calculate():
  global last_a  
  last_a = a_entry.get() 
  global last_b  
  last_b = b_entry.get()
  global last_c 
  last_c = c_entry.get()
  global last_d  
  last_d = d_entry.get()
  global last_e 
  last_e = e_entry.get()
  global last_f  
  last_f = f_entry.get()
  if a_entry.get() == "":
    a_entry.insert(0,"0") 
    a=int(a_entry.get()) 
  elif a_entry.get() > "3000" or a_entry.get() < "-3000":
    kq.config(text="Vui lòng nhập a trong khoảng [-3000, 3000]")
    return
  else:
    a=int(a_entry.get()) 
  if b_entry.get() == "":
    b_entry.insert(0,"0") 
    b=int(b_entry.get()) 
  elif b_entry.get() > "3000" or b_entry.get() < "-3000":
    kq.config(text="Vui lòng nhập b trong khoảng [-3000, 3000]")
    return
  else:
    b=int(b_entry.get()) 
  if c_entry.get() == "":
    c_entry.insert(0,"0") 
    c=int(c_entry.get()) 
  elif c_entry.get() > "3000" or c_entry.get() < "-3000":
    kq.config(text="Vui lòng nhập c trong khoảng [-3000, 3000]")
    return
  else:
    c=int(c_entry.get()) 
  if d_entry.get() == "":
    d_entry.insert(0,"0") 
    d=int(d_entry.get()) 
  elif d_entry.get() > "3000" or d_entry.get() < "-3000":
    kq.config(text="Vui lòng nhập d trong khoảng [-3000, 3000]")
    return
  else:
    d=int(d_entry.get()) 
  if e_entry.get() == "":
    e_entry.insert(0,"0") 
    e=int(e_entry.get()) 
  elif e_entry.get() > "3000" or e_entry.get() < "-3000":
    kq.config(text="Vui lòng nhập e trong khoảng [-3000, 3000]")
    return
  else:
    e=int(e_entry.get()) 
  if f_entry.get() == "":
    f_entry.insert(0,"0") 
    f=int(f_entry.get()) 
  elif f_entry.get() > "3000" or f_entry.get() < "-3000":
    kq.config(text="Vui lòng nhập f trong khoảng [-3000, 3000]")
    return
  else:
    f=int(f_entry.get()) 
  nx = []
  ny = []
  if (e==0):
    nghiem=0
    #print ("Nghiem cua phuong trinh la (x,y)=")
    if (f%d==0):
     #print (0,f/d)
     nx.append(0)
     ny.append(f/d)
     nghiem=nghiem +1
    n0= -d/c
    #print (n0)
    sodu=a*n0**2+b*n0+f
    #print (sodu)
    for dem in range (1,100):
     if ((sodu*dem)%1==0):
       mau=dem
       break
    sodu=sodu*mau
    sodu=int(sodu)
    #print (sodu)
    if sodu>0 :
     sodu2=sodu 
     sdl=(sodu2-d)/c
     sdb=(-sodu2-d)/c
     dem=sdl
     #print (dem,sdl,sdb)
     while (sdb>=dem>=sdl):
       if ((c*dem+d)==0):
         dem=dem+1
       else:
         if (sodu2%(c*dem+d)==0): 
           y=-(a*dem**2+b*dem+f)/(dem*c+d)
           #print ("(",dem,",",y,")") 
           nx.append(dem)
           ny.append(y)
           nghiem=nghiem+1
         dem=dem+1   
    else  :
     sodu2=sodu 
     sdl=(-sodu2-d)/c
     sdb=(sodu2-d)/c
     dem=sdb
     #print (dem,sdl,sdb)
     while (sdl>=dem>=sdb):
       if ((c*dem+d)==0):
         dem=dem+1
       else:
         if (sodu2%(c*dem+d)==0): 
           y=-(a*dem**2+b*dem+f)/(dem*c+d)
           #print ("(",dem,",",y,")")
           nx.append(dem)
           ny.append(y)
           nghiem= nghiem+1 
         dem=dem+1
    if nghiem==0:
      kq.config(text="Nghiệm của phương trình là (x,y):{Ø}")
    else:
      kq.config(text="Nghiệm của phương trình là (x,y):{"+";".join(f"({x}, {y})" for x, y in zip(nx, ny))+"}")
  elif (b==0) and (c==0) and (d==0): 
   if (f>0 ) and (a>0) and (e>0):
     #print ("Phương trình vô nghiệm")
     kq.config(text="Nghiệm của phương trình là (x,y):{Ø}")
   elif (e<0 and f<0) or(a<0 and f>0):
     ng=0
     x=2
     y=1
     if (a<0) and (f>0):
       a=-a
       f=-f
       e=-e
     while (ng==0) and (a*x**2+e*y**2<=-f*10) and ( a*x**2+e*y**2 >=f*10)  :
       while (a*x**2+e*y**2<=-f*10) and (ng==0)and ( a*x**2+e*y**2 >=f*10):
         if (a*x**2+e*y**2+f==0):
           nx.append(x)
           nx.append(x) 
           nx.append(-x)
           nx.append(-x) 
           ny.append(-y)
           ny.append(y) 
           ny.append(-y)
           ny.append(y)
           ng=ng+1 
         else:
           x=x+1
       x=2
       y=y+1 
     if ng==0:
       kq.config(text="Nghiệm của phương trình là (x,y):{Ø}")
     else:
       kq.config(text="Nghiệm của phương trình là (x,y):{"+";".join(f"({x}, {y})" for x, y in zip(nx, ny))+"}")
   elif (a<0 and f<0) or (f>0 and e<0):
     ng=0
     y=2
     x=1
     if (f>0) and (e<0):
       a=-a
       f=-f
       e=-e
     while (ng==0) and (a*x**2+e*y**2<=-f*10) and ( a*x**2+e*y**2 >=f*10) :
       while (a*x**2+e*y**2<=-f*10) and (ng==0) and ( a*x**2+e*y**2 >=f*10):
         if (a*x**2+e*y**2+f==0):
           nx.append(x)
           nx.append(x) 
           nx.append(-x)
           nx.append(-x) 
           ny.append(-y)
           ny.append(y) 
           ny.append(-y)
           ny.append(y)
           ng=ng+1 
         else:
           y=y+1
       y=2
       x=x+1
     if ng==0:
       kq.config(text="Nghiệm của phương trình là (x,y):{Ø}")
     else:
       kq.config(text="Nghiệm của phương trình là (x,y):{"+";".join(f"({x}, {y})" for x, y in zip(nx, ny))+"}")
   else:
      dem=0
      #print ("Phương trình có nghiệm là (x,y)=")
      for x in range (int(((-f)**(1/2))*-1), int(((-f)**(1/2))+1)) :
       for y in range (int(((-f)**(1/2))*-1), int(((-f)**(1/2))+1)) :
        if a*x**2 + e*y**2 == -f:  
         #print("(",x,",",y,")")
         nx.append(x)
         ny.append(y)
         dem=dem+1
      if dem==0:
       kq.config(text="Nghiệm của phương trình là (x,y):{Ø}")
      else:
       kq.config(text="Nghiệm của phương trình là (x,y):{"+";".join(f"({x}, {y})" for x, y in zip(nx, ny))+"}")
  else:
    nghiem=0
    a2=c*c-4*e*a
    b2=2*(b*c-2*d*a)
    c2=b**2-4*a*f
    D=delta(a2,b2,c2)
    if D<0 :
      kq.config(text="Nghiệm của phương trình là (x,y):{Ø}")
    elif D == 0:
     y1=-b2/2*a2
     y2=-b2/2*a2
    else :
        if (a2>0):
         y1=x1(b2,D,a2)
         y2=x2(b2,D,a2)
        else:
         y1=x2(b2,D,a2)
         y2=x1(b2,D,a2)
    dem=math.ceil(y1)
      #print (y1,y2,a2,b2,c2)
    #print ("Nghiem nguyen cua phuong trinh la (y,x)=")
    if (y2==round(y2,0)): 
      y2=y2+1
    while (dem<math.ceil(y2)):
      b3=b+c*dem
      c3=d*dem+e*(dem**2)+f
      D2=delta(a,b3,c3)
      #print (D2,b3,c3,dem) 
      if c3 == 0:
        y4=-b3/a
        if (y4==round(y4,0)) and (y4!=-0.0):
          #print ("(",dem,";",y4,")")
          nx.append(y4)
          ny.append(dem)
        #print ("(",dem,";",0,")")
        nx.append(0)
        ny.append(dem)
        nghiem=nghiem+1
      elif D2 == 0 :
        y=-b3/2*a
        if y==round(y,0):
          #print ("(",dem,";",y,")")
          nx.append(y)
          ny.append(dem)
          nghiem=nghiem+1
      else  :
        y3=(x2(b3,D2,a)).real
        y4=(x1(b3,D2,a)).real
        if y3==round(y3,0):
          #print ("(",dem,";",y3,")")
          nx.append(y3)
          ny.append(dem)
          nghiem=nghiem+1
        if (y4==round(y4,0)):
          #print ("(",dem,";",y4,")")  
          nx.append(y4)
          ny.append(dem)
          nghiem=nghiem+1    
      dem = dem +1
    if nghiem==0:
      kq.config(text="Nghiệm của phương trình là (x,y):{Ø}")
    else:
      kq.config(text="Nghiệm của phương trình là (x,y):{"+";".join(f"({x}, {y})" for x, y in zip(nx, ny))+"}")

def quickclear():
  a_entry.delete(0, tk.END)
  b_entry.delete(0, tk.END)
  c_entry.delete(0, tk.END)
  d_entry.delete(0, tk.END)
  e_entry.delete(0, tk.END)
  f_entry.delete(0, tk.END)

def undo_quickclear():
  a_entry.delete(0, tk.END) 
  b_entry.delete(0, tk.END)
  c_entry.delete(0, tk.END)
  d_entry.delete(0, tk.END)
  e_entry.delete(0, tk.END)
  f_entry.delete(0, tk.END)
  a_entry.insert(0,last_a) 
  b_entry.insert(0,last_b) 
  c_entry.insert(0,last_c) 
  d_entry.insert(0,last_d) 
  e_entry.insert(0,last_e) 
  f_entry.insert(0,last_f) 
# Tạo cửa sổ chính

def next_widget(event):
  current_widget = event.widget
  index = widgets.index(current_widget)
  next_index = (index + 1) % len(widgets)   
  widgets[next_index].focus()
  return "break"

def prev_widget(event):
  current_widget = event.widget
  index = widgets.index(current_widget)
  prev_index = (index - 1) % len(widgets)  
  widgets[prev_index].focus()
  return "break"

root = tk.Tk()
Image_path1 = "Images/bg3.png"
Image_path2 = "Images/icon2.png"
root.title("Phương Trình Nghiệm Nguyên")
root.geometry("950x500")
myimage = tk.PhotoImage(file=Image_path1)
bg=tk.Label(root,image=myimage)
bg.place(x=1, y=1)
try:
 icon = tk.PhotoImage(file=Image_path2) 
 root.iconphoto(False, icon)
except Exception as e:
 print(f"Lỗi khi tải icon: {e}")

tk.Label(root, text="ax^2+bx+cxy+dy+ey^2+f",font=("Times New Roman",30,"bold"),bg="white").place(x=270 , y = 40)

tk.Label(root, text="a",font=("Times New Roman",17,"bold"),bg="white").place(x=5 , y = 125)
a_entry = tk.Entry(root,font=("Times New Roman",11,"bold"),width=12, bg="#FFFFCC")
a_entry.place(x=20 , y = 130)
tk.Label(root, text="b",font=("Times New Roman",17,"bold"),bg="white").place(x=170 , y = 125)
b_entry = tk.Entry(root,font=("Times New Roman",11,"bold"),width=12, bg="#FFFFCC")
b_entry.place(x=185, y = 130)
tk.Label(root, text="c",font=("Times New Roman",17,"bold"),bg="white").place(x=335 , y = 125)
c_entry = tk.Entry(root,font=("Times New Roman",11,"bold"),width=12, bg="#FFFFCC")
c_entry.place(x=350, y = 130)
tk.Label(root, text="d",font=("Times New Roman",17,"bold"),bg="white").place(x=500 , y = 125)
d_entry = tk.Entry(root,font=("Times New Roman",11,"bold"),width=12, bg="#FFFFCC")
d_entry.place(x=515, y = 130)
tk.Label(root, text="e",font=("Times New Roman",17,"bold"),bg="white").place(x=665 , y = 125)
e_entry = tk.Entry(root,font=("Times New Roman",11,"bold"),width=12, bg="#FFFFCC")
e_entry.place(x=680, y = 130)
tk.Label(root, text="f",font=("Times New Roman",17,"bold"),bg="white").place(x=830 , y = 125)
f_entry = tk.Entry(root,font=("Times New Roman",11,"bold"),width=12, bg="#FFFFCC")
f_entry.place(x=845, y = 130)

calculate_button = tk.Button(root, text="Giải",font=("Times New Roman",16,"bold"), command=calculate, bg="#FFFFCC",width=10)
calculate_button.place(x=420 , y = 275)

qc_button = tk.Button(root, text="Xóa Nhanh",font=("Times New Roman",12,"bold"), command=quickclear, bg="#FFFFCC")
qc_button.place(x=840 , y = 180)

undo_qc_button = tk.Button(root, text="Phục Hồi",font=("Times New Roman",12,"bold"), command=undo_quickclear, bg="#FFFFCC",width=9)
undo_qc_button.place(x=840 , y = 230)

kq = tk.Label(root, text="", fg="black",font=("Times New Roman",17,"bold"),bg="white")
kq.place(x=10 , y=400)

root.bind('<Return>', lambda event: calculate_button.invoke())

widgets = [a_entry,b_entry,c_entry,d_entry,e_entry,f_entry] 

for widget in widgets:
    widget.bind("<Right>", next_widget)  
    widget.bind("<Left>", prev_widget)   

root.mainloop()

