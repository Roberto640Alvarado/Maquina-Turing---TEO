def load_tm_definition(file_path):
    tm_definition = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                #Parse each transition rule from the file
                parts = line.split(',')
                current_state = parts[0].strip()
                read_symbol = parts[1].strip()
                new_state = parts[2].strip()
                write_symbol = parts[3].strip()
                direction = parts[4].strip()
                tm_definition[(current_state, read_symbol)] = (new_state, write_symbol, direction)
    
    return tm_definition


def simulate_TM(tape, tm_definition, initial_state='q0', blank_symbol='B', accept_states=['accept']):
    tape = list(tape) + [blank_symbol] * 10  #Add blank spaces to the tape
    state = initial_state
    head_position = 0
    
    print("Inicio de la simulación de la Máquina de Turing")
    print(f"Estado inicial: {state}, Cinta: {''.join(tape)}")

    while state not in accept_states:
        symbol = tape[head_position]
        if (state, symbol) in tm_definition:
            new_state, write_symbol, move_direction = tm_definition[(state, symbol)]
            print(f"Transición: ({state}, {symbol}) -> ({new_state}, {write_symbol}, {move_direction})")
            
            #Write the new symbol on the tape
            tape[head_position] = write_symbol
            #Update the state
            state = new_state
            #Move the head
            head_position += 1 if move_direction == 'R' else -1
            
            #Ensure the head does not go out of bounds (extend tape with blanks if necessary)
            if head_position < 0:
                tape.insert(0, blank_symbol)
                head_position = 0
            elif head_position >= len(tape):
                tape.append(blank_symbol)
        else:
            print(f"No hay transición para el estado {state} y símbolo {symbol}. Terminando.")
            break
    
    print(f"Estado final: {state}")
    print(f"Cinta final: {''.join(tape)}")


#Usar el archivo "test.txt" como archivo por defecto para la definición de la TM
tm_file_path = 'test.txt'

try:
    tm_definition = load_tm_definition(tm_file_path)
except FileNotFoundError:
    print(f"Error: El archivo '{tm_file_path}' no fue encontrado.")
    exit()

#Pidiendo solo la cadena de entrada al usuario
input_string = input("Introduce la cadena de entrada para la Máquina de Turing: ")

#Ejecutar la simulación con la cadena de entrada proporcionada
simulate_TM(input_string, tm_definition)
