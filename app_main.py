from server import app
import server_stripe

_paths = {(getattr(r, "path", None), tuple(sorted(getattr(r, "methods", None) or []))) for r in app.routes}
for r in server_stripe.app.routes:
    key = (getattr(r, "path", None), tuple(sorted(getattr(r, "methods", None) or [])))
    if key not in _paths:
        app.router.routes.append(r)
