# Guía de Configuración del Entorno (Setup)

Esta guía explica, paso a paso y desde cero, cómo dejar configurada una máquina Windows para poder generar y ejecutar los analizadores léxicos/sintácticos (Lexer/Parser) generados con **ANTLR 4.13.2** en **Python**, usados en los ejercicios de este repositorio.

Está pensada para alguien que **no tiene Python, Java, ni ANTLR instalados**.

---

## 1. Requisitos previos a instalar

### 1.1 Instalar Python

1. Ir a [https://www.python.org/downloads/](https://www.python.org/downloads/) y descargar la última versión estable de Python para Windows (3.10 o superior recomendado).
2. Ejecutar el instalador.
3. **Importante:** en la primera pantalla del instalador, marcar la casilla **"Add python.exe to PATH"** antes de darle a "Install Now".
4. Verificar la instalación abriendo PowerShell y corriendo:
   ```powershell
   py --version
   ```
   Debe mostrar algo como `Python 3.14.x`.

### 1.2 Instalar Java (JDK)

ANTLR está escrito en Java, por lo que se necesita un JDK para poder generar el Lexer/Parser.

1. Descargar un JDK (por ejemplo Eclipse Temurin) desde [https://adoptium.net/](https://adoptium.net/).
2. Instalarlo con las opciones por defecto (asegurarse de que la opción de agregar Java al PATH esté marcada).
3. Verificar la instalación:
   ```powershell
   java -version
   ```
   Debe mostrar la versión instalada.

### 1.3 Descargar el archivo `.jar` de ANTLR

1. Descargar `antlr-4.13.2-complete.jar` desde [https://www.antlr.org/download.html](https://www.antlr.org/download.html).
2. Guardarlo en una ubicación fija y permanente del proyecto, por ejemplo:
   ```
   Automatas2\Homeworks\antlr-4.13.2-complete.jar
   ```
   (No lo borres ni lo muevas después de configurarlo, ya que la ruta se usará en cada sesión de terminal).

---

## 2. Clonar o ubicar el repositorio

```powershell
cd C:\Users\<tu_usuario>\Desktop\University\BackupFromOldDrive\Automatas2
```

Ajustar la ruta según donde tengas o clones el proyecto.

---

## 3. Configurar la variable de entorno `CLASSPATH` (apunta al `.jar` de ANTLR)

Esta variable le dice a Java dónde está el `.jar` de ANTLR. Se define **una vez por sesión de PowerShell** (no persiste si cierras la terminal, a menos que la configures como variable de entorno permanente del sistema).

```powershell
$env:CLASSPATH = "C:\Users\<tu_usuario>\Desktop\University\BackupFromOldDrive\Automatas2\Homeworks\antlr-4.13.2-complete.jar"
```

Verificar que quedó bien seteada:

```powershell
echo $env:CLASSPATH
```

> **Opcional (recomendado a futuro):** para no tener que definir esta variable cada vez que abres una terminal nueva, se puede configurar como variable de entorno permanente de Windows desde *Panel de Control > Sistema > Configuración avanzada del sistema > Variables de entorno*.

---

## 4. Crear el entorno virtual de Python (una sola vez, en la carpeta raíz de los ejercicios)

En vez de crear un entorno virtual por cada ejercicio, se crea **uno solo en la carpeta raíz** (por ejemplo `EjercicioTarea`), y ese mismo entorno sirve para todas las subcarpetas de ejercicios dentro de ella.

```powershell
cd C:\Users\<tu_usuario>\Desktop\University\BackupFromOldDrive\Automatas2\Competencia2\EjercicioTarea
py -m venv venv
```

Esto crea una carpeta `venv\` dentro de `EjercicioTarea`.

---

## 5. Activar el entorno virtual

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución de scripts con un error de política de ejecución, correr **una sola vez** (con PowerShell como administrador si es necesario):

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Y volver a intentar activar el entorno. Sabrás que está activo porque la línea de comandos mostrará `(venv)` al inicio.

---

## 6. Instalar las dependencias de Python

Con el entorno virtual activado:

```powershell
pip install antlr4-python3-runtime
```

### 6.1 Generar `requirements.txt`

Esto guarda la lista exacta de dependencias instaladas para que cualquier persona (o el propio proyecto en otra máquina) pueda replicar el entorno:

```powershell
pip freeze > requirements.txt
```

### 6.2 Instalar dependencias desde `requirements.txt` (en una máquina nueva)

Si el entorno virtual ya existe y solo falta instalar las dependencias (por ejemplo, alguien más clona el repositorio):

```powershell
pip install -r requirements.txt
```

---

## 7. Estructura esperada del proyecto

```
EjercicioTarea/
│
├── venv/                  <- entorno virtual único para todos los ejercicios
├── requirements.txt       <- dependencias del proyecto
│
├── Ejercicio1/
│   ├── Ejercicio1.g4      <- gramática ANTLR
│   ├── Ejercicio1Lexer.py <- generado por ANTLR
│   ├── Ejercicio1Parser.py<- generado por ANTLR
│   ├── Prueba.py          <- script de prueba
│   └── .antlr/            <- archivos auxiliares generados
│
├── Ejercicio2/
│   └── ...
│
└── EjercicioN/
    └── ...
```

---

## 8. Generar el Lexer/Parser a partir de un archivo `.g4`

Este paso usa **Java**, no Python, por lo que **no depende del entorno virtual**. Solo depende de que `CLASSPATH` esté correctamente configurado (paso 3) y de estar parado en la carpeta del ejercicio correspondiente.

```powershell
cd Ejercicio1
java -jar $env:CLASSPATH -Dlanguage=Python3 -no-listener .\Ejercicio1.g4
```

Esto genera, entre otros, los archivos:
- `Ejercicio1Lexer.py`
- `Ejercicio1Parser.py`
- `Ejercicio1.tokens`
- `Ejercicio1.interp`

> Repetir este comando cada vez que se modifique el archivo `.g4` correspondiente, para regenerar el Lexer/Parser actualizado.

---

## 9. Ejecutar el script de prueba en Python

Con el entorno virtual **activado** (paso 5) y parado en la carpeta del ejercicio:

```powershell
py .\Prueba.py
```

Ejemplo de script de prueba (`Prueba.py`) que tokeniza una entrada ingresada por consola:

```python
from antlr4 import *

from Ejercicio1Lexer import Ejercicio1Lexer

lexer = Ejercicio1Lexer(InputStream(input("? ")))

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    print("Texto ", token.text)
    print("Tipo ", token.type)
    print("Linea ", token.line)
    print("columna ", token.column)
    nombre_token = lexer.symbolicNames[token.type]

    print("Nombre del token: ", nombre_token)

    print("---------------------")
```

---

## 10. Flujo resumido (para uso diario, una vez configurado todo)

```powershell
# 1. Ir a la raíz del proyecto
cd C:\Users\<tu_usuario>\Desktop\University\BackupFromOldDrive\Automatas2\Competencia2\EjercicioTarea

# 2. Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# 3. (Si no persiste entre sesiones) Configurar CLASSPATH
$env:CLASSPATH = "C:\Users\<tu_usuario>\Desktop\University\BackupFromOldDrive\Automatas2\Homeworks\antlr-4.13.2-complete.jar"

# 4. Entrar a la carpeta del ejercicio deseado
cd Ejercicio1

# 5. Generar Lexer/Parser (solo si se modificó el .g4)
java -jar $env:CLASSPATH -Dlanguage=Python3 -no-listener .\Ejercicio1.g4

# 6. Correr el script de prueba
py .\Prueba.py

# 7. Para trabajar en otro ejercicio, regresar a la raíz y repetir desde el paso 4
cd ..

# 8. Al terminar, desactivar el entorno virtual
deactivate
```

---

## 11. Comandos útiles de referencia

| Acción | Comando |
|---|---|
| Ver carpeta actual | `pwd` |
| Subir un nivel de carpeta | `cd ..` |
| Subir dos niveles | `cd ..\..` |
| Listar archivos de la carpeta actual | `dir` o `ls` |
| Ver si CLASSPATH está seteado | `echo $env:CLASSPATH` |
| Activar entorno virtual | `.\venv\Scripts\Activate.ps1` |
| Desactivar entorno virtual | `deactivate` |
| Instalar dependencias desde archivo | `pip install -r requirements.txt` |
| Congelar dependencias actuales | `pip freeze > requirements.txt` |

---

## 12. Notas importantes

- El `venv` **no se activa automáticamente**; hay que activarlo en cada nueva sesión de terminal antes de correr scripts de Python.
- El comando de `java` para generar el Lexer/Parser **no requiere el venv activado**, solo requiere Java instalado y `CLASSPATH` configurado.
- El nombre de la gramática dentro del archivo `.g4` (`grammar NombreX;`) **debe coincidir exactamente** con el nombre del archivo (`NombreX.g4`), o ANTLR arrojará un error.
- No subir la carpeta `venv/` al repositorio (agregarla a `.gitignore`); en su lugar, cualquier persona que clone el proyecto debe crear su propio entorno virtual y luego instalar las dependencias desde `requirements.txt`.
