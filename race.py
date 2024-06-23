from random import randint

def main():
    # Get names from the user
    names = []
    racers = {}
    for i in range(4):
        name = input(f"Enter name {i + 1}: ")
        names.append(name)
        racers[name] = []
    # Generate commentary
    print("\nRace Commentary:")
    for lap in range(1, 6):  # Assuming a 5-lap race
        print(f"Lap {lap}:")
        for name in names:
            speed = randint(80, 200)  # Random speed between 80 and 120 mph
            racers[name].append(speed)
            if speed < 100:
                status = "slow"
            print(f"{name} is going at {speed} mph!")

    # Calculate average speeds
    average_speeds = {}
    for name in names:
      average_speeds[name] = sum(racers[name]) / len(racers[name])
    # Find the max average speed and the winner
    max_avg_speed = max(average_speeds.values())
    winner = max(average_speeds, key=average_speeds.get)

    # Print average speeds and the winner
    print("\nAverage Speeds:")
    for name, avg_speed in average_speeds.items():
        print(f"{name}'s average speed: {avg_speed:.2f} mph")

    print(f"\nThe winner is {winner} with an average speed of {max_avg_speed:.2f} mph!")


if __name__ == "__main__":
    main()
