### Integrantes:
- Albeño Ortega, Douglas Alejandro (00166120)
- Alfaro Ángel, Katerin Alexandra (00240620)
- Alvarado Beltrán, Roberto Carlos (00176620)
- Arucha Aguilar, Edwin Enrique (00175420)
- Iglesias Moreno, David Alejandro (00047920)

# Simulador de Máquina de Turing

Este programa en Python simula una Máquina de Turing que utiliza una única cinta y recibe una **cadena de entrada** proporcionada por el usuario. El archivo `test.txt` (predefinido) contiene la **definición de la Máquina de Turing** (los estados y transiciones).

## Explicación del código

### Funciones principales:

1. **`load_tm_definition(file_path)`**:
   - Esta función lee un archivo de texto con la definición de la Máquina de Turing y carga las transiciones en un diccionario.
   - El archivo contiene líneas con las reglas de transición en el siguiente formato:  
     ```
     Estado actual, Símbolo leído, Nuevo estado, Símbolo a escribir, Dirección
     ```
   - Cada línea se procesa y se añade al diccionario `tm_definition`.

2. **`simulate_TM(tape, tm_definition, initial_state='q0', blank_symbol='B', accept_states=['accept'])`**:
   - Esta función simula la ejecución de la Máquina de Turing sobre la cinta.
   - Recibe la cinta (cadena de entrada), la definición de la máquina (las transiciones), y otros parámetros como el estado inicial, el símbolo en blanco (`B`), y los estados de aceptación.
   - El proceso consiste en:
     1. Leer el símbolo actual de la cinta bajo el cabezal.
     2. Aplicar la regla de transición correspondiente.
     3. Escribir un nuevo símbolo en la cinta.
     4. Mover el cabezal a la izquierda o derecha.
     5. Repetir el proceso hasta alcanzar un estado de aceptación o no encontrar más transiciones.

3. **Archivo de entrada por defecto**:
   - El archivo `test.txt` contiene la definición de la Máquina de Turing y es cargado automáticamente. El formato esperado es el siguiente:
     ```
     q0, a, q1, b, R
     q1, b, q2, c, L
     q2, a, accept, a, R
     q2, b, accept, b, R
     q0, B, accept, B, R
     ```

4. **Interacción con el usuario**:
   - Se pide al usuario que ingrese una **cadena de entrada** para ser procesada por la Máquina de Turing:
     ```python
     input_string = input("Introduce la cadena de entrada para la Máquina de Turing: ")
     ```
