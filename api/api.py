from website import create_app

app = create_app()

# Vercel serverless function handler
def handler(request, *args, **kwargs):
    return app(request, *args, **kwargs)