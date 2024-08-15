"""
import random

class Railway:
    def __init__(self):
        # Initialize the train data as an instance attribute
        self.trains = {
            'train1': {
                'trainNo': 34795,
                'from': 'Multan',
                'to': 'Lahore',
                'fare': 950,
                'time': '12:30pm'
            },
            'train2': {
                'trainNo': 34605,
                'from': 'Multan',
                'to': 'Rawalpindi',
                'fare': 1370,
                'time': '1:30pm'
            },
            'train3': {
                'trainNo': 12395,
                'from': 'Multan',
                'to': 'Karachi',
                'fare': 1550,
                'time': '2:30pm'
            },
            'train4': {
                'trainNo': 90012,
                'from': 'Lahore',
                'to': 'Rawalpindi',
                'fare': 630,
                'time': '3:30am'
            },
            'train5': {
                'trainNo': 34005,
                'from': 'BWP',
                'to': 'D.G Khan',
                'fare': 630,
                'time': '7:45pm'
            }
        }

    def schedule(self):
        print("Available Trains:")
        for key, value in self.trains.items():
            print(f"\n{key}:")
            print(f"  Train No: {value['trainNo']}")
            print(f"  From: {value['from']}")
            print(f"  To: {value['to']}")
            print(f"  Fare: Rs/-{value['fare']}")
            print(f"  Time: {value['time']}")
           
    def booking(self, choice):
        # Calculate the index from the user's choice
        train_key = f'train{choice}'
        seat = random.randint(2, 35)
        
        # Check if the chosen train exists
        if train_key in self.trains:
            train = self.trains[train_key]
            print(f"You have booked seat no: {seat} on Train No: {train['trainNo']}, from {train['from']} to {train['to']}")
            print("please make sure your presence at Railway Station 30 minuts before Departure.\nHave a safe journey!")
        else:
            print("Invalid choice. Please choose a valid train number.")

def main():
    t = Railway()  # Create an instance of the Railway class b 
    t.schedule()  # Display the schedule
    choice = int(input("Please enter your choice from 1 to 5: "))
    t.booking(choice)  # Book the chosen train

if __name__=="__main__":
   main()"""


n=int(input("enter a number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
