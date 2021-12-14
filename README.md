# CombinarPDFs

## Necessidade
Combinar arquivos '.pdf' pode ser feito a partir de uma solução proprietária (com custos de licensiamento) ou a partir de sites que fornecem esse serviço.
Ao enviar arquivos (fazer o upload) em um site, não existe garantia de que esses arquivos não ficam salvos em servidores de terceiros e isso pode ferir algumas normas (principalmente no que diz respeito à LGPD).

## Objetivo: Funcionalidade para combinar arquivos PDFs em um único arquivo do mesmo formato

### Requisitos:
- Escolher mais de um arquivo no formato '.pdf' em um diretório
- Escolher o diretório que o arquivo combinado será salvo.
- Escolher o nome do arquivo combinado
- O arquivo combinado deve ser salvo no formato '.pdf'
- Ter uma interface gráfica simples

### Solução Aplicada
- Toda a lógica foi desenvolvida na linguagem Python
- Para a interface foi utilizada a biblioteca [Tkinter](https://docs.python.org/3/library/tk.html)
- Para manipulação de arquivos PDF foi utilizada a biblioteca [PyPDF2](https://pythonhosted.org/PyPDF2/)

### Ganhos
- Execução local (sem riscos de processar arquivos em servidores terceiros)
- Solução sem custos para utilização.

### Recomendações
- Para gerar um arquivo executável, sugiro utlização da biblioteca [Pyinstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html)
