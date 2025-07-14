import pandas as pd

def main():
    df = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

    print("=== Dataset Summary ===")
    print(df.info())

    print("\n=== First Few Records ===")
    print(df.head())

    print("\n=== Missing Values Check ===")
    print(df.isnull().sum())

    print("\n=== Summary Statistics ===")
    print(df.describe(include='all'))

if __name__ == "__main__":
    main()
