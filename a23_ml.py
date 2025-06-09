import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

# 1. Carregar dados
file_path = 'a23_final.xlsx'
data = pd.read_excel(file_path)

# 2. Selecionar colunas relevantes
columns_to_use = [
    'Idade do paciente em anos', 'Sexo do paciente', 'Raça/Cor do paciente',
    'Código do Procedimento Ambulatorial', 'Tipo de Estabelecimento',
    'Quantidade Produzida (APRESENTADA)', 'Valor Aprovado do procedimento'
]
df = data[columns_to_use].dropna()

# 3. Codificar variáveis categóricas
label_encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# 4. Separar variáveis independentes e alvo
X = df.drop(columns=['Valor Aprovado do procedimento'])
y = df['Valor Aprovado do procedimento']

# 5. Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Treinar o modelo
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# 7. Avaliar o modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 8. Inferir assinatura para MLflow
input_example = X_train.iloc[:5]
signature = infer_signature(X_train, model.predict(X_train))

# 9. Iniciar experimento MLflow e logar
mlflow.set_experiment("Valor_Aprovado_Prediction")

with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForestRegressor")
    mlflow.log_param("test_size", 0.2)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2_score", r2)

    mlflow.sklearn.log_model(
        model, 
        "model", 
        input_example=input_example, 
        signature=signature
    )

    run_id = mlflow.active_run().info.run_id
