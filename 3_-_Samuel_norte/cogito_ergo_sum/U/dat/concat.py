import os

def merge_dat_files(input_folder, output_file):
    # Listar todos os arquivos .dat na pasta
    dat_files = [f for f in os.listdir(input_folder) if f.endswith('.dat')]
    
    with open(output_file, 'w') as outfile:
        for dat_file in dat_files:
            file_path = os.path.join(input_folder, dat_file)
            with open(file_path, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')  # Adicionar uma quebra de linha entre os arquivos

# Exemplo de uso
merge_dat_files('./', 'merged_output.dat')