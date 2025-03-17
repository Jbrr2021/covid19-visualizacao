# Visualização de Dados COVID-19 no Brasil

Este projeto foi desenvolvido para a disciplina **Algoritmos e Estrutura de Dados** e tem como objetivo visualizar dados da COVID-19 no Brasil utilizando mapas e gráficos interativos.

## 📌 Funcionalidades
- **Mapa interativo** com dados da COVID-19 por estado.
- **Gráficos interativos** para análise do número de casos e óbitos.
- **Coleta automática** de dados a partir de uma API.

## 🛠 Tecnologias Utilizadas
Este projeto utiliza as seguintes bibliotecas:
- `folium` - Para a criação do mapa interativo.
- `pandas` - Para manipulação e análise dos dados.
- `requests` - Para buscar os dados na API.
- `matplotlib` - Para visualização de gráficos estáticos.
- `plotly` - Para gráficos interativos.
- `webbrowser` - Para abrir os arquivos HTML gerados.

## 🚀 Como Executar o Projeto

1. **Clone o repositório**
   ```sh
   git clone https://github.com/Jbrr2021/covid19-visualizacao.git
   ```

2. **Acesse a pasta do projeto**
   ```sh
   cd covid19-visualizacao
   ```

3. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
   ```

4. **Execute o script**
   ```sh
   python dados_covid.py
   ```

5. **Visualize os resultados**
   - O mapa será salvo como `covid19_mapa_brasil.html` e aberto automaticamente no navegador.
   - Os gráficos serão salvos como `grafico_covid19.html` e também abertos automaticamente.

## 📊 Fonte dos Dados
Os dados são coletados da API pública: [COVID-19 Brazil API](https://covid19-brazil-api.now.sh/)

## 📄 Licença
Este projeto é de código aberto e pode ser utilizado livremente para fins acadêmicos e educacionais.

---
**Desenvolvido por:** Jbrr2021

