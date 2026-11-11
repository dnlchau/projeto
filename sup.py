import duckdb

# Conecta ao banco
con = duckdb.connect("jsonplaceholder.duckdb")

# Executa uma consulta
resultado = con.execute("""
SELECT *
FROM usuarios
""").fetchdf()

print(resultado)

con.close()
