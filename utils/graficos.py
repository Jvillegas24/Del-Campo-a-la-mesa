import io
import base64
import matplotlib.pyplot as plt

# Datos para los gráficos
labels = ['Café', 'Frutas', 'Hortalizas', 'Leguminosas']
produccion = [1000, 2500, 1200, 800]
colores = ['#4bc0c0', '#9966ff', '#ff9f40', '#36a2eb']

# Función para crear el gráfico de barras como imagen en base64
def crear_grafico_barras():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(labels, produccion, color=colores, edgecolor='black')
    ax.set_title('Producción en toneladas (2021)', fontsize=16)
    ax.set_xlabel('Cultivos', fontsize=12)
    ax.set_ylabel('Producción (toneladas)', fontsize=12)
    ax.set_ylim(0, max(produccion) + 500)
    # Guardar el gráfico en un objeto BytesIO
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode('utf-8')

# Función para crear el gráfico circular como imagen en base64
def crear_grafico_pastel():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(produccion, labels=labels, colors=colores, autopct='%1.1f%%', startangle=90)
    ax.set_title('Distribución de Producción de Cultivos (2021)', fontsize=16)
    # Guardar el gráfico en un objeto BytesIO
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode('utf-8')
