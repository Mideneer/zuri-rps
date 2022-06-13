# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 05:39:11 2022

@author: USER
"""

import random
rps_list = ["R", "P", "S"]
correct_output = []

def rock_paper_scissor():
    user_input = input("Type R for rock, P for paper or S for scissors: ")
    player_choice = user_input.upper()
        
    while player_choice not in rps_list:
        print("Invalid input, try again!")
        user_input = input("Type R for rock, P for paper or S for scissors: ")
        player_choice = user_input.upper()
        
    
    if player_choice in rps_list:
        computer_choice = random.choice(rps_list)
        output = [player_choice, computer_choice]
        winner = ["Player", "CPU"]
        
        for each_choice in output:
            if each_choice == "R":
                rock ="Rock"
                #print(rock)
                correct_output.append(rock)
            elif each_choice == "P":
                paper = "Paper"
                #print(paper)
                correct_output.append(paper)
            elif each_choice == "S":
                scissors = "Scissors"
                #print(scissors)
                correct_output.append(scissors)
        

        print(f"Player ({correct_output[0]}): CPU ({correct_output[1]})")
            
        if "Rock" in correct_output and "Paper" in correct_output:
            return(f"{winner[correct_output.index('Paper')]} wins!")
        elif "Rock" in correct_output and "Scissors" in correct_output:
            return(f"{winner[correct_output.index('Rock')]} wins!")
        elif "Paper" in correct_output and "Scissors" in correct_output:
            return(f"{winner[correct_output.index('Scissors')]} wins!")
        else:
            return("It's a tie")
    

print(rock_paper_scissor())
if len(correct_output) == 2:
    while(correct_output[0] == correct_output[1]):
        correct_output = []
        print(rock_paper_scissor())