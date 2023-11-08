# Demonstração de Threads em Python

Este é um exemplo simples de como usar threads em Python para executar tarefas concorrentes. Neste exemplo, criei duas threads que imprimem sequências de números e letras alternadamente com um atraso de 1 segundo entre cada impressão. Isso demonstra como as threads podem ser usadas para realizar várias tarefas simultaneamente em um programa Python.

## Como Executar o Código

Certifique-se de ter o Python instalado em seu sistema. Além disso, não é necessário instalar nenhuma biblioteca adicional, pois usamos a biblioteca padrão `threading`.

1. Baixe o arquivo `thread_example.py` deste repositório.

2. Abra um terminal e navegue até o diretório onde o arquivo `thread_example.py` está localizado.

3. Execute o código Python usando o seguinte comando:

   ```
   python main.py
   ```

4. Você verá as sequências de números e letras sendo impressas alternadamente com um atraso de 1 segundo entre cada impressão.

5. Após a execução, você verá a mensagem "Programa concluído!" indicando que o programa principal foi concluído.

## Explicação do Código

- Importamos a biblioteca `threading` para trabalhar com threads e a biblioteca `time` para adicionar pausas.

- Definimos duas funções, `print_numbers` e `print_letters`, que imprimem sequências de números e letras, respectivamente, com uma pausa de 1 segundo entre cada impressão.

- Criamos duas threads, `thread1` e `thread2`, que executam as funções `print_numbers` e `print_letters`, respectivamente.

- Iniciamos as threads usando `thread1.start()` e `thread2.start()`.

- Usamos `thread1.join()` e `thread2.join()` para aguardar até que ambas as threads tenham concluído sua execução.

- Finalmente, imprimimos "Programa concluído!" para indicar que o programa principal foi concluído.

## Conclusão

Este exemplo demonstra como as threads podem ser usadas para realizar tarefas concorrentes em Python, melhorando a eficiência e a capacidade de resposta de um programa. Isso é útil em situações em que você deseja realizar várias tarefas ao mesmo tempo, como em aplicativos que precisam lidar com entrada de usuário e atualizações de interface gráfica simultaneamente.