import pandas as pd
import os

def load_data():
    global df
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "players.json")
        df = pd.read_json(file_path)
        print(df.head())
        print(df.columns)
        print("Data loaded successfully.\n")
    except Exception as e:
        print(f"Error loading data: {e}")

# BASIC ANALYSIS
def basic_statistics():
    print("\nBasic Statistics:")
    print(df.describe(include='all'))

def total_players():
    print(f"\nTotal number of players: {len(df)}")

def average_player_price():
    print(f"\nAverage player price: {df['price'].mean():.2f} Cr")

# TEAM ANALYSIS
def count_players_in_team():
    print("\nNumber of players in each team:")
    print(df['team'].value_counts())

def team_with_most_players():
    team = df['team'].value_counts().idxmax()
    count = df['team'].value_counts().max()
    print(f"\nTeam with the most players: {team} ({count} players)")

def total_team_value():
    print("\nTotal team value (sum of player prices):")
    print(df.groupby('team')['price'].sum())

def most_expensive_team():
    team_values = df.groupby('team')['price'].sum()
    team = team_values.idxmax()
    price = team_values.max()
    print(f"\nMost expensive team: {team} ({price:.2f} Cr)")

# ROLE ANALYSIS
def count_players_in_role():
    print("\nNumber of players in each role:")
    print(df['role'].value_counts())

def most_common_role():
    role = df['role'].value_counts().idxmax()
    count = df['role'].value_counts().max()
    print(f"\nMost common role: {role} ({count} players)")

def average_price_per_role():
    print("\nAverage price for each role:")
    print(df.groupby('role')['price'].mean())

def most_expensive_role():
    role_avg = df.groupby('role')['price'].mean()
    role = role_avg.idxmax()
    price = role_avg.max()
    print(f"\nMost expensive role on average: {role} ({price:.2f} Cr)")

# COUNTRY ANALYSIS
def count_players_in_country():
    print("\nNumber of players from each country:")
    print(df['country'].value_counts())

def country_with_most_players():
    country = df['country'].value_counts().idxmax()
    count = df['country'].value_counts().max()
    print(f"\nCountry with the most players: {country} ({count} players)")

def average_price_per_country():
    print("\nAverage price of players from each country:")
    print(df.groupby('country')['price'].mean())

def most_expensive_player_per_country():
    idx = df.groupby('country')['price'].idxmax()
    print("\nMost expensive player from each country:")
    print(df.loc[idx, ['country', 'name', 'price']])

# ADVANCED ANALYSIS
def top_5_expensive_players():
    print("\nTop 5 most expensive players:")
    print(df.sort_values(by='price', ascending=False).head(5)[['name', 'price', 'team', 'role']])

def top_5_expensive_players_by_role():
    print("\nTop 5 most expensive players in each role:")
    for role in df['role'].unique():
        print(f"\nRole: {role}")
        print(df[df['role'] == role].sort_values(by='price', ascending=False).head(5)[['name', 'price', 'team']])

def top_5_expensive_players_by_team():
    print("\nTop 5 most expensive players in each team:")
    for team in df['team'].unique():
        print(f"\nTeam: {team}")
        print(df[df['team'] == team].sort_values(by='price', ascending=False).head(5)[['name', 'price', 'role']])

def top_5_expensive_players_by_country():
    print("\nTop 5 most expensive players from each country:")
    for country in df['country'].unique():
        print(f"\nCountry: {country}")
        print(df[df['country'] == country].sort_values(by='price', ascending=False).head(5)[['name', 'price', 'team', 'role']])

# MENUS
def submenu_1():
    options = {
        '1': load_data,
        '2': basic_statistics,
        '3': total_players,
        '4': average_player_price
    }
    while True:
        print("\nSubmenu 1: Data Loading and Basic Analysis")
        print("1. Load the player data from JSON file")
        print("2. Display basic statistics about the dataset")
        print("3. Find the total number of players")
        print("4. Calculate the average player price")
        print("5. Back to main menu")
        choice = input("Enter your choice: ")
        if choice == '5':
            break
        func = options.get(choice)
        if func:
            func()
        else:
            print("Invalid choice!")

def submenu_2():
    options = {
        '1': count_players_in_team,
        '2': team_with_most_players,
        '3': total_team_value,
        '4': most_expensive_team
    }
    while True:
        print("\nSubmenu 2: Team Analysis")
        print("1. Count the number of players in each team")
        print("2. Find the team with the most players")
        print("3. Calculate the total team value")
        print("4. Identify the most expensive team")
        print("5. Back to main menu")
        choice = input("Enter your choice: ")
        if choice == '5':
            break
        func = options.get(choice)
        if func:
            func()
        else:
            print("Invalid choice!")

def submenu_3():
    options = {
        '1': count_players_in_role,
        '2': most_common_role,
        '3': average_price_per_role,
        '4': most_expensive_role
    }
    while True:
        print("\nSubmenu 3: Player Role Analysis")
        print("1. Count the number of players in each role")
        print("2. Find the most common role")
        print("3. Calculate the average price for each role")
        print("4. Identify the most expensive role")
        print("5. Back to main menu")
        choice = input("Enter your choice: ")
        if choice == '5':
            break
        func = options.get(choice)
        if func:
            func()
        else:
            print("Invalid choice!")

def submenu_4():
    options = {
        '1': count_players_in_country,
        '2': country_with_most_players,
        '3': average_price_per_country,
        '4': most_expensive_player_per_country
    }
    while True:
        print("\nSubmenu 4: Country Analysis")
        print("1. Count the number of players from each country")
        print("2. Find the country with the most players")
        print("3. Calculate the average price of players from each country")
        print("4. Identify the most expensive player from each country")
        print("5. Back to main menu")
        choice = input("Enter your choice: ")
        if choice == '5':
            break
        func = options.get(choice)
        if func:
            func()
        else:
            print("Invalid choice!")

def submenu_5():
    options = {
        '1': top_5_expensive_players,
        '2': top_5_expensive_players_by_role,
        '3': top_5_expensive_players_by_team,
        '4': top_5_expensive_players_by_country
    }
    while True:
        print("\nSubmenu 5: Advanced Analysis")
        print("1. Find the top 5 most expensive players")
        print("2. Find the top 5 most expensive players in each role")
        print("3. Find the top 5 most expensive players in each team")
        print("4. Find the top 5 most expensive players from each country")
        print("5. Back to main menu")
        choice = input("Enter your choice: ")
        if choice == '5':
            break
        func = options.get(choice)
        if func:
            func()
        else:
            print("Invalid choice!")

# Main menu loop
def main_menu():
    while True:
        print("\n=== IPL Player Analytics ===")
        print("1. Data Loading and Basic Analysis")
        print("2. Team Analysis")
        print("3. Player Role Analysis")
        print("4. Country Analysis")
        print("5. Advanced Analysis")
        print("6. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            submenu_1()
        elif choice == '2':
            submenu_2()
        elif choice == '3':
            submenu_3()
        elif choice == '4':
            submenu_4()
        elif choice == '5':
            submenu_5()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    df = pd.DataFrame()  # Initialize empty DataFrame
    main_menu()
