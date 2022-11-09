class Empleado :
    codigoEmpleado = ""
    nombre = ""
    usuario = ""
    contraseña = ""
    rol = ""
    puedeEditar = ""

    def __init__(self, codigoEmpleado, nombre, usuario, contraseña, rol):
         self.codigoEmpleado = codigoEmpleado
         self.nombre = nombre
         self.usuario = usuario
         self.contraseña = contraseña
         self.rol = rol
         self.puedeEditar = puedeEditar
         

    def get_codigoEmpleado(self):
        return self.codigoEmpleado

    def set_codigoEmpleado(self, codigoEmpleado):
        self.codigoEmpleado = codigoEmpleado



    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre



    def get_usuario(self):
        return self.usuario
   
    def set_usuario(self, usuario):
        self.usuario = usuario
     
     
    def get_contraseña(self):
        return self.contraseña

    def set_contraseña(self, contraseña):
        self.contraseña = contraseña

        
    def get_rol(self):
        return self.rol

    def set_rol(self, rol):
        self.rol= rol  
      
    def get_puedeEditar(self):
        return self.puedeEditar

    def set_puedeEditar(self, puedeEditar):
        self.puedeEditar = puedeEditar  
      
                         
    
    