import folium
import pandas as pd
import requests
import webbrowser
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# URL da API com dados do Brasil
url = "https://covid19-brazil-api.now.sh/api/report/v1"
response = requests.get(url)
data = response.json()

# Criar um dataframe com os dados necessários
df = pd.DataFrame(data['data'])[['state', 'cases', 'deaths', 'uf']]

# Coordenadas aproximadas dos estados brasileiros
coords = {
    "AC": [-9.02, -70.81], "AL": [-9.57, -36.78], "AM": [-3.47, -65.10], "AP": [1.41, -51.77],
    "BA": [-12.96, -38.51], "CE": [-3.73, -38.53], "DF": [-15.78, -47.93], "ES": [-20.32, -40.34],
    "GO": [-16.68, -49.25], "MA": [-2.53, -44.30], "MT": [-12.64, -55.42], "MS": [-20.51, -54.54],
    "MG": [-19.92, -43.94], "PA": [-1.46, -48.50], "PB": [-7.12, -34.87], "PR": [-25.43, -49.27],
    "PE": [-8.05, -34.88], "PI": [-5.09, -42.80], "RJ": [-22.91, -43.20], "RN": [-5.81, -35.21],
    "RO": [-8.76, -63.90], "RS": [-30.03, -51.23], "RR": [2.82, -60.67], "SC": [-27.59, -48.55],
    "SE": [-10.91, -37.07], "SP": [-23.55, -46.63], "TO": [-10.25, -48.32]
}

# Criar um mapa centralizado no Brasil
m = folium.Map(location=[-14.23, -51.92], zoom_start=4)

# Adicionar os estados ao mapa
for index, row in df.iterrows():
    estado = row['uf']  # Sigla do estado
    if estado in coords:
        lat, lon = coords[estado]
        folium.CircleMarker(
            location=[lat, lon],
            radius=row['cases'] / 50000,  # Ajuste do tamanho
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.6,
            popup=f"{row['state']}: {row['cases']} casos, {row['deaths']} mortes"
        ).add_to(m)

# Salvar o mapa
mapa_arquivo = "covid19_mapa_brasil.html"
m.save(mapa_arquivo)

# Criar um gráfico de barras com os dados
fig = make_subplots(rows=1, cols=2, subplot_titles=["Casos por Estado", "Mortes por Estado"])

fig.add_trace(go.Bar(x=df['state'], y=df['cases']), row=1, col=1)
fig.add_trace(go.Bar(x=df['state'], y=df['deaths']), row=1, col=2)

fig.update_layout(height=600, width=1000)
fig.write_html("grafico_covid19.html")

# Abrir o mapa e o gráfico automaticamente no navegador
webbrowser.open(mapa_arquivo)
webbrowser.open("grafico_covid19.html")

print("Mapa e gráficos do Brasil atualizados com sucesso!")
