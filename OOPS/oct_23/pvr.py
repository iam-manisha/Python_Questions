#create a class called pvr cinema and create 3 generic property and 6 specific property and 3 object and print all the specific and generic properties of all the object

class PVRcinema:
    p_name="PVR"
    p_loc="Whitefield"
    p_tickets={"Premium":2000,"Gold":1000,"Regular":500}

movie_1=PVRcinema()
movie_2=PVRcinema()
movie_3=PVRcinema()

#Assign the Specific Properties
movie_1.name="Avatar"
movie_1.hall=1
movie_1.language="English"
movie_1.duration="2hrs 50min"
movie_1.ticket=3000


print("-"*80)

movie_2.name="Spider Man"
movie_2.hall=2
movie_2.language="Germany"
movie_2.duration="3hrs 50min"
movie_2.ticket=2000

print("-"*80)

movie_3.name="Jawan"
movie_3.hall=3
movie_3.language="Hindi"
movie_3.duration="1hrs 50min"
movie_3.ticket=1000


#Assign the Specific and Generic Properties by using object
print("Theater:",movie_1.p_name)
print("Location:",movie_1.p_loc)
print("Movie Name:",movie_1.name)
print("Movie Duration:",movie_1.duration)

print("Ticket Price:",movie_1.p_tickets)

print("-"*80)