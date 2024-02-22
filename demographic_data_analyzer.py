import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=0)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    # What is the average age of men?
    average_age_men = float("%0.1f" % df.loc[df['sex'] == 'Male', 'age'].mean())

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = float("%0.1f" % (len(df[df['education']=='Bachelors'])/len(df['education'])*100))

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    rich = df['salary'] == '>50K'
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df['education'].isin(advanced)
    lower_education = ~df['education'].isin(advanced)
    df_high_edu_sal = pd.DataFrame({'col1': higher_education, 'col2': rich})
    df_low_edu_sal = pd.DataFrame({'col1': lower_education, 'col2': rich})

    # percentage with salary >50K
    higher_education_rich = float("%0.1f" % (df_high_edu_sal.all(axis='columns').sum()/higher_education.sum() * 100))
    lower_education_rich = float("%0.1f" % (df_low_edu_sal.all(axis='columns').sum()/lower_education.sum() * 100))

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = int(df['hours-per-week'].min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df['hours-per-week'] == min_work_hours
    df_rich_minwork = pd.DataFrame({'col1': min_workers, 'col2': rich})

    rich_percentage = float("%0.1f" % (df_rich_minwork.all(axis='columns').sum()/min_workers.sum() * 100))

    # What country has the highest percentage of people that earn >50K?
    df_country_rich = pd.DataFrame({'col1': df['native-country'], 'col2': rich})
    df_country = pd.DataFrame({'col1': df['native-country'], 'col2': True})
    df_country_rich_count = df_country_rich.groupby('col1')['col2'].sum()
    df_country_count = df_country.groupby('col1')['col2'].sum()

    highest_earning_country = (df_country_rich_count/df_country_count)[(df_country_rich_count/df_country_count) == max(df_country_rich_count/df_country_count)].index[0]
    highest_earning_country_percentage = float("%0.1f" % (max(df_country_rich_count/df_country_count) * 100))
    # Identify the most popular occupation for those who earn >50K in India.


    top_IN_occupation = (df[df['native-country']=='India'].value_counts('occupation'))[df[df['native-country']=='India'].value_counts('occupation') == max(df[df['native-country']=='India'].value_counts('occupation'))].index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
