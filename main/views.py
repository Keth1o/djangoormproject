from django.http import HttpResponse
from django.urls import reverse
from formula import m1_func, m2_func

SUBSTANCES = ["Si", "Cu", "Ae", "Ti", "W", "Mg", "Pb", "Ge", "Latum", "H2O", "Гліцерин"]

def index(request):
    """Головна сторінка зі списком речовин"""
    html = "<h1>Список речовин</h1><ul>"
    for s in SUBSTANCES:
        url = reverse('substance_detail', args=[s])
        html += f'<li><a href="{url}">{s}</a></li>'
    html += "</ul>"
    return HttpResponse(html)

def substance_detail(request, name):
    """Сторінка з таблицею обчислень для вибраної речовини"""
    if name not in SUBSTANCES:
        return HttpResponse("<h1>Речовину не знайдено</h1>", status=404)

    # умовні значення параметрів (для прикладу)
    p0, t0, b, p20, pv20, vv = 1.2, 0.9, 0.003, 1.1, 0.8, 0.004

    # список температур від -20 до 10 з кроком 5
    temps = list(range(-20, 15, 5))

    rows = ""
    for t in temps:
        m1 = m1_func(p0, t0, b, t, p20)
        m = (p20 * (1 + b * 20) / (1 + b * t))  # базова маса
        m2 = m2_func(m, pv20, b, t, p20, vv)
        rows += f"<tr><td>{t} °C</td><td>{m1:.3f}</td><td>{m2:.3f}</td></tr>"

    html = f"""
    <h1>Результати для речовини: {name}</h1>
    <table border="1" cellpadding="8" style="border-collapse: collapse;">
        <tr><th>Температура</th><th>m1</th><th>m2</th></tr>
        {rows}
    </table>
    <p><a href="{reverse('index')}">⬅ Повернутись назад</a></p>
    """
    return HttpResponse(html)
