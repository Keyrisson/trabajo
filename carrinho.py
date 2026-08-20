# Gerando um arquivo HTML para a página do Carrinho de Compras
# Incluindo um estilo CSS limpo e profissional conforme as diretrizes

html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carrinho | Livraria Multicultural</title>
    <style>
        :root {
            --primary: #2c3e50;
            --accent: #e74c3c;
            --success: #27ae60;
            --bg: #f9f9f9;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg);
            margin: 0;
            padding: 20px;
            color: #333;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background: #fff;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        h1 { color: var(--primary); margin-bottom: 1.5rem; }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 2rem;
        }

        th {
            text-align: left;
            padding: 1rem;
            border-bottom: 2px solid #ddd;
            color: #555;
        }

        td {
            padding: 1rem;
            border-bottom: 1px solid #eee;
        }

        .btn-remove {
            color: var(--accent);
            cursor: pointer;
            background: none;
            border: none;
            font-weight: bold;
        }

        .summary {
            text-align: right;
            border-top: 2px solid #eee;
            padding-top: 1rem;
        }

        .btn-checkout {
            background-color: var(--success);
            color: white;
            border: none;
            padding: 1rem 2rem;
            border-radius: 4px;
            font-size: 1.1rem;
            cursor: pointer;
            margin-top: 1rem;
            width: 100%;
        }

        .back-link { display: inline-block; margin-bottom: 1rem; color: var(--primary); }
    </style>
</head>
<body>

<div class="container">
    <a href="index.html" class="back-link">← Voltar à Loja</a>
    <h1>Meu Carrinho</h1>
    
    <table>
        <thead>
            <tr>
                <th>Produto</th>
                <th>Preço</th>
                <th>Quantidade</th>
                <th>Total</th>
                <th>Ação</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Cem Anos de Solidão</td>
                <td>R$ 49,90</td>
                <td><input type="number" value="1" min="1" style="width: 50px;"></td>
                <td>R$ 49,90</td>
                <td><button class="btn-remove">Remover</button></td>
            </tr>
            <tr>
                <td>O Pequeno Príncipe</td>
                <td>R$ 29,90</td>
                <td><input type="number" value="1" min="1" style="width: 50px;"></td>
                <td>R$ 29,90</td>
                <td><button class="btn-remove">Remover</button></td>
            </tr>
        </tbody>
    </table>

    <div class="summary">
        <p><strong>Subtotal:</strong> R$ 79,80</p>
        <p><strong>Frete:</strong> Grátis</p>
        <h3>Total: R$ 79,80</h3>
        <button class="btn-checkout">Finalizar Compra</button>
    </div>
</div>

</body>
</html>
"""

with open("carrinho.html", "w", encoding="utf-8") as f:
    f.write(html_content)
"""
"""