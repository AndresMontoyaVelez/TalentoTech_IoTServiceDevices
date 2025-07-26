from os import name
import re
import sqlite3
import pandas as pd
import mysql.connector
import numpy as np

bd = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'projectciber'
    )

def sanitize_input(user_input):
    if isinstance(user_input, str):
        sanitized_input = re.sub(r"[\'\"\\;]", '', user_input)
        sanitized_input = re.sub(r'<script.*?>.*?<\/script>|<.*?javascript:.*?>|<.*? on\w+=.*?>', '', sanitized_input, flags=re.IGNORECASE)
        return sanitized_input
    return user_input

def main(sqliny):
    
    df = pd.DataFrame(sqliny)

    # 1. Eliminar espacios en blanco al inicio y al final de las cadenas de texto
    df['NameEmploy'] = df['NameEmploy'].str.strip()

    # 2. Reemplazar valores faltantes
    df['ApellidoEmploy'].fillna(df['ApellidoEmploy'].mean(), inplace=False)

    # 3. Eliminar o reemplazar caracteres especiales para evitar XSS
    df['NameEmploy'] = df['NameEmploy'].str.replace(r'[^\w\s]', '', regex=True)
    df['ApellidoEmploy'] = df['ApellidoEmploy'].str.replace(r'[^\w\s]', '', regex=True)

    # 4. Validación y limpieza de correos electrónicos
    def validate_email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            return np.nan

    df['EmailEmploy'] = df['EmailEmploy'].apply(validate_email)

    # 5. Normalizar datos: convertir a minúsculas
    df['EmailEmploy'] = df['EmailEmploy'].str.lower()


    # 6. Prevenir inyección SQL sanitizando comentarios
    df['Comment'] = df['Comment'].str.replace(r"[\'\"\\;]", '', regex=True)

    # 7. Eliminar duplicados
    df.drop_duplicates(inplace=True)
