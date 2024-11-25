print( '                            LIBRARY MANAGEMENT SYSTEM')
print('')


def happy():
        print('press 1 for 101.no book informatins')
        print('press 2 for 102.no book informatins')
        print('press 3 for 103.no book informatins')
        print('press 4 for 104.no book informatins')
        print('press 5 for 105.no book informatins')
happy()

def kaa():
        print('')
        g=int(input('''DO YOU WONT TO CONTINUE
       prees 1 for continue
       prees 2 for exit :enter number :'''))
        print('')
        if(g==1):
            happy()
        print('')
        if(g==1):
            joy()
        else:
             print('thanks for visit  LIBRARY SYSTEM')  
print('')



def joy():
         z=int(input('enter number :'))   
         if(z==1):
              print('')
              print('''101 Book Name: Atomic Habits
                 Author Name: James Clear
                 Title : Atomic Habits
                 Price : $17.99
                 Launch Date: October 16, 2018''')
              kaa()
         elif(z==2):
             print('')
             print('''102 Book Name: The Midnight Library
                 Author Name: Matt Haig
                 Title : The Midnight Library
                 Price : $13.99
                 Launch Date: September 29, 2020''')
             kaa()
         elif(z==3):
             print('')
             print('''103 Book Name: The Alchemist
                 Author Name: Paulo Coelho
                 Title : The Alchemist
                 Price : $16.99
                 Launch Date: April 15, 1988''')
             kaa()
         elif(z==4):
             print('')
             print('''104 Book Name: Becoming
                 Author Name: Michelle Obama
                 Title : Becoming
                 Price : $18.99
                 Launch Date: November 13, 2018''')
             kaa()
         elif(z==5):
             print('')
             print('''105 Book Name: The Four Agreements
                 Author Name: Don Miguel Ruiz
                 Title : The Four Agreements
                 Price : $12.99
                 Launch Date: November 7, 1997''')
             kaa()
        
joy() 