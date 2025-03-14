import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    """
    Carrega o dataset.
    """
    df = pd.read_csv(file_path)
    return df

def plot_univariate_analysis(df, target_col):
    """
    Análise univariada: Distribuição de cada variável em relação à classe.
    """
    for col in df.columns:
        if col != target_col:  # Ignorar a variável-alvo
            plt.figure(figsize=(8, 6))
            sns.countplot(x=col, hue=target_col, data=df, palette="Set2")
            plt.title(f"Distribuição de {col} por Classe")
            plt.xlabel(col)
            plt.ylabel("Contagem")
            plt.legend(title="Classe", loc="upper right")
            plt.show()

def plot_bivariate_analysis(df, target_col):
    """
    Análise bivariada: Correlação entre as variáveis e a classe.
    """
    # Codificar todas as colunas categóricas
    df_encoded = df.copy()
    label_encoders = {}

    for col in df_encoded.columns:
        if df_encoded[col].dtype == 'object':  # Aplicar apenas a colunas categóricas
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col])
            label_encoders[col] = le  # Armazenar o encoder para referência futura

    # Calcular a matriz de correlação
    correlation_matrix = df_encoded.corr()

    # Plotar a matriz de correlação
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Matriz de Correlação")
    plt.show()

def identify_patterns(df, target_col):
    """
    Identifica padrões dos cogumelos comestíveis (e) e venenosos (p).
    """
    # Separar os dados em comestíveis e venenosos
    edible = df[df[target_col] == 'e']
    poisonous = df[df[target_col] == 'p']

    # Analisar as características mais comuns em cada classe
    for col in df.columns:
        if col != target_col:
            print(f"\nAnálise da variável: {col}")
            print(f"Comestíveis (e):")
            print(edible[col].value_counts(normalize=True).head())
            print(f"Venenosos (p):")
            print(poisonous[col].value_counts(normalize=True).head())

def main():
    file_path = "data/mushrooms.csv"  # Caminho para o dataset
    target_col = "class"  # Variável-alvo

    # Carregar os dados
    df = load_data(file_path)

    # Análise univariada
    plot_univariate_analysis(df, target_col)

    # Análise bivariada
    plot_bivariate_analysis(df, target_col)

    # Identificar padrões
    identify_patterns(df, target_col)

if __name__ == "__main__":
    main()