##Representation of how lights direction app would work.

## User login
def intro():
    """Intro function prompts user for student_id and student_name. 
    
    Args: 
        student_id (str): The student's ID number.
        student_name (str): The student's name.
    
    Returns:
        student_name (str): The student's name.
    """
    student_id = input("Welcome to Lights Direction. Please enter your student ID: ")
    student_name = input("Please enter your name: ")
    return student_name
  


## Input directions
def get_input_directions():
    """Prompts and obtains the starting and ending locations
    
    Args: 
        start_point (str): The starting location input by the user.
        end_point (str): The ending location input by the user.
        locations_list (list): A list of valid locations for comparison.
    
    Returns:
        start_point (str): The validated starting location.
        end_point (str): The validated ending location.
     """
    locations_list = ["tbe", "aeb", "seb"]

    start_point = input("Please enter your starting location using the shortened building name : ")
    start_point = start_point.lower() # makes sure that input is lowercased, when compared to the list
    if start_point in locations_list: #checks if location is valid or not
        print("Valid")
    if start_point not in locations_list:
        print("Invalid")
        return None, None

    end_point = input("Please enter your end location using the shortened building name as listed on your class schedule: ")
    end_point = end_point.lower() # makes sure that input is lowercased when compared to the list
    if end_point in locations_list: #checks if location is valid or not
        print("Valid")
    if end_point not in locations_list:
        print("Invalid")
        return None, None
    return start_point, end_point

    

#starts up lights
def start_up_lights(start_point, end_point):
    """Turns on lights for start and end locations
    
    Args:
        start_point (str): The starting location input by the user.
        end_point (str): The ending location input by the user. 
        tbel (bool): Represents the light status for TBE.
        aebl (bool): Represents the light status for AEB.
        sebl (bool): Represents the light status for SEB.
    
    Returns:
        tbel (bool): Updated light status for TBE.
        aebl (bool): Updated light status for AEB.
        sebl (bool): Updated light status for SEB.
    """
    tbel = False
    aebl = False
    sebl = False

    if start_point == "tbe":
        print("Starting lights are on")
        tbel = True #this turns on the light
    if start_point == "aeb":
        print("Starting lights are on")
        aebl = True
    if start_point == "seb":
        print("Starting lights are on")
        sebl = True

    if end_point == "tbe":
        print("Ending lights are on")
        tbel = True #this turns on the light
    if end_point == "aeb":
        print("Ending lights are on")
        aebl = True
    if end_point == "seb":
        print("Ending lights are on")
        sebl = True

    return tbel, aebl, sebl

def j_change():
    print("Change made by Jairo to show in branch")
   



if __name__ == "__main__":
    # Run tests first to ensure logic works
    #test_app()

    # Run actual application flow
    student_name = intro()
    print("Welcome " + student_name)
    start_point, end_point = get_input_directions()

    if start_point is not None and end_point is not None:
        start_up_lights(start_point, end_point)
        # ending message
        print("Please follow the light path. Lights will turn off in 2 minutes")

    j_change()
    

 
 
