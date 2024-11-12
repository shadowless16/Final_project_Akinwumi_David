print("Hello welcome to temperatue Logger")

# Temprature list
temp_logger = {}

# temp_function
def log_temp():
    day = input("Enter the Day: ")
    temp = int(input("Enter the temperature: "))
    temp_logger[day] = {"Temp": temp}
    print(f"The temperature for {day} is {temp}°")

# fucntion to calcualte average temp
def calculate_average():
    if len(temp_logger) == 0:
        print("No temperatures has logged.")
        return
    
    average_temp = sum(temp["Temp"] for temp in temp_logger.values()) / len(temp_logger)
    print(f"\nAverage temperature: {average_temp:.2f}°")


# while loop to continuously run the code
while True:
    
    option = int(input("Hello would you like to log the temperature for today. \n1. Yes \n2. Calaculate Average \n3. Quit Program \nSelect on of the options: "))

    match option:
        case 1:
            log_temp()
        case 2:
            calculate_average()
        case 3:
            print("Exiting Program")
            break
        case _:
            print("Enter one of the follow option above")
