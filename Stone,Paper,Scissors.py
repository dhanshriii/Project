import random

play1=str(input("enter stone ,paper, or sessiors ? :")).lower()
play2=random.randint(1,3)

if play2==1:
    play2="stone"
elif play2==2:
    play2="paper"
elif play2==3:
    play2="sessiors"
print("bot: ",play2)

if play1==play2:
    print("its a tie!!")
elif (play1=="stone" and play2=="sessiors") or (play1=="paper" and play2=="stone") or (play1=="sessiors" and play2=="paper"):
    print("\nYou Win")
else:
    print("\nOohh!!You Loss!!")