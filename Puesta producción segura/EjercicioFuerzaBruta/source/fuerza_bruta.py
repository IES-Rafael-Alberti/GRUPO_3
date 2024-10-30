import hashlib

def calcula_sha(passwd: str):
    m = hashlib.sha256(passwd.encode())
    return m.hexdigest()


def comparacion_sha(passwd:str,archivo:str):
    
    with open(archivo, 'r') as f:
        lines = f.readlines()
        for line_number, line in enumerate(lines, start=1):
            contenido = line.strip()
            contenido_sha = calcula_sha(contenido)            
            
            if contenido_sha == passwd:
                
                return True, contenido
    
    return False,None

if __name__=='__main__':
   
   contraseña_sha= input('Dime un sha para buscar su contraseña en el diccionario\n')
   comparacion, contenido=  comparacion_sha(contraseña_sha,'contrasenas_test.txt')
   if comparacion:
    print(f'La contraseña para el sha {contraseña_sha} es {contenido} ')
   else:
      print(f'La contraseña para el sha {contraseña_sha} no se ha encontrado en la lista')


