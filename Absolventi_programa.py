print("1.Absolventi")
print("2.klase")


while(True):
    
    choice = input("izvelies lomu(1/2): ")

    
    if choice in ('1', '2'):
        
        if choice == '1':
            
            print('1.jā')
            print('1.Nē')
            
            choice2 = input("Atnāksi?(1/2): ")
            
            if choice2 in ('1', '2'):
                    
                if choice2 == '1':
                    print('Labi! gaidām tevi DD/MM/YYYY')

                elif choice2 == '2':
                    print('Jauku dienu')
        elif choice == '2':
            input('Kas jums ir nepiecišams pasākuma organizēšanai?: ')
            print('Viss pēc iespējas prasitais jums tiks izots Gaidiet!')

    exit()
