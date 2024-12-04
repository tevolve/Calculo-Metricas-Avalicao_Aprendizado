import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Valores arbitrários da matriz de confusão
VP = 50  # Verdadeiros Positivos
VN = 30  # Verdadeiros Negativos
FP = 10  # Falsos Positivos
FN = 20  # Falsos Negativos

# Total de elementos
total = VP + VN + FP + FN

# Fórmulas das métricas
def calcular_acuracia(VP, VN, FP, FN):
    return (VP + VN) / total

def calcular_precisao(VP, FP):
    return VP / (VP + FP)

def calcular_sensibilidade(VP, FN):
    return VP / (VP + FN)

def calcular_especificidade(VN, FP):
    return VN / (VN + FP)

def calcular_f1_score(precisao, recall):
    return 2 * (precisao * recall) / (precisao + recall)

# Cálculo das métricas
acuracia = calcular_acuracia(VP, VN, FP, FN)
precisao = calcular_precisao(VP, FP)
sensibilidade = calcular_sensibilidade(VP, FN)
especificidade = calcular_especificidade(VN, FP)
f1_score = calcular_f1_score(precisao, sensibilidade)

# Exibir resultados
print(f"Acurácia: {acuracia:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"Sensibilidade (Recall): {sensibilidade:.2f}")
print(f"Especificidade: {especificidade:.2f}")
print(f"F1-Score: {f1_score:.2f}")

# Gerar dados para a curva ROC
y_true = np.array([1]*VP + [0]*VN + [1]*FN + [0]*FP)
y_scores = np.random.uniform(0, 1, len(y_true))  # Valores arbitrários para probabilidades

# Calcular valores da curva ROC
fpr, tpr, _ = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)

# Plotar a curva ROC
plt.figure()
plt.plot(fpr, tpr, color='blue', lw=2, label=f'Área sob a curva (AUC) = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--', lw=2)
plt.xlabel('Taxa de Falsos Positivos (FPR)')
plt.ylabel('Taxa de Verdadeiros Positivos (TPR)')
plt.title('Curva ROC')
plt.legend(loc="lower right")
plt.grid()
plt.show()
