import productos

# Hereda de clase producto
class Stock :
    codigo = []
    productos = []
    stockMinimo = []
    stockMaximo = []
    stockActual = []
    cantidadDeVentas = []
    montoTotalVentas = []

    def __init__(self):
         self.codigo = []
         self.producto = []
         self.stockMinimo = []
         self.stockMaximo = []
         self.stockActual = []
         self.cantidadDeVentas = []
         self.montoTotalVentas  = []
         
    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo



    def get_producto(self):
        return self.producto

    def set_producto(self, producto):
        self.producto = producto



    def get_stockMinimo(self):
        return self.stockMinimo
   
    def set_stockMinimo(self, stockMinimo):
        self.stockMinimo = stockMinimo
     
     
    def get_stockMaximo(self):
        return self.stockMaximo

    def set_stockMaximo(self, stockMaximo):
        self.stockMaximo = stockMaximo

        
    def get_stockActual(self):
        return self.stockActual

    def set_stockActual(self, stockActual):
        self.stockActual = stockActual   
        
   
    def get_CantidadDeVenta(self):
        return self.PrecioDeVenta

    def set_PrecioDeVentas(self, precioDeVenta):
        self.PrecioDeVenta = precioDeVenta    
    

    def get_montoTotalVentas(self):
        return self.montoTotalVentas

    def set_montoTotalVentas(self, montoTotalVentas):
        self.montoTotalVentas = montoTotalVentas   

        
    def calculartotalVentas(self, precioDeVenta):
        return ("El monto total de venta es: ") +  str(self.cantidadDeVentas * precioDeVenta)
        
  
      
                     
    
   