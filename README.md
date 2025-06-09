# 🧠 DataSUS Pipeline: Engenharia de Dados, Ciência de Dados e Analytics com AWS & Databricks

Este projeto demonstra uma solução completa e escalável de **Engenharia de Dados**, **Ciência de Dados** e **Análise Preditiva** aplicada à saúde pública utilizando dados do **DataSUS**.

---

## 🎯 Objetivo

Analisar e modelar padrões relacionados à saúde pública brasileira por meio dos registros hospitalares do SIH/SUS (DataSUS), com o uso de tecnologias modernas de Big Data, Machine Learning e Visualização.

---

## 🧱 Arquitetura Utilizada

| Camada                | Descrição                                                                 |
|-----------------------|--------------------------------------------------------------------------|
| **Infraestrutura**    | AWS S3 para armazenamento (camadas Bronze, Silver e Gold)                |
| **Processamento**     | Databricks com PySpark para ETL e EDA                                     |
| **Modelagem**         | Random Forest com Scikit-learn e MLflow para versionamento de modelos     |
| **CI/CD & MLOps**     | GitHub para versionamento, MLflow Tracking, integração com Databricks     |
| **Visualização**      | Notebooks interativos e potencial integração com dashboards em BI         |

---

## 📁 Estrutura de Arquivos

├── a23_ETL_1.ipynb       # Extração e pré-processamento de dados brutos  
├── a23_ETL_2.ipynb       # Limpeza, normalização e feature engineering  
├── a23_EDA_3.ipynb       # Análise exploratória visual e estatística  
├── a23_ml.py             # Treinamento e tracking de modelo Random Forest com MLflow  
├── a23_final.xlsx        # Dataset final com variáveis tratadas  
├── README.md             # Documentação do projeto  

---

## 📦 Stack Tecnológica

- **AWS S3** – Armazenamento de dados (raw, clean, business-ready)
- **Databricks** – Notebooks, clusters Spark, PySpark
- **Scikit-learn** – Modelagem preditiva (Random Forest)
- **MLflow** – Versionamento e logging de modelos
- **Python & R** – Scripts de extração e modelagem
- **Git & GitHub** – Controle de versão, CI/CD
- **Pandas, Matplotlib, Seaborn** – Manipulação e visualização de dados

---

## 🚀 Execução

### 2. Extração e Pré-processamento
Execute os notebooks `a23_ETL_1.ipynb` e `a23_ETL_2.ipynb` para gerar o dataset final.

### 3. Análise Exploratória
Execute `a23_EDA_3.ipynb` para obter insights visuais e estatísticos.

### 4. Modelagem Preditiva
Execute `a23_ml.py` para treinar o modelo, calcular métricas e registrar tudo no MLflow.

---

## 📊 Métricas do Modelo (Random Forest)

- **MSE**: 754.03
- **R²**: 0.8992 (modelo explica 89,9% da variância)

---

## 🛡️ Boas Práticas Adotadas

- Otimização de custos com S3 Intelligent-Tiering
- Cluster auto-terminável no Databricks
- CI/CD com Git e possibilidade de integração com GitHub Actions
- Logging automático com MLflow
- Dados anonimizados conforme LGPD

---

## 👨‍💻 Autor

**Diego de Mattos**  
Data Scientist | Física | MBA USP  
[LinkedIn]([https://www.linkedin.com/](https://www.linkedin.com/in/diego-de-mattos-166417167/)) 

---

## 📄 Licença

Este projeto é livre para uso acadêmico e de demonstração. Para uso comercial, entre em contato com o autor.
"""
