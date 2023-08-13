from create_dataframe import create_behavioural_dataframe


df = create_behavioural_dataframe(root_path='C:/Users/mariu/OneDrive/Desktop/behavioural_analysis/data/result_files')

df.to_excel('C:/Users/mariu/OneDrive/Desktop/behavioural_analysis/new_behavioural_dataframe.xlsx')
