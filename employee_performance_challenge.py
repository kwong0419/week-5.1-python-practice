import pandas as pd
import matplotlib.pyplot as plt


def load_employee_data():
    df = pd.read_csv('./data/employee_performance.csv')
    return df

df = load_employee_data()
df.columns = df.columns.str.lower()

def explore_employee_dataframe(df):
    print(df.head(10))
    print(df.info())
    print(df.describe())

def select_and_filter_employee_data(df):
     print(df[['employee_id', 'first_name', 'last_name', 'performance_score']])
     print(df[df['performance_score'] > 80])
     print(df.loc[0:10, ['employee_id', 'first_name', 'last_name', 'performance_score']])

def employee_data_operations(df):
    df['salary_per_year'] = (df['salary'] / df['years_at_company'])
    return df.sort_values(by='performance_score', ascending=False)

def top_3_employees_with_highest_salary(df):
    print(df[['first_name', 'last_name','email','salary']].sort_values('salary', ascending=False).head(3))

def avg_performance_score_by_department(df):
    return df.groupby('department_id')['performance_score'].mean()

def plot_salary_vs_years_of_experience(df):
    plt.scatter(df['years_at_company'], df['salary'])
    plt.title('Employee Salaries vs. years_at_company')
    plt.xlabel('years_at_company')
    plt.ylabel('salary')
    plt.show()


def main():
    # Uncomment each function one by one to see the output

    # print(f'2. Explore the DataFrame \n')
    # print(explore_employee_dataframe(df))

    # print(f'3. Select and filter employee data \n')
    # print(select_and_filter_employee_data(df))

    # print(f'4. Perform Data Operations: \n')
    # print(employee_data_operations(df))

    # print(f'5. Find the top 3 employees with the highest salary \n')
    # print(top_3_employees_with_highest_salary(df))

    # print(f'6. Average performance score by department \n')
    # print(avg_performance_score_by_department(df))

    # print(f'7. Plot a scatter plot of salary vs years_at_company \n')
    # print(plot_salary_vs_years_of_experience(df))

if __name__ == "__main__":
    main()
