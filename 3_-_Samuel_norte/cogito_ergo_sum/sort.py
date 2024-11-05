import pandas as pd

def sort_csv(input_csv, output_csv):
    # Ler o arquivo CSV
    df = pd.read_csv(input_csv)
    
    # Ordenar os dados pelas colunas X e Y
    df_sorted = df.sort_values(by=['X', 'Y'])
    
    # Salvar o arquivo CSV ordenado
    df_sorted.to_csv(output_csv, index=False)

# Exemplo de uso
sort_csv('output_pixels.csv', 'sorted_output_pixels.csv')