import math # Importa todo o módulo math
from math import sqrt # Importa apenas a função sqrt do módulo math
from math import factorial # Importa apenas a função factorial do módulo math
from math import pow # Importa apenas a função pow do módulo math
from math import ceil # Importa apenas a função ceil do módulo math
from math import floor # Importa apenas a função floor do módulo math
from math import trunc # Importa apenas a função trunc do módulo math
from math import hypot # Importa apenas a função hypot do módulo math
import math
num=int(input('Digite um número: '))
raiz=math.sqrt(num) 
print ('A raiz quadrada de {} é {}'.format(num, math.ceil(raiz))) # math.ceil arredonda para cima
print ('A raiz quadrada de {} é {}'.format(num, math.floor(raiz))) # math.floor arredonda para baixo
print ('='*30)
from math import sqrt, floor
num=int(input('Digite um número: '))
raiz=sqrt(num) # Não é necessário usar math.sqrt
print ('A raiz quadrada de {} é {}'.format(num, floor(raiz))) # Não é necessário usar math.floor
print ('='*30) 

