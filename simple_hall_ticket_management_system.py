class Star_Cinema :
    hall_list=[]

    def entry_hall(self,hall_id):
        self.hall_list.append(hall_id)


class Hall(Star_Cinema):
    seats={"101" : [[0,0,0],[0,0,0],[0,0,0]], "102" : [[0,0,0],[0,0,0],[0,0,0]] , "103" : [[0,0,0],[0,0,0],[0,0,0]]}
    show_list=[]

    def hall_info (self,rows,cols,hall_no):
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.entry_hall(hall_no)

    def entry_show(self,id,movie_name,time):
        self.id=id
        self.movie_name=movie_name
        self.time=time
        info=(id,movie_name,time)
        self.show_list.append(info)
        print("Show Id = ",id)
        print("Remaining Seats = ",self.seats[self.id])
        
    def view_available_seat(id):
        id= str(id)
        for key in Hall.seats.keys():
            if (key==id):
                print(Hall.seats[key])

    def view_show_list():
            print ("Running Show Name and ID : JAWAN (ID->101) ,PK (ID->102) , SPIDER MAN (ID->103)")


    def book_seat (id,seat_touple_list):        
            for element in seat_touple_list:
                lst=element
                row=lst[0]
                col=lst[1]
                
                for key in Hall.seats.keys():
                    if (key==id):
                        key_detect=Hall.seats[id]
                        if (key_detect[row-1][col-1]==1):
                             print("Sorry The Seat is Already Booked")
                             print ("Run The Code Again . View Available Seat and Book The Seat Which is Marked 0")
                             exit()
                        key_detect[row-1][col-1]=1
            for i in range (len(key_detect)):
                print(key_detect[i])
            print(seat_touple_list , "Seat is booked for you")
    
    def view_available_seat(id):
        id=str(id)
        print(Hall.seats[id])
                   
         
         
         


class id_selection:
    def is_id_valid_or_not(id):
        if (id==101):
              print ("Movie : JAWAN is Selected")
        elif (id==102):
              print("Movie : PK is Seleted")
        elif (id==103):
            print("Movie : SPIDER MAN is Selected")
        else:
            print ("Run the Code again and Choose a Valid ID")
            exit()

   




print ("WELCOME TO STAR CINEPLEX !!!! ")
print("1. View All Show Today")
print("2. View Available Seat")
print("3. Book Seat")
print("4. Exit")
user_choice=int(input("Enter Your Choice : "))
while (1):
    if ((user_choice)==1):
        Hall.view_show_list()
        
    elif (user_choice==2):
        id=int(input("Enter a Show ID : "))
        id_selection.is_id_valid_or_not(id)
        print ("Available Seats-")
        print ("0 Marked Seats ar available but 1 are Not") 
        Hall.view_available_seat(id)
        

    elif (user_choice==3):
            id=int(input("Enter a Show ID : "))
            seat_touple_list=[]
            total_seat=int(input("Enter How Many Seats Do You Want to Book : "))
            for i in range (total_seat):
                row=int(input("Enter The Row you Want to Book (It Must Be From 1 to 5): "))
                if (row<1 and row>5):
                    print("Enter Valid Row")
                    exit()
                col=int(input("Enter The Column you Want to Book (It Must Be From 1 to 3): "))
                if (col<1 and row>3):
                    print("Enter Valid Column")
                    exit()
                seat_touple=(row,col)
                seat_touple_list.append(seat_touple)
            Hall.book_seat(str(id),seat_touple_list)

    elif (user_choice==4):
        print("Thanks For Visit Our Apps")
        exit()
    else:
        print("Enter a Valid Option")
    
    
    print("1. View All Show Today")
    print("2. View Available Seat")
    print("3. Book Seat")
    print("4. Exit")
    user_choice=int(input("Enter Your Choice : "))
    

     


