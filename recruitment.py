# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
# func 1 only printing for the  to the user  
def get_skills():
    skills_list = ["fast", "communication","programming", "listening"] # list 
    return skills_list # to save the the array and give its value when needed

  

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
# func 2 only printing to user  all the skills  

def show_skills(skills):
    for skill in skills:
        print(get_skills()) # invok func and print it 
    return show_skills  
    show_skills(skills_list)
 

# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
# func 3 
def get_user_skills(skills):
    get_skills() # invok func 
    print(skills_list)
    new_list = []
    number = int(input("select only 2 skills: "))
    print ("you picked ", number) 
    new_list.update(number)
    return get_user_skills   
    ''' using loop to make sure only are picked'''


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
# func 4 
def get_user_cv(skills):
    cv = {} # empty dict
    user_cv = True
    while (user_cv): # loop for the user to add name,age,&cv 
        name = input("\nWhat is your name?\t")
        age = input ("\nHow old are you?\t")
        experience = input("\nHow many years of experiencedo you have?\t")

    # storing the inputs to dict 
    user_cv[name] = "name"
    user_cv[age] = "age" 
    user_cv[experience] = "experience"


    ''' 
    d = dict (input ("enter a value: ").split() for _ in range(n) )
    print (d) 
    '''



# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
# func 5 
def check_acceptance(cv, desired_skill):
    ...

# main func 
def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
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
     

if __name__ == "__main__":
    main()
    '''
