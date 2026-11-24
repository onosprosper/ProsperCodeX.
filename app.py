from flask import Flask, render_template, Response

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('index.html')

@app.get('/health')
def health():
    return {'status': 'ok', 'site': 'ProsperCodeX'}


@app.get('/sitemap.xml')
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://prospercodex.onrender.com/</loc>
    </url>
</urlset>"""
    return Response(xml, mimetype="application/xml")


@app.get('/robots.txt')
def robots():
    content = """User-agent: *
Allow: /
Disallow: /health

Sitemap: https://prospercodex.onrender.com/sitemap.xml
"""
    return Response(content, mimetype="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
