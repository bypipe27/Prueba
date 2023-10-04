

# CRUD 
# My Project pharmacy

clients = 'Luis, Mateo' # variable of type string 

def _print_welcome():
    print("WELCOME TO PHARMACY UNIVALLE TULUÁ")
    print("*" * 60)
    print("What would you like to do today:")
    print("[C]reate client o user")
    print("[R]ead client o user")
    print("[U]pdate client o user")
    print("[D]elete client o user")


def create_clients(client_name):
    global clients
    if client_name not in clients:#  if name not in clients , name add 
        clients += client_name
    else:
        print('Client already is in the Client\'s list')


def read_clients(client_name):
    global clients 
    
    if client_name in clients:  
        print(f'The name is,{client_name}')
    else:
        print('The name not is')


def update_client(client_name, update_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ",",update_name+",")
    else:
        print("Error103")


def delete_client(client_name):
    global clients
    if client_name in clients:
        # Remove the client name and the trailing comma
        clients = clients.replace(client_name + ",", "")
        print(f"Deleted {client_name}")
    else:
        print("Client not found") 




# Devuelve la lista clintes al día.
def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients
    clients +=', '



def _get_client_name():
    return input("Enter your name:")  

if __name__ == '__main__':

    _print_welcome()
    option = input("Type your activity: ").upper()

    if option == 'C':
        client_name = _get_client_name() # se obtiene el nombre del cliente
        _add_comma()
        create_clients(client_name) # se envía el nombre del cliente para crear
        list_clients()   

    elif option == 'R':
        client_name = _get_client_name() # se obtiene el nombre del cliente
        read_clients(client_name) # se envía el nombre del cliente para comparar en lista
        list_clients()  

    elif option == 'U':
        client_name = _get_client_name()
        update_name = input("What is the update client name")
        update_client(client_name, update_name) 
        list_clients() 
        
    elif option == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    else:
        print("Invalid command")