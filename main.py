import requests
import pandas as pd
import duckdb

# ===============================
# Baixa os dados da API
# ===============================

posts = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
).json()

usuarios = requests.get(
    "https://jsonplaceholder.typicode.com/users"
).json()

comentarios = requests.get(
    "https://jsonplaceholder.typicode.com/comments"
).json()

# ===============================
# Converte para DataFrame
# ===============================

df_posts = pd.DataFrame(posts)
df_usuarios = pd.DataFrame(usuarios)
df_comentarios = pd.DataFrame(comentarios)

# ===============================
# Conecta ao DuckDB
# ===============================

con = duckdb.connect("jsonplaceholder.duckdb")

# ===============================
# Salva as tabelas
# ===============================

con.execute("""
CREATE OR REPLACE TABLE posts AS
SELECT * FROM df_posts
""")

con.execute("""
CREATE OR REPLACE TABLE usuarios AS
SELECT * FROM df_usuarios
""")

con.execute("""
CREATE OR REPLACE TABLE comentarios AS
SELECT * FROM df_comentarios
""")

# ===============================
# Consulta SQL
# ===============================

resultado = con.execute("""
SELECT
    p.id,
    p.title,
    u.name,
    u.email
FROM posts p
LEFT JOIN usuarios u
ON p.userId = u.id
LIMIT 20
""").fetchdf()

print(resultado)

con.close()