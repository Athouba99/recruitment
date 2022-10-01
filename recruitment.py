# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
# func 1 only printing for the  to the user  
def get_skills():
     return ["fast", "communication","programming", "listening"] # to save the the array and give its value when needed  
     

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
# func 2 only printing to user  all the skills  

def show_skills(skills):
    print ()
    print("Skills:") # to be show as the sample output 
    for idx,skill in enumerate(skills,start=1):
        print(f"{idx}.{skill}\n")
        #print(get_skills()) # invok func and print it 
     
    
# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
# func 3 
def get_user_skills(skills):
    show_skills(skills) # call func 
    
    new_list = [ input("please choose a skill from above by entering its name: "), input("please choose another skill from above by entering its number: "),]
    return [skills[int(selected) - 1] for selected in new_list]
      

# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
# func 4 
def get_user_cv(skills):
    cv ={"name": input ("what is your name?"),
          "age": int(input("how old are you?")),
          "experience": int(input("how many years of experince do you have?")),
          "skills": get_user_skills(skills),}

    # assigning an output for func 3  

    

# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
# func 5 
def check_acceptance(cv, desired_skill):
    '''
    get_skills() #invok function 
    get_user_cv(skills) #invok function 

    if age >= 40 <= 25:
        if experience > 3:
            if skills in skills_list:
                return True 
    '''
    return (
        25 < cv["age"] < 40 and cv["experience" > 3 and desired_skill in cv["skilld"]] ) 
        

# main func No.6 
def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome


    #1
    print("Welcome to the special recruitment program, please answer the following questions:") # welcome message 
    
    #2
     
    skills = get_skills #assignment
    wanted_skill = 2

    #3
    cv = get_user_cv(skills) 

    #4
    if check_acceptance(cv, skills[wanted_skill]):
            print(f"you have been accepted, {cv['name']}.")
    else:
            print("sorry, you have been rejected.")
        

  

    
if __name__ == "__main__":
    main() 
    
    
    '''
    get_skills()
    show_skills(skills): # len of the func will be used 
      print(skills[skill])
        print("\n \t Skills : \n")
        print("1.{skills[0]}\n")
        print("2.{skills[1]}\n")
        print("3.{skills[2]}\n")
        print("3.{skills[3]}\n") 

    get_user_skills(skills)
    get_user_cv(skills) 
    '''
