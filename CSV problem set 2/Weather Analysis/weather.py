import pandas as pd  
import matplotlib.pyplot as plt 

def get_hottest_day(df):
    hottest = df.loc[df['Temperature'].idxmax()]
    print(f"Hottest day: {hottest['Date'].date()} with {hottest['Temperature']}°C")

def get_average_temperature(df):
    avg_temp = df['Temperature'].mean()
    print(f"Average temperature: {avg_temp:.2f}°C")

def count_rainy_days(df):
    rainy_days = df[df['Rainfall'] > 0].shape[0]
    print(f"Total rainy days: {rainy_days}")

def plot_temperature_trend(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='blue')
    plt.title("Temperature Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    df = pd.read_csv("weather.csv", parse_dates=['Date'])

    while True:
        print("""
        🌦️ Weather Data Analysis
        1. Show Hottest Day
        2. Show Average Temperature
        3. Count Rainy Days
        4. Show Temperature Trend Plot
        5. Exit
        """)
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            get_hottest_day(df)
        elif choice == '2':
            get_average_temperature(df)
        elif choice == '3':
            count_rainy_days(df)
        elif choice == '4':
            plot_temperature_trend(df)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
