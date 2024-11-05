import pandas as pd

def sort_csv_by_r(input_csv, output_csv):
    # Ler o arquivo CSV
    df = pd.read_csv(input_csv)
    
    # Ordenar os dados pela coluna R
    df_sorted = df.sort_values(by=['R'])
    
    # Salvar o arquivo CSV ordenado
    df_sorted.to_csv(output_csv, index=False)

# Exemplo de uso
sort_csv_by_r('sorted_output_pixels.csv', 'sorted_by_r_output_pixels.csv')