"""
Módulo para carregar e gerenciar dados do projeto IACOV-BR.

Este módulo fornece funções para carregar as bases de dados bruta e tratada,
com tratamento de erros e validação de dados.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Optional


class DataLoader:
    """Classe para carregar e gerenciar dados do projeto."""
    
    def __init__(self, data_dir: str = "data/raw"):
        """
        Inicializa o carregador de dados.
        
        Args:
            data_dir: Diretório contendo os arquivos de dados
        """
        self.data_dir = Path(data_dir)
        self.raw_file = self.data_dir / "F_Tabela_Geral_Final(1).xlsx"
        self.treated_file = self.data_dir / "df_iacov_treated.xlsx"
    
    def load_raw_data(self) -> pd.DataFrame:
        """
        Carrega a base de dados bruta (não tratada).
        
        Returns:
            DataFrame com os dados brutos
            
        Raises:
            FileNotFoundError: Se o arquivo não existir
        """
        if not self.raw_file.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.raw_file}")
        
        print(f"Carregando dados brutos de {self.raw_file}...")
        df = pd.read_excel(self.raw_file)
        print(f"✓ Dados brutos carregados: {df.shape[0]} linhas × {df.shape[1]} colunas")
        
        return df
    
    def load_treated_data(self) -> pd.DataFrame:
        """
        Carrega a base de dados tratada.
        
        Returns:
            DataFrame com os dados tratados
            
        Raises:
            FileNotFoundError: Se o arquivo não existir
        """
        if not self.treated_file.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.treated_file}")
        
        print(f"Carregando dados tratados de {self.treated_file}...")
        df = pd.read_excel(self.treated_file)
        print(f"✓ Dados tratados carregados: {df.shape[0]} linhas × {df.shape[1]} colunas")
        
        return df
    
    def load_both(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Carrega ambas as bases de dados.
        
        Returns:
            Tupla contendo (dados_brutos, dados_tratados)
        """
        raw = self.load_raw_data()
        treated = self.load_treated_data()
        return raw, treated
    
    @staticmethod
    def get_data_info(df: pd.DataFrame, name: str = "Dataset") -> None:
        """
        Imprime informações detalhadas sobre o DataFrame.
        
        Args:
            df: DataFrame a analisar
            name: Nome do dataset para exibição
        """
        print(f"\n{'='*80}")
        print(f"INFORMAÇÕES: {name}")
        print(f"{'='*80}")
        print(f"\nDimensões: {df.shape[0]:,} linhas × {df.shape[1]} colunas")
        
        print(f"\nTipos de dados:")
        print(df.dtypes)
        
        print(f"\nValores faltantes (top 10):")
        missing = df.isnull().sum().sort_values(ascending=False)
        missing_pct = (missing / len(df) * 100).round(2)
        missing_info = pd.DataFrame({
            'Coluna': missing.index,
            'Faltantes': missing.values,
            'Percentual': missing_pct.values
        })
        print(missing_info.head(10).to_string(index=False))
        
        print(f"\nEstatísticas descritivas (variáveis numéricas):")
        print(df.describe().round(2))
    
    @staticmethod
    def get_missing_summary(df: pd.DataFrame) -> pd.DataFrame:
        """
        Retorna um resumo dos valores faltantes.
        
        Args:
            df: DataFrame a analisar
            
        Returns:
            DataFrame com resumo de valores faltantes
        """
        missing = df.isnull().sum()
        missing_pct = (missing / len(df) * 100).round(2)
        
        summary = pd.DataFrame({
            'Coluna': df.columns,
            'Faltantes': missing.values,
            'Percentual': missing_pct.values,
            'Tipo': df.dtypes.values
        }).sort_values('Faltantes', ascending=False)
        
        return summary[summary['Faltantes'] > 0]


# Exemplo de uso
if __name__ == "__main__":
    loader = DataLoader()
    
    # Carregar dados
    raw_data = loader.load_raw_data()
    treated_data = loader.load_treated_data()
    
    # Exibir informações
    loader.get_data_info(raw_data, "Base Bruta")
    loader.get_data_info(treated_data, "Base Tratada")
    
    # Resumo de valores faltantes
    print("\n" + "="*80)
    print("RESUMO DE VALORES FALTANTES - BASE BRUTA")
    print("="*80)
    print(loader.get_missing_summary(raw_data))
    
    print("\n" + "="*80)
    print("RESUMO DE VALORES FALTANTES - BASE TRATADA")
    print("="*80)
    print(loader.get_missing_summary(treated_data))
